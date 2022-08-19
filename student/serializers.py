from rest_framework.serializers import ModelSerializer
from .models import student


class StudentSerializer(ModelSerializer):
    class Meta:
        model = student
        fields = ['schoolId', 'standardId',  'id', 'name',
                  'phone', 'email', 'gender', 'dob', 'address', 'admissionDate', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
