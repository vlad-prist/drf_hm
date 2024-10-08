# Generated by Django 5.0.7 on 2024-08-16 09:40

import django_celery_beat.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_payment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default=django_celery_beat.utils.now, verbose_name='Время последнего посещения'),
        ),
    ]
