# Уроки и материалы DRF
Проект по отработке Django REST framework

В данном проекте используются различные методы и подходы DRF


## Выполнено
- [x] Созданы два приложения: users, materials.
- [x] Определены модели для каждого приложения: users - User, Payment; materials - Course, Lesson.
- [x] В главные настройки прописаны приложения 'rest_framework', 'django_filters'.
- [x] Установлен пакет зависимостей для приложений выше (pip install djangorestframework| pip install django-filter)
- [x] Для моделей описаны Viewsets и Generic-классы.
- [x] Добавлены дополнительные атрибуты в сериализаторы, с использованием [SerializerMethodField()](https://nodejs.org/)
- [x] Выведены фикстуры (файлы json) для всех сущностей каждой модели.
- [x] В Контроллере для класса Списка платежей настроена фильтрация (по полям "тип оплаты", "оплаченный урок/курс"
и сортировка по дате платежа.
- [x] Реализован CRUD для пользователей, в том числе регистрацию пользователей 
(реализация контроллера Viewset осуществлена по тьюториулу https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/)
- [x] В урлах использована JWT-авторизация и закрыли каждый эндпоинт авторизацией (прописано в настройках settings.py).
- [x] Добавлены права Модератора с установкой ограничейний на (добавление, удаление)
- [x] Создана валидация (для уроков и курсов) на проверку ссылки на отсутствие в материалах ссылок на сторонние ресурсы, кроме youtube.com.
- [x] Создана новая модель "Подписка", настроен контроллер и прописаны урлыю.
- Для создание подписки вручную через Shell: импортируем каждую модель: Subscription, User, Course. -> Создаем: Subscription.objects.create(user=User.objects.get(pk=3), course=Course.objects.get(pk=2))
- [x] Приложение Materials протестировано.
- [x] Для работы с документацией проекта установлена библиотека [drf-yasg](https://nodejs.org/) (установлен дополнительно setuptools)
- [x] Реализовано выставление счета на оплату через Stripe (https://dashboard.stripe.com/test/payments/pi_3PmwbZLf1o8Zu43R2J0RSoP5)
- pip install forex-python
- pip install strive
- [x] Реализован функционал подписки на обновление курсов
- [x] С помощью celery-beat реализована проверка пользователей по дате последнего входа
- [x] Приложение залито в Docker
 

## Использование Docker

Для работы с Docker на компьютере должен быть установлен Docker и docker-compose 

Инструкции по установке [Docker Desktop on Windows](https://docs.docker.com/desktop/install/windows-install/)

Дополнительный справочный ресурс [Docker Hub](https://hub.docker.com/)

Создание и последующий запуск контейнера командой docker-compose up -d --build

