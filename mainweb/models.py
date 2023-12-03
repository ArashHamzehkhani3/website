from django.db import models

# Create your models here.



class Book(models.Model):
    name = models.CharField(max_length=255)
    phonenumber=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    meal=models.TextField()
    capacity=models.TextField()








class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
