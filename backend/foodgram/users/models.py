from django.contrib.auth.models import AbstractUser
from django.db import models

from foodgram.settings import ROLES_CHOICES


class CustomUser(AbstractUser):

    username = models.CharField(max_length=150, unique=True)

    first_name = models.CharField(max_length=150)

    last_name = models.CharField(max_length=150)

    email = models.EmailField(max_length=254)

    password = models.CharField(max_length=150)

    role = models.CharField(
        max_length=32,
        choices=ROLES_CHOICES,
        default='user',
        verbose_name='роль пользователя'
    )

    def __str__(self):
        return str(self.username)


class Follow(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='follower'
    )

    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='following',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_follow'
            )
        ]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ['-id']

    def __str__(self):
        return f'{self.user}{self.author}'
