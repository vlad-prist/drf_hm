from django.urls import path
from users.apps import UsersConfig
from users.views import PaymentListAPIView, UserViewSet
from rest_framework.routers import DefaultRouter


app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('payment/', PaymentListAPIView.as_view(), name='payment-list'),
] + router.urls
