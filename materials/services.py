# import json
# from datetime import datetime, timedelta
# from django_celery_beat.models import PeriodicTask, IntervalSchedule
#
#
# def send_mail_4_hours(*args, **kwargs):
#     """
#     Отправляет сообщение об обновлении курса каждые 4 часа
#     """
#     schedule, created = IntervalSchedule.objects.get_or_create(
#         every=10,
#         period=IntervalSchedule.SECONDS,
#     )
#     PeriodicTask.objects.create(
#         interval=schedule,  # we created this above.
#         name='Update course',  # simply describes this periodic task.
#         task='materials.tasks.sending_update_course',  # name of task.
#         args=json.dumps(['arg1', 'arg2']),
#         kwargs=json.dumps({
#             'be_careful': True,
#         }),
#         expires=datetime.utcnow() + timedelta(seconds=30)
#     )
