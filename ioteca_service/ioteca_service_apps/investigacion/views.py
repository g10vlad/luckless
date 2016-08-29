from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import InvestigacionModelo
from ioteca_service_apps.utils.permissions import ModelPermission

from ioteca_service_apps.utils.pagination import ModelPagination


# Create your views here.

class InvestigacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvestigacionModelo

class InvestigacionViewSet(ModelPagination, viewsets.ModelViewSet):
    queryset = InvestigacionModelo.objects.all()
    serializer_class = InvestigacionSerializer
