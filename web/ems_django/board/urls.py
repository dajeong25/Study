# -*- coding: utf-8 -*-

from django.urls import path
from . import views


urlpatterns=[
    path("write/", views.write),
    path("list/", views.list),
]

