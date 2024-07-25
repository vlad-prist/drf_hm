from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='название курса')
    image = models.ImageField(upload_to="course/images", verbose_name="картинка (превью)", **NULLABLE)
    description = models.TextField(verbose_name='описание курса')

    lessons = models.ManyToManyField('Lesson', related_name='related_lesson')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name='название урока')
    description = models.TextField(verbose_name='описание урока')
    image = models.ImageField(upload_to="lesson/images", verbose_name="картинка (превью)", **NULLABLE)
    link = models.URLField(max_length=300, verbose_name="ссылка на видео", **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
