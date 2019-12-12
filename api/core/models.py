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


PRIORIDADES = (('ALTA', 'Alta'), ('MEDIA', 'Media'), ('BAIXA', 'Baixa'))


class TipoServico(models.Model):
    nome = models.CharField(max_length=50, primary_key=True)
    prioridade = models.CharField(max_length=20, choices=PRIORIDADES, default='BAIXA')


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
    tipoServico = models.ForeignKey(
        TipoServico,
        on_delete=models.CASCADE,
        related_name='chamados',
        to_field='nome',
        blank=True,
        null=True
    )


class Resolve(models.Model):
    chamado = models.ForeignKey(
    Chamado,
        on_delete=models.CASCADE,
        related_name='resolvido'
    )
    funcionario = models.ForeignKey(
        Funcionario,
        on_delete=models.CASCADE,
        related_name='resolvido'
    )
    descricao = models.TextField(blank=False, null=False)
    data_resolucao = models.DateTimeField()
    data_vinculo = models.DateTimeField()


class Usados(models.Model):
    chamado = models.ManyToManyField(
        Chamado,
        related_name='produtos'
    )
    produtos = models.ManyToManyField(
        Produto,
        related_name='produtos'
    )
    quantidade = models.IntegerField(default=1)