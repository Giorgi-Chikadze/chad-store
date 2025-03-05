from django.contrib import admin
from products.models import (
    Cart, Product, ProductTag,
    Review, FavoriteProduct, ProductImage, CartItem
)


admin.site.register(Cart)
admin.site.register(ProductTag)
admin.site.register(Review)
admin.site.register(FavoriteProduct)
admin.site.register(ProductImage)
admin.site.register(CartItem)

class ProductImageInLine(admin.StackedInline):
    model = ProductImage
    extra = 0 

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    inlines = [ProductImageInLine]
