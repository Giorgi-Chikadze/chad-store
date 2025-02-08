from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from products.models import Product, Review, Cart, ProductTag, FavoriteProduct
from products.serializers import ProductSerializer, ReviewSerializer, CartSerializer, ProductTagSerializer, FavoriteProductSerializer


@api_view(['GET', 'POST'])
def product_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        product_list = []
        
        for product in products:
            product_data = {
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'currency': product.currency,
                'quantity': product.quantity
            }
            product_list.append(product_data)

        return Response({'products': product_list})
    elif request.method == "POST":
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            new_product = Product.objects.create(
                name=data.get('name'),
                description=data.get('description'),
                price=data.get('price'),
                currency=data.get('currency', 'GEL'), 
                quantity = data.get('quantity')
            )
            return Response({'id': new_product.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def review_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        review_list = []
        
        for review in reviews:
            review_data = {
                'id': review.id,
                'product_id': review.product.id,
                'content': review.content,
                'rating': review.rating
            }
            review_list.append(review_data)
        
        return Response({'reviews': review_list})

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data, context={"request":request})
        if serializer.is_valid():
            review = serializer.save()
            return Response(
                {'id': review.id, 'message': 'Review created successfully!'},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST'])
def cart_view(request):
    if request.method == 'GET':
        cart_products = Cart.objects.all()
        serializer = CartSerializer(cart_products, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CartSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"Product added to the cart"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)




@api_view(["GET","POST"])
def product_tag_view(request):
    if request.method == "GET":
        tags = ProductTag.objects.all()
        serializer = ProductTagSerializer(tags, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ProductTagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Tag added sucesfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
        
            

@api_view(["GET", "POST"])
def favorite_product_view(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)
        
        fav_products = FavoriteProduct.objects.all()
        serializer = FavoriteProductSerializer(fav_products, many = True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = FavoriteProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Product has been added to favorites"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            
            



