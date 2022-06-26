from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

# @admin.register()
class UserClass(UserAdmin):
    # fieldsets = ((None, {'fields': }))
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'is_staff', 'is_Provider')
        }),
        ('Advanced options', {
            # 'classes': ('collapse',),
            'fields': ()
        }),
    )

    list_display = ('username', 'email', 'is_staff', 'is_Provider')

    
# 'enable_comments', 'registration_required', 'template_name'
admin.site.register(User, UserClass)
admin.site.register(Product)
admin.site.register(ProductReview)
admin.site.register(Order)
admin.site.register(Category)