from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name