from django.db import models
from datetime import datetime
# Create your models here.
class Kontakt(models.Model):
    oferta = models.CharField(max_length=200)
    oferta_id = models.IntegerField()
    nazwa = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    telefon = models.CharField(max_length=100)
    wiadomosc = models.TextField(blank=True)
    data_kontaktu = models.DateTimeField(default=datetime.now, blank=True)
    uzytkownik_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.nazwa

