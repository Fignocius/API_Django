from django.db import models


class Setor(models.Model):
    cod_setor = models.CharField(max_length=15, primary_key= True, null=False)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.cod_setor


class Funcionario(models.Model):
    matricula= models.CharField(max_length=30, primary_key= True)
    nome= models.CharField(max_length=50)
    tipo= models.CharField(max_length=25)
    senha= models.CharField(max_length=30)
    setor= models.ForeignKey(
        Setor,
        on_delete=models.CASCADE,
        related_name='funcionarios',
        to_field='cod_setor',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.matricula


class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao= models.TextField(blank=True)
    quantidade= models.IntegerField(default= 0)

    def __str__(self):
        return self.nome


class TipoServico(models.Model):
    nome = models.CharField(max_length=50, primary_key=True)


class Chamado(models.Model):
    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.CASCADE,
        related_name='chamados',
        to_field='matricula',
        blank=True,
        null=True
    )
    descricao = models.TextField(null=False)