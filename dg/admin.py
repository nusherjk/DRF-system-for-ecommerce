from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(ProductReview)
admin.site.register(Order)
admin.site.register(Category)