from rest_framework.serializers import ModelSerializer
from .models import student


class StandardSerializer(ModelSerializer):
    class Meta:
        model = student
        fields = ['school_id', 'standard_id',  'id', 'name',
                  'phone', 'email', 'gender', 'dob', 'address', 'admission_date', 'result', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
