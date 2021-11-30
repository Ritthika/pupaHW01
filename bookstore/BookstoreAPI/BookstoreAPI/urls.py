from django.contrib import admin
from django.urls import include,path
from CustomerApp import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]