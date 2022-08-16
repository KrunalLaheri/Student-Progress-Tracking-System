from django.contrib import admin
from django.urls import path, include
from standard import views
from rest_framework.routers import DefaultRouter

from standard.views import StandardCreate, StandardList, StandardLoginAPIView, StandardUserAPIView, StandardRefreshAPIView, StandardLogoutAPIView

urlpatterns = [
    path('standardlogin/', StandardLoginAPIView.as_view()),
    path('standarduser/', StandardUserAPIView.as_view()),
    path('standardrefresh/', StandardRefreshAPIView.as_view()),
    path('standardlogout/', StandardLogoutAPIView.as_view()),
    path('standardlist/', StandardList.as_view()),
    path('standardcreate/', StandardCreate.as_view()),
]
