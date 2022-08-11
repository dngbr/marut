from django.db import models

# Create your models here.
class Email(models.Model):
    nume = models.CharField(max_length=30)
    telefon = models.CharField(max_length=20)
    email = models.EmailField()
    mesaj = models.CharField(max_length=1000)