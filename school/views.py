from datetime import datetime, timedelta, timezone
from rest_framework import exceptions
from rest_framework.views import APIView
from school.authentication import JWTAuthentication, create_access_token, create_refresh_token, decode_refresh_token
from .models import School, Usertoken
from .serializers import SchoolSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.


class LoginAPIView(APIView):
    def post(self, request):
        response = Response()
        email = request.data['email']
        password = request.data['password']

        user = School.objects.filter(email=email).first()
        schid = user.schoolId
        print(schid)
        if user is None:
            raise exceptions.AuthenticationFailed({
                'data': {},
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Login UnSuccessfull'
            })

        if not user.check_password(password):
            data = {
                'data': {},
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Login UnSuccessfull'
            }
            raise exceptions.AuthenticationFailed(data)

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        Usertoken.objects.create(user_id=user.id,
                                 token=refresh_token,
                                 expired_at=datetime.utcnow() + timedelta(days=7)
                                 )

        response.set_cookie(key='refresh_token',
                            value=refresh_token, httponly=True)
        response.data = {
            'data': {'token': access_token, 'schoolId': user.id},
            'status': status.HTTP_200_OK,
            'message': 'Login Successfull'
        }
        return response


class UserAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        data = SchoolSerializer(request.user).data
        if not data:
            return Response({
                'data': {},
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Fetching UnSuccessfull'
            })
        else:
            return Response({
                'data': data,
                'status': status.HTTP_200_OK,
                'message': 'Success Krunal'
            })


class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')

        id = decode_refresh_token(refresh_token)

        if not Usertoken.objects.filter(user_id=id,
                                        token=refresh_token,
                                        expired_at__gt=datetime.now(tz=timezone.utc)).exists():
            raise exceptions.AuthenticationFailed(data={
                'data': {},
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Refresh UnSuccessfull'
            })
        access_token = create_access_token(id)
        return Response({
            'data': {'token': access_token},
            'status': status.HTTP_200_OK,
            'message': 'Refresh Successfull'})


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
    # authentication_classes = [JWTAuthentication]
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['schoolId']

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'data': response.data, 'status': status.HTTP_200_OK, 'message': 'Data Found Successfully'}
        return response
