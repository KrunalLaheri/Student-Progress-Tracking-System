from .models import exam, result
from rest_framework.serializers import ModelSerializer


class ExamSerializer(ModelSerializer):
    class Meta:
        model = exam
        fields = ['schoolId',  'standardId', 'examId', 'examName']


class ResultSerializer(ModelSerializer):
    class Meta:
        model = result
        fields = ['schoolId', 'standardId',
                  'studentId', 'resultId', 'examName', 'data', 'year']
