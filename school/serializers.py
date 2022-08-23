from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import School


class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'schoolId', 'name',
                  'email', 'phone', 'address', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
