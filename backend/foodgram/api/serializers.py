from django.core.validators import MinValueValidator
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from recipes.models import Tag, Ingredient, Recipe


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = 'id', 'name', 'color', 'slug'


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = '__all__'


class IngredientInRecipeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='ingredient.id')
    name = serializers.CharField(
        read_only=True,
        source='ingredient.name'
    )

    measurement_unit = serializers.CharField(
        read_only=True,
        source='ingredient.measurement_unit'
    )

    amount = serializers.IntegerField()




# class RecipeSerializer(serializers.ModelSerializer):
#     tags = TagField(
#         slug_field='id', queryset=Tag.objects.all(), many=True
#     )
#     ingredients = IngredientInRecipeSerializer(
#         source='ingredient_in_recipe',
#         read_only=True, many=True
#     )
#
#     class Meta:
#         model = Recipe
#         exclude = ('image',)



