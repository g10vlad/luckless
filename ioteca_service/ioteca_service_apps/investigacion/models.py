from __future__ import unicode_literals

from django.db import models

# Create your models here.

class InvestigacionModelo(models.Model):

    editorial = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    isbn = models.IntegerField()
    medio_publicacion = models.CharField(max_length=100)
    num_paginas = models.IntegerField()
    tipo_publicacion = models.CharField(max_length=100)
    titulo_publicacion = models.CharField(max_length=100)


    class Meta:
        verbose_name = "Investigación"
        verbose_name_plural = "Investigaciones"

    def __str__(self):
        return self.editorial
