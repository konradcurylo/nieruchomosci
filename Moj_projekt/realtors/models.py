from django.db import models
from datetime import datetime
# Create your models here.

class Agenci(models.Model):
    nazwa = models.CharField(max_length=200)
    zdjecie = models.ImageField(upload_to='photos/%Y/%m/%d/')
    opis = models.TextField(blank=True)
    telefon = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    czy_sprzedawcam = models.BooleanField(default=False)
    data_zatrudnienia = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.nazwa
