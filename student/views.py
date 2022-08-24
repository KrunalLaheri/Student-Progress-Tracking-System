from datetime import datetime, timedelta, timezone
import email
from email import header
from msilib.schema import ListView
from rest_framework import exceptions
from rest_framework.views import APIView
from school.authentication import StandardJWTAuthentication, StudentJWTAuthentication, create_access_token, create_refresh_token, decode_refresh_token
from .models import student, Usertoken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from student.serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend


class StudentLoginAPIView(APIView):
    def post(self, request):
        semail = request.data['email']
        spassword = request.data['password']

        user = student.objects.filter(
            email=semail, password=spassword).first()
        if user is None:
            # data = {
            #     'data': {},
            #     'status': status.HTTP_400_BAD_REQUEST,
            #     'message': 'Login UnSuccessfull'
            # }
            raise exceptions.AuthenticationFailed({
                'data': {},
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Login Unsuccessfull'
            })

        access_token = create_access_token(user.studentId)
        refresh_token = create_refresh_token(user.studentId)

        Usertoken.objects.create(user_id=user.studentId,
                                 token=refresh_token,
                                 expired_at=datetime.utcnow() + timedelta(days=7)
                                 )
        response = Response()
        response.set_cookie(key='refresh_token',
                            value=refresh_token, httponly=True)
        response.data = {
            'data': {'token': access_token},
            'status': status.HTTP_200_OK,
            'message': 'Login Successfull',
            'studentId': user.studentId
        }
        return response


class StudentUserAPIView(APIView):
    authentication_classes = [StudentJWTAuthentication]

    def get(self, request):
        return Response({
            'data': StudentSerializer(request.user).data,
            'status': status.HTTP_200_OK,
            'message': 'Success'})


class StudentRefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')

        id = decode_refresh_token(refresh_token)

        if not Usertoken.objects.filter(user_id=id,
                                        token=refresh_token,
                                        expired_at__gt=datetime.now(tz=timezone.utc)).exists():
            raise exceptions.AuthenticationFailed({
                'data': {},
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Refresh UnSuccessfull'
            })
        access_token = create_access_token(id)
        return Response(
            {
                'data': {'token': access_token},
                'status': status.HTTP_200_OK,
                'message': 'Refresh Successfull'})


class StudentLogoutAPIView(APIView):

    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        Usertoken.objects.filter(token=refresh_token).delete()
        response = Response()
        response.delete_cookie(key='refresh_token')
        response.data = {
            'message': 'success',
            'status': status.HTTP_200_OK,
            'message': 'Logout Successfull'
        }

        return response


class StudentList(ListAPIView):
    # authentication_classes = [StudentJWTAuthentication]
    queryset = student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['classId', 'schoolId', 'studentId']
    # lookup_field = 'schoolId'/////////////////////////////////////////////new API for lokking for a single student based on ID
    # def get_queryset(self):
    #     user = self.request.user
    #     return student.objects.filter(school_id=user)

    # def get(self, request):
    #     queryset = StudentSerializer(student.objects.all())
    #     response = Response()
    #     response.data = {
    #         'status': status.HTTP_200_OK,
    #         'message': 'test',
    #         'data': queryset.data
    #     }
    #     return response

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data, 'status': status.HTTP_200_OK, 'message': 'Data Found Successfully'}
        return response


class StudentCreate(CreateAPIView):
    # authentication_classes = [StudentJWTAuthentication]
    queryset = student.objects.all()
    serializer_class = StudentSerializer
    # response = Response()
    # response.data = {
    #     'message': 'success',
    #     'status': status.HTTP_200_OK,
    #     'message': 'Logout Successfull'
    # }

    # return response

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        data = {
            'data': {},
            'Message': 'You have successfully register',
            'status': status.HTTP_200_OK,
        }
        return Response(data)
        # else:
        #     data = {
        #         'data': {},
        #         'Message': 'You have successfully register',
        #         'status': status.HTTP_400_BAD_REQUEST,
        #     }
        #     return Response(data)
