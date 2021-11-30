from django.contrib import admin
from django.urls import include,path
from CustomerApp import views
from rest_framework import routers


urlpatterns = [
    path('', include('CustomerApp.urls')),
    path('admin/', admin.site.urls),
]