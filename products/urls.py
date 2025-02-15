from django.urls import path
from products.views import product_view, review_view,CartViewSet,TagViewSet, FavoriteProductViewSet

urlpatterns = [
    path('products/', product_view, name="products"),
    path('reviews/', review_view, name="reviews"),
    path('cart', CartViewSet.as_view(), name="cart"),
    path('tags', TagViewSet.as_view(), name='tag'),
    path('favorites', FavoriteProductViewSet.as_view(), name='favorites' ),
    path('favorites/<int:pk>', FavoriteProductViewSet.as_view(), name='favorites' )
]