from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.generics import ListAPIView, ListCreateAPIView

from products.models import Product, Review, Cart, ProductImage, ProductTag, FavoriteProduct
from products.serializers import ProductSerializer, ProductImageSerializer, ReviewSerializer, CartSerializer, ProductTagSerializer, FavoriteProductSerializer



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]



class ReviewViewSet(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(product_id=self.kwargs['product_id'])
    


class CartViewSet(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset






class TagViewSet(ListAPIView):
    queryset = ProductTag.objects.all()
    serializer_class = ProductTagSerializer
    permission_classes = [IsAuthenticated]

        
            

class FavoriteProductViewSet(ModelViewSet):
    queryset = FavoriteProduct.objects.all()
    serializer_class = FavoriteProductSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'delete']


    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset


class ProductImageViewSet(CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, GenericAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(product__id=self.kwargs['product_id'])
    
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            return self.retrieve(self, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

            



