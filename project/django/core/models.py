from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    descrepion = models.TextField()
    price = models.IntegerField()
    image_P = models.ImageField()


    def __str__ (self):
        return self.name
