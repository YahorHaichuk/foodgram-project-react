from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from rest_framework_simplejwt.tokens import AccessToken


from recipes.models import Recipe
from users.models import CustomUser, Follow


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.SlugField(
        max_length=150,
        allow_blank=False
    )
    email = serializers.EmailField()

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email'
        )


class CustomUserCreateSerializer(serializers.ModelSerializer):
    """ Сериализаторор для модели User."""

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'password'
        )

        validators = [
            UniqueTogetherValidator(
                queryset=CustomUser.objects.all(),
                fields=('username', 'email'),
                message='Имя пользователя или email уже используются'
            )
        ]

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)


class UserMeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
        )


class GetTokenSerializer(serializers.Serializer):
    username_field = get_user_model().USERNAME_FIELD
    token_class = AccessToken


class CustomUserSerializer(serializers.ModelSerializer):
    """ Сериализаторор для модели User."""
    is_subscribed = serializers.SerializerMethodField()

    def get_is_subscribed(self, author):
        user = self.context.get('request', None).user
        if user.is_authenticated:
            return Follow.objects.filter(user=user, author=author).exists()
        return False

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'is_subscribed'
        )

