from asyncio import AbstractServer
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_title = models.CharField(max_length=100)
    store_city = models.CharField(max_length=50)

    def __str__(self):
        return self.store_title


class Book(models.Model):
    book_in_store = models.ForeignKey(Store,on_delete=models.CASCADE,null=True,related_name='bookid')
    image = models.ImageField(upload_to="Post/imgs",null=True)
    book_title = models.CharField(max_length=100)
    book_author = models.CharField(max_length=50)
    book_stock= models.IntegerField(null=True)
    book_edition= models.IntegerField(null=True)
    def __str__(self):
        return self.book_title