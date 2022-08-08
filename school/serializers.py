from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import School


class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = ['school_code', 'school_name',
                  'email', 'phone_no', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
