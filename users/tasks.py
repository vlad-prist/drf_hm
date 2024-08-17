from datetime import timezone, timedelta
from celery import shared_task
from django.core.mail import send_mail

from config import settings
from users.models import User


# @shared_task
# def check_active_users():
#     users = User.objects.filter(is_active=True, is_superuser=False, is_stuff=False, last_login__isnull=False)
#     if users.exists():
#         for user in users:
#             if timezone.now - user.last_login > timedelta(minutes=1):
#                 user.is_active = False
#                 user.save()
#                 print(f'Пользователь с email: {user.email} был заблокирован, ввиду отсутствия онлайн более 30 дней')
#                 send_mail(
#                     subject='Блокировка',
#                     message=f'Пользователь с email: {user.email} был заблокирован, ввиду отсутствия онлайн более 30 дней',
#                     from_email=settings.EMAIL_HOST_USER,
#                     recipient_list=[user.email]
#                 )


@shared_task
def check_active_users():
    user = User.objects.filter(last_login__lt=timezone.now() - timezone.timedelta(minutes=1)).update(is_active=False)
    if user:
        print(f'Пользователь с email: {user.email} был заблокирован, ввиду отсутствия онлайн более 30 дней')
        send_mail(
            subject='Блокировка',
            message=f'Пользователь с email: {user.email} был заблокирован, ввиду отсутствия онлайн более 30 дней',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
