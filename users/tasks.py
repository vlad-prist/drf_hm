from datetime import timedelta, datetime
from celery import shared_task
from django.core.mail import send_mail
from config import settings
from users.models import User


@shared_task
def check_active_users():
    inactive_users = User.objects.filter(last_login__isnull=False, is_active=True, is_superuser=False)
    now = datetime.now()
    for user in inactive_users:
        if now - user.last_login > timedelta(days=31):
            user.is_active = False
            user.save()
            print(f'Пользователь с email: {user.email} был заблокирован, ввиду отсутствия онлайн более 30 дней')
            send_mail(
                subject='Блокировка',
                message=f'Пользователь с email: {user.email} был заблокирован, ввиду отсутствия онлайн более 30 дней',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email]
            )
