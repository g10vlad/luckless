from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import ReconocimientosMdl, RegimenDocente
from ioteca_service_apps.utils.permissions import ModelPermission

from ioteca_service_apps.utils.pagination import ModelPagination

# Create your views here.

class ReconocimientoMdlSerializer(serializers.ModelSerializer):
#    tipo_categoria = serializers.SerializerMethodField()

    class Meta:
        model = ReconocimientosMdl

#    def get_tipo_categoria(self, obj):
#        return obj.get_tipo_categoria_display()

class ReconocimientoMdlViewSet(ModelPagination, viewsets.ModelViewSet):
    queryset = ReconocimientosMdl.objects.all()
    serializer_class = ReconocimientoMdlSerializer
#    permission_classes = [ModelPermission, ]

class RegimenDocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegimenDocente

class RegimenDocenteViewSet(ModelPagination, viewsets.ModelViewSet):
    queryset = RegimenDocente.objects.all()
    serializer_class = RegimenDocenteSerializer
