from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from users.models import User
from users.tasks import check_active_users


class CheckActiveUsersTest(TestCase):
    ''' Тестирование задачи по блокировке пользователей.
     Для теста использовались секунды
     '''

    def setUp(self):
        # Создание тестовых пользователей
        self.user1 = User.objects.create(email='user1@example.com', password='password123')
        self.user1.last_login = timezone.now() - timedelta(seconds=31)
        self.user1.is_active = True
        self.user1.save()

        self.user2 = User.objects.create(email='user2@example.com', password='password123')
        self.user2.last_login = timezone.now() - timedelta(seconds=29)
        self.user2.is_active = True
        self.user2.save()

    def test_check_active_users(self):
        # Выполнение задачи
        check_active_users()

        # Обновление объектов из базы данных
        self.user1.refresh_from_db()
        self.user2.refresh_from_db()

        # Проверка изменения статуса
        self.assertFalse(self.user1.is_active, "User1 should be inactive")
        self.assertTrue(self.user2.is_active, "User2 should still be active")

