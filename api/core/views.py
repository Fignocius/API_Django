from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class SetorViewSet(viewsets.ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer


class FuncionariosViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer


class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class ChamadosViewSet(viewsets.ModelViewSet):
    queryset = Chamado.objects.all()
    serializer_class = ChamadoSerializer


class TipoServicosViewSet(viewsets.ModelViewSet):
    queryset = TipoServico.objects.all()
    serializer_class = TipoServicoSerializer


class ResolveViewSet(viewsets.ModelViewSet):
    queryset = Resolve.objects.all()
    serializer_class = ResolveSerializer


class UsadosViewSet(viewsets.ModelViewSet):
    queryset = Usados.objects.all()
    serializer_class = UsadosSerializer
