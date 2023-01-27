from django.db import models

# Create your models here.

class Contacts(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.CharField(max_length=500)
    def __str__(self) -> str:
        return self.email
    