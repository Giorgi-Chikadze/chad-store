from django.urls import path, include
from .views import  CategoryImageViewSet, CategoryListView

from rest_framework_nested import routers
from rest_framework.routers import SimpleRouter, DefaultRouter


router = routers.DefaultRouter()
router.register('categories', CategoryListView)
# router.register('category_detail', CategoryDetailView)

categories_router = routers.NestedDefaultRouter(
    router,
    'categories',
    lookup = 'category',
)

categories_router.register('images', CategoryImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(categories_router.urls)),
]


