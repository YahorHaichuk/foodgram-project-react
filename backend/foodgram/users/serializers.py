from api.serializers import ShopingCardSerializer
from django.contrib.auth.hashers import make_password
from recipes.models import Recipe
from rest_framework import serializers
from users.models import Follow, User


class UserSerializer(serializers.ModelSerializer):
    """ Сериализаторор для модели User."""
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    def create(self, validated_data):
        password = validated_data['password']
        validated_data['password'] = make_password(password)
        return super().create(validated_data)

    class Meta:
        model = User
        fields = [
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'password',
        ]


class RegistrationSerializer(serializers.ModelSerializer):
    """ Сериализация регистрации пользователя. """

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = [
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'password',
            'token',
            'is_subscribed'
        ]

    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError(
                'email не соответствует User'
            )
        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class SetPasswordSerializer(serializers.ModelSerializer):
    """ Сериализатор эндпойнта SetPassword. """
    new_password = serializers.CharField(
        required=True,
        max_length=50,
        min_length=8,
        write_only=True
    )
    current_password = serializers.CharField(
        required=True,
        max_length=50,
        min_length=4,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['new_password', 'current_password']

    def validate(self, attrs):
        if attrs['new_password'] == attrs['current_password']:
            raise serializers.ValidationError(
                'новый и старый пароли совпадают'
            )
        return super().validate(attrs)


class UserSubscribtionsSerializer(serializers.ModelSerializer):
    """ Сериализатор эндпойнта UserSubscribtions. """

    recipes = serializers.SerializerMethodField()
    recipes_count = serializers.SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'is_subscribed',
            'recipes',
            'recipes_count'
        ]

    def get_recipes(self, obj):
        recipes = Recipe.objects.filter(author_id=obj.id)
        serializer = ShopingCardSerializer(recipes, many=True)
        return serializer.data

    def get_recipes_count(self, obj):
        recipes = Recipe.objects.filter(author_id=obj.id)
        return recipes.count()

    def get_is_subscribed(self, obj):
        return Follow.objects.filter(
            user=self.context.get('user'),
            author=obj
        ).exists()

    def update(self, instance, validated_data):
        author = User.objects.get(username=self.context.get('author'))
        instance.email = author.email
        return instance


class FollowSerializer(serializers.ModelSerializer):
    """ Сериализатор модели Follow. """

    result = UserSubscribtionsSerializer()

    class Meta:
        model = Follow
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    """ Сериализатор модели Users List и Create. """

    class Meta:
        model = User
        fields = [
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'is_subscribed',
        ]
