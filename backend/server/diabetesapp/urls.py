# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 21:56:31 2020

@author: Asus
"""

from django.urls import path
from diabetesapp import views

urlpatterns = [
    path('',views.index_page),
    path('predictdiabetes', views.predict_diabetes),
]