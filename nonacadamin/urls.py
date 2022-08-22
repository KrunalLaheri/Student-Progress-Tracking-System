from django.contrib import admin
from django.urls import path, include
from nonacadamin.views import CategoriList, CategoriCreate, SubcategoryList, SubcategoryCreate, LevelList, LevelCreate, ParticipationList, ParticipationCreate

urlpatterns = [
    path('categorilist/', CategoriList.as_view()),
    path('subcategorilist/', SubcategoryList.as_view()),
    path('levellist/', LevelList.as_view()),
    path('participationlist/', ParticipationList.as_view()),
    path('categoricreate/', CategoriCreate.as_view()),
    path('subcategoricreate/', SubcategoryCreate.as_view()),
    path('levelcreate/', LevelCreate.as_view()),
    path('participationcreate/', ParticipationCreate.as_view()),

]
