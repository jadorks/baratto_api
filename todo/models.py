from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
# class Users(models.Model):
#     Fname = models.CharField(max_length=50)
#     Lname = models.CharField(max_length=50)
#     Email = models.CharField(max_length=50)
#     DOB = models.DateField()
#     GENDER = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#     )
#     gender = models.CharField(max_length=1, choices=GENDER)
#     Phonenumber = models.CharField(max_length=15)
#     Address = models.CharField(max_length=50)
#     OtherSocialMedia = models.CharField(max_length=50)


class Category(models.Model):
    title = models.CharField(max_length = 100, null = False, blank = False)

    def __str__(self):
        return self.title


class Products(models.Model):
    user = models.ForeignKey(User, related_name='products', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, default=5, on_delete=models.SET_DEFAULT)
    title = models.CharField(max_length = 100)
    price = models.FloatField()
    description = models.CharField(max_length = 100)
    image = models.ImageField(default='default_product.jpg', upload_to='product_pics')

    def __str__(self):
        return self.title 

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
