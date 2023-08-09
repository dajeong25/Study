# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 15:25:03 2023
"""
from django.urls import path
from . import views

urlpatterns = [
    path("exchange", views.exchange),
    path("select", views.select),
    ]

