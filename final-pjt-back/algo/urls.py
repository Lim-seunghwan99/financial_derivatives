# final_pjt_back/urls.py
from django.contrib import admin
from django.urls import path, include
from algo.views import UserProfileAPIView

urlpatterns = [
    path('<str:username>/', UserProfileAPIView.as_view(), name='user-profile'),
]
