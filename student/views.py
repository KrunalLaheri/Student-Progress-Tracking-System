from datetime import datetime, timedelta, timezone
import email
from msilib.schema import ListView
from rest_framework import exceptions
from rest_framework.views import APIView
from school.authentication import StudentJWTAuthentication, create_access_token, create_refresh_token, decode_refresh_token
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
            raise exceptions.AuthenticationFailed('Invalid Credintials')

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
            'token': access_token,
            'status': status.HTTP_200_OK,
            'message': 'Login Successfull'
        }
        return response


class StudentUserAPIView(APIView):
    authentication_classes = [StudentJWTAuthentication]

    def get(self, request):
        return Response(StudentSerializer(request.user).data)


class StudentRefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')

        id = decode_refresh_token(refresh_token)

        if not Usertoken.objects.filter(user_id=id,
                                        token=refresh_token,
                                        expired_at__gt=datetime.now(tz=timezone.utc)).exists():
            raise exceptions.AuthenticationFailed('unsuthenticated')
        access_token = create_access_token(id)
        return Response({'token': access_token})


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
    queryset = student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['classId', 'schoolId', 'studentId']
    # def get_queryset(self):
    #     user = self.request.user
    #     return student.objects.filter(school_id=user)


class StudentCreate(CreateAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer
