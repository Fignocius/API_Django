from rest_framework import serializers
from .models import *


class SetorSerializer(serializers.ModelSerializer):
    funcionarios = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Setor
        fields = ['cod_setor', 'nome','funcionarios']


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields =['matricula', 'nome', 'tipo', 'senha', 'setor']


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'quantidade']


class ChamadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chamado
        fields =['funcionario', 'descricao']