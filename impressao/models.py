from django.db import models

class ResponsaveisTecnicos(models.Model):
    NOME = models.CharField(max_length=50)
    CNPJ = models.CharField(max_length=50)
    NOME_REGISTRO = models.CharField(max_length=50)