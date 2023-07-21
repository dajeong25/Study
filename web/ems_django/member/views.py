from django.shortcuts import render
from .models import Member
from django.http import HttpResponseRedirect
from django.contrib import auth
from deco.deco import loginIdchk, adminChk, loginchk

# Create your views here.
# request : 요청객체, 요청정보를 저장
def join(request):
    if request.method != "POST":
        # /templates/member/join.html => Template파일 호출
        return render(request, 'member/join.html')
    else:
        # POST 방식 요청 : 파라미터 존재
        member = Member(id=request.POST["id"], \
                        pw=request.POST["pw"], \
                        name=request.POST["name"], \
                        gender=request.POST["gender"], \
                        tel=request.POST["tel"], \
                        email=request.POST["email"], \
                        picture = request.POST["picture"])
        # insert 구문 실행
        member.save() 
        # HttpResponseRedirect : 브라우저에서 login url을 재요청하도록 명령
        # "POST /member/join/ HTTP/1.1" 302 0 : 302가 rediect
        return HttpResponseRedirect("../login/")


# session 객체 > 브라우저 환경 저장
# 장고에서는 자동으로 db에서 세션 관리 django_session
# 아이디 : id=hoo    ⇒ 1차확인
# 비밀번호 : pw=123  ⇒ 2차확인
def login(request):
    if request.method != "POST":
        return render(request, "member/login.html")
    else:
        # POST 방식 요청 : 파라미터 존재
        id=request.POST["id"]
        pw=request.POST["pw"]
        try:
            # Member.objects.get(id=id) : id파라미터의 값에 해당하는 member객체 조회
            member = Member.objects.get(id=id) #(Member.id = 파라미터id)
        except:
            #예외발생
            context = {'msg':"아이디를 확인하세요"}
            return render(request, "member/login.html", context)
        else:
            #정상처리
            # db에 저장된 비밀번호와 입력된 비밀번호 검증
            if member.pw == pw:
                request.session['login']=id  #로그인 세션 관리
                return HttpResponseRedirect("../main/")
            else:
                context={'msg':'비밀번호를 확인하세요'}
                return render(request, "member/login.html", context)
            
def main(request):
    return render(request, "member/main.html")

def logout(request):
    auth.logout(request) #session 정보 제거
    return HttpResponseRedirect("../login/")


### 검증필요!
# 1. 로그인된 경우2
# 2. 내정보만 조회가능. 단, 관리자인 경우 다른회원 정보 조회가능
## 1+2 조건 모두 만족해야만 조회 가능하도록 수정
@loginIdchk
def info(request, id): #id: admin 또는 아이디값
    # 1+2 조건 만족하는 경우만 실행
    member = Member.objects.get(id=id)
    return render(request, "member/info.html", {'mem':member})


## 실행조건
# 1. 로그인필수
# 2. 관리자여야만 실행
@adminChk
def list(request):
    mlist = Member.objects.all() #모든회원 목록 정보 조회
    return render(request, "member/list.html", {'mlist':mlist})


def picture(request):
    if request.method != "POST":
        return render(request, 'member/pictureform.html')
    else:
    # 파일 업로드 실행
    # <input type="file" name="picture" ...
    # request.FILES['picture'] : 파일의 내용
        fname = request.FILES['picture'].name   #업로드된 파일의 이름
        handle_upload(request.FILES['picture']) #파일업로드 기능
        return render(request, "member/picture.html", {'fname':fname})

def handle_upload(f): # f: 업로드된 파일의 내용(stream)
    # wb(write binary) mode
    # dest : 생성될 파일 - 파일을 만들어주는 것
    # file/picture/파일이름 >> 파일생성. 
    # BASE_DIR/file/picture 폴더에 생성
    with open("file/picture/"+f.name, 'wb') as dest:
        # f.chunks() : 버퍼크기만큼 파일 읽기
        for ch in f.chunks():
            dest.write(ch)


@loginIdchk
def update(request, id): 
    if request.method != "POST":
        member = Member.objects.get(id=id)
        return render(request, "member/update.html", {'mem':member})
    else:
        # 비밀번호 검증
        mem  = Member.objects.get(id=id) # 수정한 데이터 조회
        # request.POST['pw'] : 화면에 입력된 비밀번호
        # mem.pw : db에 등록된 비밀번호
        if request.POST['pw'] == mem.pw:
            member = Member(id=request.POST["id"], \
                            pw=request.POST["pw"], \
                            name=request.POST["name"], \
                            gender=request.POST["gender"], \
                            tel=request.POST["tel"], \
                            email=request.POST["email"], \
                            picture = request.POST["picture"])
            # id값 존재 : update / 없으면 insert
            member.save() #update 실행
            return HttpResponseRedirect(f"../../info/{id}/")
        else:
            context = {"msg":"비밀번호 오류입니다", "url":f"../../update/{id}/"}
            return render(request, "alert.html", context)

# 본인탈퇴 : 본인 비번검증.   로그아웃, 로그인화면 출력
# 강제탈퇴 : 관리자 비번검증. 회원목록 출력
@loginIdchk
def delete(request, id):
    if request.method != "POST":
        if id =="admin":
            context={'msg':'관리자는 탈퇴 불가입니다', 'url':'../../list/'}
            return render(request, 'alert.html', context)
        return render(request, "member/delete.html", {'id': id})
    else:
        login = request.session["login"]
        # member : 로그인한 회원의 정보
        member = Member.objects.get(id=login)
        if member.pw == request.POST['pw']: #비밀번호 일치
            mem = Member.objects.get(id=id)
            mem.delete() # mem : 탈퇴해야하는 회원 정보 delete
            if id == login : # 본인 탈퇴
                auth.logout(request)
                context = {'msg':'회원 탈퇴가 왼료되었습니다' ,'url':'../../login/'}
                return render(request, "alert.html", context)
            else: #관리자 강제탈퇴
                context = {'msg':'회원 탈퇴가 왼료되었습니다' ,'url':'../../list/'}
                return render(request, "alert.html", context)
        else:
            # 비밀번호 불일치
            context = {'msg':'비밀번호 오류' ,'url':f'../../delete/{id}/'}
            return render(request, "alert.html", context)

@loginchk 
def password(request):
    if request.method != "POST":
        return render(request, "member/passwordform.html")
    else: 
        # 입력된 비번 == db비번 검증
        login = request.session['login']
        member = Member.objects.get(id=login)
        if member.pw == request.POST['pw']:
            member.pw = request.POST["chgpw"]
            member.save()
            context = {'msg':'비밀번호 변경 성공'
                       , 'url':f'../info/{login}/'
                       , 'closer':True}
            return render(request, "member/password.html", context)
        else:
            context = {'msg':'비밀번호 오류' 
                       , 'url':'../password/'
                       , "closer":False}
            return render(request, "member/password.html", context)




