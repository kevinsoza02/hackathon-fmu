from django.contrib import admin
from django.urls import path
from market.views import *

urlpatterns = [
    path('', IndexView.as_view()),
]
