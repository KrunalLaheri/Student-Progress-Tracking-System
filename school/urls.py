from django.urls import path, include

from school.views import LoginAPIView, LogoutAPIView, RefreshAPIView, UserAPIView

urlpatterns = [
    path('login', LoginAPIView.as_view()),
    path('user', UserAPIView.as_view()),
    path('refresh', RefreshAPIView.as_view()),
    path('logout', LogoutAPIView.as_view())
]
