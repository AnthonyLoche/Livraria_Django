from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from livraria.models import Autor
from livraria.serializers import AutorSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor
    serializer_class = AutorSerializer
