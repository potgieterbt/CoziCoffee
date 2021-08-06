from django.contrib import admin

from .models import Cart, Product, Reviews
# Register your models here.

admin.site.register(Cart)
admin.site.register(Reviews)
admin.site.register(Product)