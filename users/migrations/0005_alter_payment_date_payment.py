# Generated by Django 5.0.7 on 2024-07-31 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='date_payment',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата оплаты'),
        ),
    ]