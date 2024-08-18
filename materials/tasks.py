from celery import shared_task
from django.core.mail import send_mail
from config import settings
from materials.models import Subscription, Course


@shared_task
def sending_update_course(course):
    course_updates = Subscription.objects.filter(course=course.id)
    for single_update in course_updates:
        send_mail(
            subject='Обновление материалов курса!',
            message=f'Вышло обновление материалов курса - {single_update.course.title}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[single_update.user.email]
        )
    print("Сообщение отправлено")


# @shared_task
# def sending_update_4_hours():
#     four_hours_ago = timezone.now() - timedelta(minutes=1)
#     course_updates = Course.objects.filter(last_update__gte=four_hours_ago)
#     for course in course_updates:
#         sending_update_course.delay(course)
