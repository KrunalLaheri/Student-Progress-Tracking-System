from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import categori, subcategory, level, participation
from .serializers import CategoriSerializer, SubcategorySerializer, LevelSerializer, ParticipationSerializer


class CategoriList(ListAPIView):
    queryset = categori.objects.all()
    serializer_class = CategoriSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['schoolId',  'classId', 'examId', 'examName']
    # filter_backends = [SearchFilter]
    # search_fields = ['id']        // we can only search fields which is CharField or TextField


class CategoriCreate(CreateAPIView):
    queryset = categori.objects.all()
    serializer_class = CategoriSerializer


class SubcategoryList(ListAPIView):
    queryset = subcategory.objects.all()
    serializer_class = SubcategorySerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['schoolId',  'classId', 'examId', 'examName']


class SubcategoryCreate(CreateAPIView):
    queryset = subcategory.objects.all()
    serializer_class = SubcategorySerializer


class LevelList(ListAPIView):
    queryset = level.objects.all()
    serializer_class = LevelSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['schoolId',  'classId', 'examId', 'examName']


class LevelCreate(CreateAPIView):
    queryset = level.objects.all()
    serializer_class = LevelSerializer


class ParticipationList(ListAPIView):
    queryset = participation.objects.all()
    serializer_class = ParticipationSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['schoolId',  'classId', 'examId', 'examName']


class ParticipationCreate(CreateAPIView):
    queryset = participation.objects.all()
    serializer_class = ParticipationSerializer
