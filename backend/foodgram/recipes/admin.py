from django.contrib import admin

from .models import Tag, Ingredient, IngredientAmount, Recipe


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'slug')
    search_fields = ('name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('name',)

class IngredientAmountInLine(admin.TabularInline):
    model = IngredientAmount
    extra = 0

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'cooking_time',
                    'text')
    search_fields = ('name',)
    inlines = [IngredientAmountInLine]

