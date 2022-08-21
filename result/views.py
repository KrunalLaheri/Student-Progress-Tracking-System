from django.shortcuts import render

from result.serializers import ExamSerializer, ResultSerializer
from .models import exam, result
from rest_framework.generics import ListAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class ExamList(ListAPIView):
    queryset = exam.objects.all()
    serializer_class = ExamSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['schoolId',  'classId', 'examId', 'examName']
    # filter_backends = [SearchFilter]
    # search_fields = ['id']        // we can only search fields which is CharField or TextField


class ExamCreate(CreateAPIView):
    queryset = exam.objects.all()
    serializer_class = ExamSerializer


class ResultList(ListAPIView):
    queryset = result.objects.all()
    serializer_class = ResultSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['schoolId', 'classId',
                        'studentId', 'resultId', 'examName', 'year']
    # filter_backends = [SearchFilter]
    # search_fields = ['id']        // we can only search fields which is CharField or TextField


class ResultCreate(CreateAPIView):
    queryset = result.objects.all()
    serializer_class = ResultSerializer
