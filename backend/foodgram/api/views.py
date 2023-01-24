from urllib import request

from api import serializers
from api.filters import Filter, NameSearchFilter
from api.permissions import IsAuthorOrReadOnly
from api.serializers import (CreateRecipeSerialzer, IngredientsSerializer,
                             RecipeSerialzer, ShopingCardSerializer,
                             TagsSerializer)
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from recipes.models import (Favorite, IngredientAmount, Ingredients, Recipe,
                            Tags, UserShopCart)
from recipes.utilits import make_send_file
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import mixins


class TagsViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """ Представление модели Tags """
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    pagination_class = None


class IngredientVievSet(viewsets.ReadOnlyModelViewSet):
    """ Представление модели Ingredient """
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
    filter_backends = (NameSearchFilter,)
    search_fields = ('^name',)
    pagination_class = None


class RecipeVievSet(viewsets.ModelViewSet):
    """ Представление модели Recipe """
    queryset = Recipe.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = Filter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            serializer = RecipeSerialzer
            #serializer.is_valid(raise_exception=True)
            return RecipeSerialzer
        #serializer = CreateRecipeSerialzer
        #serializer.is_valid(raise_exception=True)
        return CreateRecipeSerialzer


    # serializer = self.get_serializer_class(data=data)
    # serializer.is_valid(raise_exception=True)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    @action(
        detail=False,
        methods=['get'],
        permission_classes=[IsAuthenticated],
        name='download_shopping_cart')
    def download_shopping_cart(self, request):
        """ Скачать файл со списком ингредиентов """
        ingredient = IngredientAmount.objects.filter(
            recipe__usershopcart__user=request.user
        ).values(
            'ingredient__name',
            'ingredient__measurement_unit'
        ).annotate(amount_sum=Sum('amount'))

        file_data = make_send_file(ingredient)
        return HttpResponse(
            file_data,
            content_type='text/plain',
            status=status.HTTP_200_OK
        )

    def add_recipe(self, request, pk, model):
        """Вспомогательная функция для добавления рецепта в
        shopping_cart или favorite."""
        user = request.user
        recipe = get_object_or_404(Recipe, pk=pk)
        object = model.objects.filter(
            user=user,
            recipe=recipe
        )
        if request.method == 'POST':
            model.objects.get_or_create(
                user=user,
                recipe=recipe
            )
            serializer = ShopingCardSerializer(recipe)
            serializer.validate(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        if request.method == 'DELETE':
            object.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    @action(
        detail=True,
        methods=['post', 'delete'],
        permission_classes=[IsAuthenticated],
        name='shopping_cart'
    )
    def shopping_cart(self, request, pk=None):
        """ Обработка запросов на добавление в корзину """

        return self.add_recipe(request, pk, UserShopCart)

    @action(
        detail=True,
        methods=['post', 'delete'],
        permission_classes=[IsAuthenticated],
        name='favorite'
    )
    def favorite(self, request, pk=None):
        """ Представление запросов по url .../favorite/"""

        return self.add_recipe(request, pk, Favorite)
