from rest_framework import exceptions
from datetime import datetime, timedelta
import jwt
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from .models import School


# in create_access_token(id) in id we pass id of the user


def create_access_token(id):
    return jwt.encode(
        {
            'user_id': id,
            'exp': datetime.utcnow()+timedelta(seconds=30),
            'iat': datetime.utcnow()

        }, 'access_secret', algorithm='HS256')


def create_refresh_token(id):
    return jwt.encode(
        {
            'user_id': id,
            'exp': datetime.utcnow()+timedelta(days=7),
            'iat': datetime.utcnow()

        }, 'refresh_secret', algorithm='HS256')


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)
            user = School.objects.get(pk=id)
            return (user, None)

        return exceptions.AuthenticationFailed('Unauthenticated User')


def decode_access_token(token):
    try:
        payload = jwt.decode(token, 'access_secret', algorithms='HS256')
        return payload['user_id']
    except Exception as e:
        print(e)
        raise exceptions.AuthenticationFailed('unauthenticated')


def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, 'refresh_secret', algorithms='HS256')
        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('unauthenticated')
