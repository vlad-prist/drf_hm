# Generated by Django 5.0.7 on 2024-08-16 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0011_course_last_update'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='last_update',
        ),
    ]
