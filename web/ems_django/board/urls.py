# -*- coding: utf-8 -*-
from django.urls import path
from . import views


urlpatterns=[
    path("write/", views.write),
    path("list/", views.list),
    path("info/<int:num>/", views.info),
    path('update/<int:num>/', views.update),
    path('delete/<int:num>/', views.delete),
]

