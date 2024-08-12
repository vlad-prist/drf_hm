from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from users.models import Payment, User
from users.permissions import IsOwner #, IsUserOwner
from users.serializers import PaymentSerializer, UserSerializer #, UserDetailSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

    # def get_serializer_class(self):
    #     if self.action in ['retrieve', 'list']:
    #         return UserDetailSerializer
    #     if self.action in ['update', 'partial_update']:
    #         return UserSerializer

    # def get_permissions(self):
    #     if self.action in ['list',]:
    #         self.permission_classes = [AllowAny]
    #     else:
    #         self.permission_classes = [IsUserOwner]
    #     return super().get_permissions()


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('lesson_paid', 'course_paid', 'payment_type',)
    ordering_fields = ('date_payment',)
