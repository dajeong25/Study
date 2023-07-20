# -*- coding: utf-8 -*-

from django.urls import path
from . import views

urlpatterns = [
    path("join/", views.join),   # http://localhost:8000/member/join/
    path('login/', views.login), # http://localhost:8000/member/login/
    path('main/', views.main),   # http://localhost:8000/member/main/
    path('logout/', views.logout), # http://localhost:8000/member/main/
    path('info/<str:id>/', views.info),   # http://localhost:8000/member/info/{{request.session.login}}/
    path('list/', views.list),   # http://127.0.0.1:8000/member/list/
    path('picture/', views.picture), #http://127.0.0.1:8000/member/picture/
]
