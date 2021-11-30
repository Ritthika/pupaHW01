from rest_framework import viewsets
from CustomerApp.serializers import BookSerializer
from CustomerApp.models import Book

class UserViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer