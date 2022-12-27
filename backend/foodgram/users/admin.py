from django.contrib import admin

from .models import CustomUser, Follow


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'role')
    search_fields = ('name',)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'author')
    search_fields = ('name',)
