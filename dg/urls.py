"""doog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cgitb import lookup
from django.contrib import admin
from django.urls import path, include
from .views import UserViwset,  index, Home,  CategoryViwset, ProductViewset, Orderviewset, ProfileViewset, Webhookviewset
from rest_framework_nested import routers

router = routers.DefaultRouter()

#register = router.register(r'register')
user = router.register(r'users', UserViwset)
product = router.register(r'products', ProductViewset)

category = router.register(r'categories', CategoryViwset)

order = router.register(r'order', Orderviewset)

profile = router.register(r'profile', ProfileViewset, basename='profile')


profile_nest = routers.NestedSimpleRouter(router, r'profile', lookup="profile")
profile_nest.register(r'self', ProfileViewset)
### IMPORTANT MESSENGER WEBHOOK
#webhook = router.register(r'webhook', Webhookviewset, basename='webhook')

urlpatterns = [
    path('', index, name="stand"),
    path('home/', Home.as_view(), name="landing"),
    path('webhook/', Webhookviewset.as_view(), name="webhook"),

    path('api/', include(router.urls)),
    path('api/', include(profile_nest.urls))


]
