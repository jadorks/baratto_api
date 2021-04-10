from django.db import models

# Create your models here.
class Users(models.Model):
    Fname = models.CharField(max_length=50)
    Lname = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    DOB = models.DateField()
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER)
    Phonenumber = models.CharField(max_length=15)
    Address = models.CharField(max_length=50)
    OtherSocialMedia = models.CharField(max_length=50)
    

class Products(models.Model):
    UserID = models.ForeignKey(Users, on_delete=models.CASCADE)
    Name = models.CharField(max_length = 100)
    Price = models.IntegerField()
    Description = models.CharField(max_length = 100)
    

    def __str___(self):
        return self.title 
