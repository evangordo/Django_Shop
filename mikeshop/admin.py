from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(Order)
admin.site.register(BasketItems)
admin.site.register(Category)