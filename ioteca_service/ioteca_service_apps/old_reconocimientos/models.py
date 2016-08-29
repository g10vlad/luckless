from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ReconocimientosMdl(models.Model):

    DOCENTE_CATEGORIA=(
    ('AX', 'Auxiliar'),
    ('P', 'Principal'),
    ('AS', 'Asociado'),
    )

    institucion=models.CharField(max_length=100)
    reconocimiento=models.CharField(max_length=100)
    fecha=models.DateTimeField()
    lugar=models.CharField(max_length=100)
    fuente = models.CharField(max_length=100)
    #date_fin = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Reconocimiento Docente"
        verbose_name_plural = "Reconocimientos Docente"

    def __str__(self):
        return self.catedra

class RegimenDocente(models.Model):
    REGIMEN_DOCENTE=(
    ('DX', 'Dedicacion Exclusiva'),
    ('TC', 'Tiempo Completo'),
    ('TP', 'Tiempo Parcial'),
    ('PA', 'Pasantia'),
    ('PC', 'Practicante'),
    )
    tipo_regimen=models.CharField(max_length=2, choices=REGIMEN_DOCENTE)

    class Meta:
        verbose_name = "Regimen Docente"
        verbose_name_plural = "Regimen Docentes"

    def __str__(self):
        return u"%s" % (self.get_tipo_regimen_display())
