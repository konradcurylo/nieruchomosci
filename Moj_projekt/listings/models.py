from django.db import models
from datetime import datetime
from realtors.models import Agenci
# Create your models here.
class Oferty(models.Model):
    agent = models.ForeignKey(Agenci, on_delete = models.DO_NOTHING)
    tytul = models.CharField(max_length=200)
    adres = models.CharField(max_length=200)
    miasto = models.CharField(max_length=100)
    wojewodztwo = models.CharField(max_length=100)
    kodpocztowy = models.CharField(max_length=20)
    opis = models.TextField(blank=True)
    cena = models.IntegerField()
    sypialnie = models.IntegerField()
    lazienki = models.IntegerField()
    garaz = models.IntegerField(default=0)
    pow_domu = models.IntegerField()
    pow_dzialki = models.DecimalField(max_digits=5, decimal_places=1,blank=True)
    zdjecie_glowne = models.ImageField(upload_to='photos/%Y/%m/%d/')
    zdjecie_1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    zdjecie_2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    zdjecie_3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    zdjecie_4 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    zdjecie_5 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    zdjecie_6 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    czy_opublikowane = models.BooleanField(default=True)
    data_oferty = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.tytul
