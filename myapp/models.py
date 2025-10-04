#Individu gender 

from django.db import models

class Individu(models.Model):
    GENDER_CHOICES = [
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    ]

    nama_depan = models.CharField(max_length=100)
    nama_belakang = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(blank=True, null=True)
    kota = models.CharField(max_length=100, blank=True, null=True)
    tahun_engagement = models.PositiveIntegerField(blank=True, null=True)
    consent_publish = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nama_depan} {self.nama_belakang}"
# 
# lalu dimigrasikan 
#
#python manage.py makemigrations
#python manage.py migrate
#