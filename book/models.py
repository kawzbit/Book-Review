from distutils.command import upload
from django.db import models
from django.contrib.auth.models import User 

class Book(models.Model):
    title = models.CharField(max_length= 150)
    description = models.CharField(max_length= 250)
    image = models.ImageField(upload_to= "books/images/")
    
    url = models.URLField(blank= True)


class Review(models.Models):
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)

    def __str__(self):
        return self.text

        

  