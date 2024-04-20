from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from livraria.models import Livro

from livraria.serializers import (
    LivroSerializer,
    LivroListSerializer,
    LivroDetailSerializer,
)

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["categoria__descricao", "editora__nome", "autor__nome", "compra__status"]
    search_fields = ["titulo", "autor", "editora", "categoria"]
    ordering_fields = ["titulo", "preco"]
    ordering = ["titulo"]


def get_serializer_class(self):
    if self.action == "list":
        return LivroListSerializer
    elif self.action == "retrieve":
        return LivroDetailSerializer
    return LivroSerializer

