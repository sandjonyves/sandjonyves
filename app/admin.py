from django.contrib import admin

from app.models import cart, Product,Order

# Register your models here.

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(cart)
