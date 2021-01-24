from django.contrib import admin

# Register your models here.
from userlogin.models import Cuisine,Customer,Restaurant,OrderItems,Order,Item

admin.site.register(Customer)
admin.site.register(Cuisine)
admin.site.register(Restaurant)
admin.site.register(Order)

admin.site.register(Item)
admin.site.register(OrderItems)