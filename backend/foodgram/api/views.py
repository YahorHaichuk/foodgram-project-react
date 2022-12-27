from .mixins import ListPostDelPatch, GetPostMixin
from .serializers import TagSerializer, IngredientSerializer

from rest_framework import viewsets

from recipes.models import Tag, Ingredient, Recipe


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


# class RecipeViewSet(GetPostMixin):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer

