# -*- coding: utf-8 -*-
from django.shortcuts import render

def loginIdchk(func):
    def check(request, id):
        try:
            login = request.session["login"]
        except:
            context = {'msg' : "로그인하세요", "url":"../../login"}
            return render(request, "alert.html", context)
        else:
            if login != id and login != "admin":
                context = {'msg':"본인만 거래 가능합니다", "url":"../../main"}
                return render(request, "alert.html", context)
        return func(request, id)
    return check


def adminChk(func):
    def check(request):
        try:
            login = request.session["login"]
        except:
            context = {'msg' : "로그인하세요", "url":"../login"}
            return render(request, "alert.html", context)
        else:
            if login != "admin":
                context = {'msg':"관리자만 조회가능합니다.", "url":"../main"}
                return render(request, "alert.html", context)
        return func(request)
    return check
