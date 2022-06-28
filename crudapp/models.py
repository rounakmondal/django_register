from django.db import models

# Create your models here.class
class students(models.Model):
    FirstName = models.CharField(max_length=50)
    LasttName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    Contact = models.BigIntegerField()


class ranjan(models.Model):
    FirstName = models.CharField(max_length=50)
    LasttName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    Contact = models.BigIntegerField()

class contactmee(models.Model):
    Name = models.CharField(max_length=50)
    EmailField = models.EmailField(max_length=50)
    Message = models.CharField(max_length=50)