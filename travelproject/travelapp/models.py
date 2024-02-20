from django.db import models

class Place2(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    imag=models.ImageField(upload_to="pics")

    def __str__(self):
        return self.name
