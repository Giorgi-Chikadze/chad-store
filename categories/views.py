from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin

from categories.models import Category, CategoryImage
from .serializers import CategoryDetailSerializer, CategoryImageSerializer, CategorySerializer

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    

class CategoryDetailView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer

    

class CategoryImageViewSet(ListCreateAPIView):
    queryset = CategoryImage.objects.all()
    serializer_class = CategoryImageSerializer

    def get_queryset(self):
        cateogory_id = self.kwargs['category_id']

        return self.queryset.filter(category=cateogory_id)
    

    
