from rest_framework.serializers import ModelSerializer

from nonacadamin.models import categori, level, participation, subcategory


class CategoriSerializer(ModelSerializer):
    class Meta:
        model = categori
        fields = ['catId', 'catName']


class SubcategorySerializer(ModelSerializer):
    class Meta:
        model = subcategory
        fields = ['subCatId', 'catId', 'subCatName']


class LevelSerializer(ModelSerializer):
    class Meta:
        model = level
        fields = ['lvlId', 'lvlName']


class ParticipationSerializer(ModelSerializer):
    class Meta:
        model = participation
        fields = ['coCurricularId', 'schoolId', 'classId', 'studentId', 'category',
                  'subCategory',  'studentName', 'name', 'level', 'points', 'year', 'date', 'isVerified', 'desc']
