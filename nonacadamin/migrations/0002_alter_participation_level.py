# Generated by Django 4.0.6 on 2022-08-22 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nonacadamin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nonacadamin.level'),
        ),
    ]
