from django.urls import path
from products.views import (ProductViewSet,
                            ReviewViewSet,
                            CartViewSet,TagViewSet,
                            FavoriteProductViewSet,
                            ProductImageViewSet)

urlpatterns = [
    path('products/', ProductViewSet.as_view({
        'get':'list',
        'post':'create',
    }), name="products"),

    path('products/<int:pk>', ProductViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'patch':'partial_update',
        'delete':'destroy',
    }), name="product"),
    # path('reviews/',ReviewViewSet.as_view(), name="reviews"),
    path('products/<int:product_id>/reviews/',ReviewViewSet.as_view(), name="reviews"),
    path('cart/', CartViewSet.as_view(), name="cart"),
    path('tags/', TagViewSet.as_view(), name='tag'),
    path('favorite_products/', FavoriteProductViewSet.as_view({'get':'list', 'post':'create'}), name='favorites' ),
    path('favorite_products/<int:pk>', FavoriteProductViewSet.as_view({'get':'retrieve','delete':'destroy'}), name='favorites' ),
    path('products/<int:product_id>/images/', ProductImageViewSet.as_view(), name='product-images'),
    path('products/<int:product_id>/images/<int:pk>', ProductImageViewSet.as_view(), name='product-image'),
    
]