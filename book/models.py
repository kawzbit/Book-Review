from distutils.command import upload
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length= 150)
    description = models.CharField(max_length= 250)
    image = models.ImageField(upload_to= "books/images/")
    
    url = models.URLField(blank= True)
