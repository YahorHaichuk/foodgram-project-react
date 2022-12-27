from django.core import validators
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models



from foodgram.settings import COLOR_CHOISES


class Tag(models.Model):
    name = models.CharField(max_length=256, blank=False,
                            verbose_name='Название тега')

    color = models.CharField(max_length=20, blank=False, choices=COLOR_CHOISES,
                             verbose_name='Цвет')

    slug = models.SlugField(max_length=20, unique=True,
                            verbose_name='slug тега')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

        def __str__(self):
            return f'{self.name}'


class Ingredient(models.Model):
    name = models.CharField(max_length=256, blank=False,
                            verbose_name='Название Рецепта')

    measurement_unit = models.CharField(max_length=10, blank=False,
                                        verbose_name='Единица измерения')

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'

    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):
    author = models.CharField(max_length=256, blank=False,
                              verbose_name='Автор')

    name = models.CharField(max_length=256, blank=False,
                            verbose_name='Название Рецепта')

    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='posts/',
        blank=True
    )

    text = models.TextField(verbose_name='Текст рецепта')

    tag = models.ManyToManyField(Tag,
                                 verbose_name='Теги',
                                 related_name='recipes')

    cooking_time = models.PositiveIntegerField(
        verbose_name='Время приготовления',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class IngredientAmount(models.Model):
    ingregient = models.ForeignKey(
        Ingredient,
        default='1',
        on_delete=models.CASCADE,
        verbose_name='ингредиент',
        related_name='ingredient_in_recipe'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='ингредиенты',
        related_name='ingredient_in_recipe',
    )

    amount = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )
