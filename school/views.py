from datetime import datetime, timedelta, timezone
from rest_framework import exceptions
from rest_framework.views import APIView
from school.authentication import JWTAuthentication, create_access_token, create_refresh_token, decode_refresh_token
from .models import School, Usertoken
from .serializers import SchoolSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView

# Create your views here.


class LoginAPIView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = School.objects.filter(email=email).first()
        if user is None:
            raise exceptions.AuthenticationFailed('Invalid Credintials')

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Invalid Credintials')

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        Usertoken.objects.create(user_id=user.id,
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


class UserAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        return Response(SchoolSerializer(request.user).data)


class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')

        id = decode_refresh_token(refresh_token)

        if not Usertoken.objects.filter(user_id=id,
                                        token=refresh_token,
                                        expired_at__gt=datetime.now(tz=timezone.utc)).exists():
            raise exceptions.AuthenticationFailed('unsuthenticated')
        access_token = create_access_token(id)
        return Response({'token': access_token})


class LogoutAPIView(APIView):

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


class SchoolList(ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
