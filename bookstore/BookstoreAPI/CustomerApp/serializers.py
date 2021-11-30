from rest_framework import serializers
from CustomerApp.models import Book

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ['id', 'book_name', 'amount', 'pic_url', 'price']