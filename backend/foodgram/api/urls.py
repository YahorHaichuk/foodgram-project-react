from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import CustomUserViewSet, GetTokenView
from .views import TagViewSet, IngredientViewSet

app_name = 'api'

router = DefaultRouter()

router.register(r'tags', TagViewSet, basename='tags')
router.register(r'ingredients', IngredientViewSet, basename='ingredients')
router.register(r'users', CustomUserViewSet, basename='users')
#router.register(r'recipes', RecipeViewSet, basename='recipes')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

]


