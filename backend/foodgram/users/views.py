from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import CustomUser, Follow
from .serializers import SignUpSerializer, CustomUserSerializer, \
    UserMeSerializer, GetTokenSerializer, CustomUserCreateSerializer
from rest_framework_simplejwt import views


from rest_framework import viewsets, mixins, status
from api.mixins import GetPostMixin, ListPostDel


class CustomUserViewSet(GetPostMixin):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    @action(
        detail=False,
        methods=['get'],
        permission_classes=[IsAuthenticated]
    )
    def me(self, request, pk=None):
        data = UserMeSerializer(request.user, many=False).data
        return Response(data, status=status.HTTP_200_OK)


class GetTokenView(views.TokenObtainSlidingView):
    """Обработчик получения токенов при регистрации."""
    serializer_class = GetTokenSerializer


class UsersViewSet(GetPostMixin):
    queryset = CustomUser.objects.all()
    #lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.validated_data['password'] = make_password(
            serializer.validated_data['password']
        )
        serializer.save()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CustomUserCreateSerializer
        return CustomUserSerializer


