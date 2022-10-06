from django.db import models
from django.db import models

# Create your models here.
class Dosen(models.Model):
    NIP = models.CharField(max_length=200)
    nama = models.CharField(max_length=200)
    tanggal_lahir = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    fakultas = models.CharField(max_length=200)
    prodi = models.CharField(max_length=200)
    alamat_rumah = models.CharField(max_length=200)
    foto = models.CharField(max_length=500, null=True)

# def __str__(self):pytho
#     return self.NIP

class Staff(models.Model):
    nama = models.CharField(max_length=200)
    NIP = models.CharField(max_length=200)
    tanggal_lahir = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    alamat_rumah = models.CharField(max_length=200)
    foto = models.CharField(max_length=500, null=True)

# def __str__(self):
#     return self.NIP

class Mahasiswa(models.Model):
    NIM = models.CharField(max_length=200)
    nama = models.CharField(max_length=200)
    tanggal_lahir = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    fakultas = models.CharField(max_length=200)
    prodi = models.CharField(max_length=200)
    foto = models.CharField(max_length=500, null=True)

# def __str__(self):
#     return self.NIP

