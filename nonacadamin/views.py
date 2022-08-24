from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import categori, subcategory, level, participation
from .serializers import CategoriSerializer, SubcategorySerializer, LevelSerializer, ParticipationSerializer
from rest_framework.response import Response
from rest_framework import status


class CategoriList(ListAPIView):
    queryset = categori.objects.all()
    serializer_class = CategoriSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['catId']
    # filter_backends = [SearchFilter]
    # search_fields = ['id']        // we can only search fields which is CharField or TextField

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data, 'status': status.HTTP_200_OK, 'message': 'Data Found Successfully'}
        return response


class CategoriCreate(CreateAPIView):
    queryset = categori.objects.all()
    serializer_class = CategoriSerializer

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


class SubcategoryList(ListAPIView):
    queryset = subcategory.objects.all()
    serializer_class = SubcategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['subCatId']

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data, 'status': status.HTTP_200_OK, 'message': 'Data Found Successfully'}
        return response


class SubcategoryCreate(CreateAPIView):
    queryset = subcategory.objects.all()
    serializer_class = SubcategorySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {
            'data': {},
            'Message': 'You have successfully register sub-category',
            'status': status.HTTP_200_OK,
        }
        return Response(data)


class LevelList(ListAPIView):
    queryset = level.objects.all()
    serializer_class = LevelSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['schoolId',  'classId', 'examId', 'examName']

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data, 'status': status.HTTP_200_OK, 'message': 'Data Found Successfully'}
        return response


class LevelCreate(CreateAPIView):
    queryset = level.objects.all()
    serializer_class = LevelSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {
            'data': {},
            'Message': 'You have successfully register level',
            'status': status.HTTP_200_OK,
        }
        return Response(data)


class ParticipationList(ListAPIView):
    queryset = participation.objects.all()
    serializer_class = ParticipationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['schoolId',  'classId', 'studentId']

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data, 'status': status.HTTP_200_OK, 'message': 'Data Found Successfully'}
        return response


class ParticipationCreate(CreateAPIView):
    queryset = participation.objects.all()
    serializer_class = ParticipationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {
            'data': {},
            'status': status.HTTP_200_OK,
            'message': 'You have successfully register participation'
        }
        return Response(data)
