from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    Description = models.TextField()
    category = models.CharField(max_length=256)
    subcategory1 = models.CharField(max_length=265)
    subcategory2 = models.CharField(max_length=256)
    subcategory3 = models.CharField(max_length=256)
    prd_img = models.ImageField(upload_to='product_images/')


