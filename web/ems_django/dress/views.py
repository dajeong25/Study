from django.shortcuts import render
from pathlib import Path
from .dress import predict

basedir = str(Path.cwd())
# basedir #'D:\\emspy\\python_web\\emsjango'

def index(request):
    if request.method != "POST":
        return render(request, "dress/index.html")
    else:
        try:
            img = handle_upload(request.FILES['dress'])
        except Exception as ex:
            print(ex)
            result = "이미지를 선택해주세요"
            return render(request, "dress/index.html"
                          , {"result" : result})
            
        result = predict(basedir + '/file/dress/dress.jpg')
        return render(request, "dress/index.html"
                      , {'img':"/file/dress/dress.jpg", "result" : result})

def handle_upload(f):
    with open(basedir + '/file/dress/dress.jpg', "wb") as dest:
        for ch in f.chunks():
            dest.write(ch) #/file/dress/dress.jpg에 저장

