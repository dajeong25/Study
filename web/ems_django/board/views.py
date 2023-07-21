from django.shortcuts import render
from .models import Board
from django.http import HttpResponseRedirect
from django.utils import timezone #.now() 현재 일시
from django.core.paginator import Paginator
import traceback

# Create your views here.
def write(request):
    if request.method != "POST":
        return render(request, "board/write.html")
    else:
        try:
            filename = request.FILES["file1"].name
            handle_upload(request.FILES["file1"])
        except: filename=""

        b = Board(name = request.POST["name"]
                  , pw=request.POST["pw"]
                  , title=request.POST["title"]
                  , content=request.POST['content']
                  , regdate=timezone.now()
                  , readcnt=0
                  , file1=filename)
        b.save()
        return HttpResponseRedirect("../list")

def handle_upload(f):
    #업로드위치 : BASE_DIR/file/board 폴더
    with open(f"file/board/{f.name}", "wb") as dest:
        for ch in f.chunks():
            dest.write(ch)

def list(request):
    # get방식에서 전달받은 pageNum 파라미터값
    # pageNum가 없으면 1로 설정
    pageNum = int(request.GET.get("pageNum",1))
    # Board.objects.all() : board 테이블의 모든 정보 조회
    # .order_by("num") : 오름차순 정렬 1 2 3 
    # .order_by("-num") : 내림차순 3 2 1
    all_boards = Board.objects.all().order_by("-num")
    # 10개씩 묶어서 그룹화
    paginator = Paginator(all_boards, 10)
    # 조회하는 pageNum 번째의 게시글 목록 저장. 화면에 출력할 게시물목록
    board_list = paginator.get_page(pageNum)
    listcount = Board.objects.count() #등록된 레코드 건수
    return render(request, "board/list.html", 
                  {"board":board_list, "listcount":listcount})

def info(request, num):
    board = Board.objects.get(num=num) #num 값에 해당하는 게시물 1건 조회
    board.readcnt += 1 # 조회 건수 1 중가
    board.save()       # 게시물 수정 :: 조회 건수 1 증가 되어 저장 
    return render(request, "board/info.html", {'b':board})


def update(request, num):
    if request.method != 'POST':
        board = Board.objects.get(num=num)
        return render(request, 'board/update.html',{'b': board})
    else :
        board = Board.objects.get(num=num)
        pw = request.POST["pw"]
        if board.pw != pw :
            context = {"msg":"비밀번호 오류","url":"../../update/"+str(num) + "/"}
            return render(request,"alert.html",context)
        try :
            filename = request.FILES["file1"].name
            handle_upload(request.FILES["file1"])
        except :
            filename = ""
        try :
            if filename == "" :
               filename = request.POST["file2"]
            b=Board(num=num,\
                    name=request.POST["name"],\
                    pw=request.POST["pw"],\
                    title=request.POST["title"],\
                    content=request.POST["content"],\
                    file1=filename)   
            b.save()
            return HttpResponseRedirect("../../list/")
        except Exception as e :
            print(traceback.format_exc()) #runserver 콘솔창에 오류 메세지 출력
            context = {"msg":"게시물 수정 실패",\
                       "url":"../../update/"+str(num) + "/"}
            return render(request,"alert.html",context)

# 게시물 삭제하기
def delete (request, num):
    if request.method != 'POST':
        return render(request, 'board/delete.html',{"num":num})
    else :
       b=Board.objects.get(num=num)
       pw = request.POST["pw"]
       if pw != b.pw :
          context = {"msg":"비밀번호 오류",\
                       "url":"../../delete/"+str(num) + "/"}
          return render(request,"alert.html",context)
       try :
          b.delete()
          return HttpResponseRedirect("../../list/")
       except :
          print(traceback.format_exc()) #runserver 콘솔창에 오류 메세지 출력
          context = {"msg":"게시물 삭제 실패",\
                       "url":"../../delete/"+str(num) + "/"}
          return render(request,"alert.html",context)
      