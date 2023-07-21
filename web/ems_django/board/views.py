from django.shortcuts import render
from .models import Board
from django.http import HttpResponseRedirect
from django.utils import timezone

# Create your views here.
def write(request):
    if request.method != "POST":
        return render(request, "board/write.html")
    else:
        try:
            filename = request.FILES["file1"].name
            handle_upload(request.FILES["file1"])
        except: filename=""
        else:
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
    return render(request, "board/list.html")
