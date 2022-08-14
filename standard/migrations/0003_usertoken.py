# Generated by Django 4.0.6 on 2022-08-09 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0002_alter_standard_standard_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usertoken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('token', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expired_at', models.DateTimeField()),
            ],
        ),
    ]