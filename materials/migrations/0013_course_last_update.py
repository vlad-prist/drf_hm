# Generated by Django 5.0.7 on 2024-08-19 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0012_remove_course_last_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='last_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Последнее обновление'),
        ),
    ]
