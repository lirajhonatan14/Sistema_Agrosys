from django.db import models

class ResponsaveisTecnicos(models.Model):
    NOME = models.CharField(max_length=50)
    CNPJ = models.CharField(max_length=50)
    NUM_REGISTRO = models.ForeignKey("impressao.ProdutorRural", on_delete=models.CASCADE, blank=True, null=True)

class ProdutorRural(models.Model):
    NOME = models.CharField(max_length=100)
    NUM_REGISTRO = models.AutoField(primary_key=True)
    PROPRIEDADE = models.ForeignKey("impressao.ResponsaveisTecnicos", on_delete=models.CASCADE, blank=True, null=True)
    
class Propriedade(models.Model):
    DESCRICAO = models.CharField(max_length=100)
    CNPJ = models.CharField(max_length=100, primary_key=True)
    LOCAL =models.ForeignKey("impressao.Diagnostico", on_delete=models.CASCADE, blank=True, null=True)
    LATITUDE = models.CharField(max_length=100)
    LONGITUDE = models.CharField(max_length=100)
    
class Diagnostico(models.Model):
    NUM = models.AutoField(primary_key=True)
    CULTURA = models.CharField(max_length=100)
    PRODUTO_COMERCIAL = models.CharField(max_length=100)
    ALVO = models.CharField(max_length=100)
    AREA_TRATAR = models.CharField(max_length=100)
    VOLUME_CALDA = models.CharField(max_length=100)
    INTERVALO_SEGURANCA = models.CharField(max_length=100)
    MODALIDADE_APLICACAO = models.CharField(max_length=100)
    EQUIPAMENTO_APLICACAO = models.CharField(max_length=100)
    QUANTIDADE_ADQUIRIR = models.CharField(max_length=100)
    NUMERO_APLICACOES = models.CharField(max_length=100)
    EPOCA_APLICACAO = models.CharField(max_length=100)
    