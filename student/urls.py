from django.contrib import admin
from django.urls import path, include
from student import views
from rest_framework.routers import DefaultRouter

from student.views import StudentLoginAPIView, StudentUserAPIView, StudentRefreshAPIView, StudentLogoutAPIView

urlpatterns = [
    path('studentlogin/', StudentLoginAPIView.as_view()),
    path('studentuser/', StudentUserAPIView.as_view()),
    path('studentrefresh/', StudentRefreshAPIView.as_view()),
    path('studentlogout/', StudentLogoutAPIView.as_view()),
    path('studentcreate/', views.StudentCreate.as_view()),
    path('studentlist/', views.StudentList.as_view()),
]
