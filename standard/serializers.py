from rest_framework.serializers import ModelSerializer
from .models import standard, subject


class StandardSerializer(ModelSerializer):
    class Meta:
        model = standard
        fields = ['school_id',  'id', 'name',
                  'email', 'phone', 'password', 'subject']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = subject
        fields = ['subject_id', 'subject_name']
