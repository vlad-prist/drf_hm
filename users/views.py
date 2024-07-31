from rest_framework import generics, viewsets
from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()



class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('lesson_paid', 'course_paid', 'payment_type',)
    ordering_fields = ('date_payment',)
