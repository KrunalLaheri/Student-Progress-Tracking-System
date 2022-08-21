from django.contrib import admin
from django.urls import path, include
from result.views import ExamList, ExamCreate, ResultList, ResultCreate

urlpatterns = [
    path('examlist/', ExamList.as_view()),
    path('examcreate/', ExamCreate.as_view()),
    path('resultlist/', ResultList.as_view()),
    path('resultcreate/', ResultCreate.as_view())
]
