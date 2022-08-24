from .models import exam, result
from rest_framework.serializers import ModelSerializer


class ExamSerializer(ModelSerializer):
    class Meta:
        model = exam
        fields = ['schoolId',  'classId', 'examId', 'examName']


class ResultSerializer(ModelSerializer):
    class Meta:
        model = result
        fields = ['schoolId', 'classId',
                  'studentId', 'resultId', 'sem', 'year', 'data', 'studentName', 'avg']
