from django.db import models

class Verduras(models.Model):
    nome = models.CharField(max_length=100)
    preco_por_quilo = models.DecimalField(max_digits=6, decimal_places=2)
    estoque = models.IntegerField()

class Frutas(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    quantidade_disponivel = models.IntegerField()

class Entrega(models.Model):
    nome_cliente = models.CharField(max_length=255)
    endereco_entrega = models.TextField()
    data_entrega = models.DateTimeField()
    pagamento = models.OneToOneField('Pagamento', on_delete=models.CASCADE, related_name='entrega')

class Pagamento(models.Model):
    metodo_pagamento = models.CharField(max_length=50)
    valor_total = models.DecimalField(max_digits=8, decimal_places=2)

class Item(models.Model):
    entrega = models.ForeignKey(Entrega, on_delete=models.CASCADE, related_name="itens")
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=6, decimal_places=2)
