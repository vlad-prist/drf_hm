from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='apitest@apitest.com')
        self.course = Course.objects.create(title='Test Course', description='Test Course', owner=self.user)
        self.lesson = Lesson.objects.create(title='Test Lesson', description='Test Lesson', course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)


    def test_lesson_retrieve(self):
        url = reverse("materials:lesson_detail", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('title'), self.lesson.title
        )


    def test_lesson_create(self):
        # url = reverse("materials:lesson_list")
        data = {
            'title': 'Test Lesson 2',
            'description': 'Test Lesson 2',
            'course': self.course.pk,
            'owner': self.user.pk,
        }
        response = self.client.post('/lesson/', data=data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(Lesson.objects.all().count(), 2)


    def test_lesson_update(self):
        url = reverse("materials:lesson_detail", args=(self.lesson.pk,))
        data = {
            'title': 'Test Lesson',
        }
        response = self.client.get(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('title'), 'Test Lesson'
        )



