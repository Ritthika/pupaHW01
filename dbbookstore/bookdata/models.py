from django.db import models

# Create your models here.
class book(models.Model):
    bookname = models.CharField(max_length=30)
    amount = models.IntegerField()
    pic_url = models.CharField(max_length=90)
    price = models.IntegerField()
    def str(self):
        return self.bookname