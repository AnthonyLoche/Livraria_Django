from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from livraria.models import Categoria, Livro, Editora, Autor
from livraria.serializers import CategoriaSerializer

from livraria.serializers import (
    LivroSerializer,
    LivroListSerializer,
    LivroDetailSerializer,
    EditoraSerializer,
    AutorSerializer,
)


# Create your views here.
class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


def get_serializer_class(self):
    if self.action == "list":
        return LivroListSerializer
    elif self.action == "retrieve":
        return LivroDetailSerializer
    return LivroSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
