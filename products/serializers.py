from rest_framework import serializers
from products.models import Review, Product, Cart, ProductTag, FavoriteProduct


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    currency = serializers.ChoiceField(choices=['GEL', 'USD', 'EUR'])
    quantity = serializers.IntegerField()


class ReviewSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(write_only=True)
    content = serializers.CharField()
    rating = serializers.IntegerField()

    def validate_product_id(self, value):
        try:
            Product.objects.get(id=value)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Invalid product_id. Product does not exist.")
        return value

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value

    def create(self, validated_data):
        product = Product.objects.get(id=validated_data['product_id'])
        user = self.context['request'].user

        review = Review.objects.create(
            product=product,
            user=user,
            content=validated_data['content'],
            rating=validated_data['rating'],
        )
        return review
    


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        exclude = ['created_at', 'updated_at']


    def validate_product_id(self, value):
        if not Product.objects.filter(id=value).exists():
            raise serializers.ValidationError("Invalid product_id. Product does not exist.")
        return value
    #ამოწმებს პროდუქტი არსებობს თუ არა მონაცემთა ბაზაში


class ProductTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTag
        exclude = ['created_at', 'updated_at']



class FavoriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteProduct
        exclude = ['created_at', 'updated_at']

    
    def validate_product_id(self, value):
        if  not Product.objects.filter(id=value).exists():
            raise serializers.ValidationError("Invalid product_id. Product does not exist.")
        return value
    
    #ამოწმებს პროდუქტი არსებობს თუ არა მონაცემთა ბაზაში