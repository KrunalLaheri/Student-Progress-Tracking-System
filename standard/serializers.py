from rest_framework.serializers import ModelSerializer
from .models import standard, subject


class StandardSerializer(ModelSerializer):
    class Meta:
        model = standard
        fields = ['schoolId',  'classId', 'className', 'teacherName',
                  'email', 'phone', 'password', 'profilePhoto']
        #   'subject'
        extra_kwargs = {
            'password': {'write_only': True}
        }


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = subject
        fields = ['subjectId', 'subjectName']
