from django.urls import path, include
from products.views import (ProductViewSet,
                            ReviewViewSet,
                            CartViewSet,TagViewSet,
                            FavoriteProductViewSet,
                            ProductImageViewSet, CartItemViewSet)

from rest_framework_nested import routers
from rest_framework.routers import SimpleRouter, DefaultRouter


router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('favorite_products',FavoriteProductViewSet)
router.register('cart', CartViewSet)
router.register('tags', TagViewSet)


products_router = routers.NestedDefaultRouter(

    router,
    'products',
    lookup = 'product'
)

router.register('cart_items', CartItemViewSet, basename='cart-items')

products_router.register('images', ProductImageViewSet)
products_router.register('reviews', ReviewViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include(products_router.urls)),
]



