from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import School


class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = ['schoolId', 'name',
                  'email', 'phone', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
