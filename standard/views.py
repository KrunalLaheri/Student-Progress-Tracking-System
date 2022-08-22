from datetime import datetime, timedelta, timezone
import email
from rest_framework import exceptions
from rest_framework.views import APIView
from school.authentication import StandardJWTAuthentication, create_access_token, create_refresh_token, decode_refresh_token
from .models import standard, subject, Usertoken
from .serializers import StandardSerializer, SubjectSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter


class StandardLoginAPIView(APIView):
    def post(self, request):
        sid = request.data['email']
        spassword = request.data['password']

        user = standard.objects.filter(email=sid, password=spassword).first()
        if user is None:
            data = {
                'data': {},
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Login UnSuccessfull'
            }
            raise exceptions.AuthenticationFailed(data)

        access_token = create_access_token(user.classId)
        refresh_token = create_refresh_token(user.classId)

        Usertoken.objects.create(user_id=user.classId,
                                 token=refresh_token,
                                 expired_at=datetime.utcnow() + timedelta(days=7)
                                 )
        response = Response()
        response.set_cookie(key='refresh_token',
                            value=refresh_token, httponly=True)
        response.data = {
            'data': {'token': access_token},
            'status': status.HTTP_200_OK,
            'message': 'Login Successfull'
        }
        return response


class StandardUserAPIView(APIView):
    authentication_classes = [StandardJWTAuthentication]

    def get(self, request):
        return Response(
            {
                'data': StandardSerializer(request.user).data,
                'status': status.HTTP_200_OK,
                'message': 'Success'
            })


class StandardRefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')

        id = decode_refresh_token(refresh_token)

        if not Usertoken.objects.filter(user_id=id,
                                        token=refresh_token,
                                        expired_at__gt=datetime.now(tz=timezone.utc)).exists():
            data = {
                'data': {},
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Login UnSuccessfull'
            }
            raise exceptions.AuthenticationFailed(data)
        access_token = create_access_token(id)
        return Response({
            'data': {'token': access_token},
            'status': status.HTTP_200_OK,
            'message': 'Refresh Successfull'})


class StandardLogoutAPIView(APIView):

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


class StandardList(ListAPIView):
    queryset = standard.objects.all()
    serializer_class = StandardSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['schoolId', 'classId']
    # filter_backends = [SearchFilter]
    # search_fields = ['id']        // we can only search fields which is CharField or TextField


class StandardCreate(CreateAPIView):
    queryset = standard.objects.all()
    serializer_class = StandardSerializer
