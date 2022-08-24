from django.shortcuts import render

from result.serializers import ExamSerializer, ResultSerializer
from .models import exam, result
from rest_framework.generics import ListAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from rest_framework.response import Response
from rest_framework import status


class ExamList(ListAPIView):
    queryset = exam.objects.all()
    serializer_class = ExamSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['schoolId',  'classId', 'examId', 'examName']
    # filter_backends = [SearchFilter]
    # search_fields = ['id']        // we can only search fields which is CharField or TextField

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data, 'status': status.HTTP_200_OK, 'message': 'Data Found Successfully'}
        return response


class ExamCreate(CreateAPIView):
    queryset = exam.objects.all()
    serializer_class = ExamSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {
            'data': {},
            'Message': 'You have successfully register category',
            'status': status.HTTP_200_OK,
        }
        return Response(data)


class ResultList(ListAPIView):
    queryset = result.objects.all()
    serializer_class = ResultSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['schoolId', 'classId',
                        'studentId', 'resultId', 'sem', 'year', 'studentName', 'avg']
    # filter_backends = [SearchFilter]
    # search_fields = ['id']        // we can only search fields which is CharField or TextField

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data, 'status': status.HTTP_200_OK, 'message': 'Data Found Successfully'}
        return response


class ResultCreate(CreateAPIView):
    queryset = result.objects.all()
    serializer_class = ResultSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {
            'data': {},
            'Message': 'You have successfully register category',
            'status': status.HTTP_200_OK,
        }
        return Response(data)
