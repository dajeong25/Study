from django.shortcuts import render
from .models import Member
from django.http import HttpResponseRedirect
from django.contrib import auth
from deco.deco import loginIdchk, adminChk

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
                        email=request.POST["email"])
        # insert 구문 실행
        member.save() 
        # HttpResponseRedirect : 브라우저에서 login url을 재요청하도록 명령
        # "POST /member/join/ HTTP/1.1" 302 0 : 302가 rediect
        return HttpResponseRedirect("../login/")


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
        fname = request.FILES['picture'].name  #업로드된 파일의 이름
        handle_upload(request.FILES['picture'])
        return render(request, "member/picture.html", {'fname':fname})

def handle_upload(f): # f: 파일의 내용(stream)
    # wb(write binary) mode
    with open("file/picture/"+f.name, 'wb') as dest:
        for ch in f.chunks():
            dest.write(ch)





