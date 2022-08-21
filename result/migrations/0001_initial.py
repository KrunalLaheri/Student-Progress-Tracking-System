# Generated by Django 4.0.6 on 2022-08-19 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('standard', '0007_rename_school_id_standard_schoolid_and_more'),
        ('student', '0005_rename_admission_date_student_admissiondate_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='exam',
            fields=[
                ('examId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('examName', models.CharField(max_length=20)),
                ('schoolId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('standardId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='standard.standard')),
            ],
        ),
        migrations.CreateModel(
            name='result',
            fields=[
                ('resultId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('data', models.JSONField()),
                ('year', models.DateField()),
                ('examName', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='result.exam')),
                ('schoolId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('standardId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='standard.standard')),
                ('studentId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student.student')),
            ],
        ),
    ]
