from django import forms
from django.shortcuts import render
from .models import ResponsaveisTecnicos, ProdutorRural, Propriedade, Diagnostico

class ResponsaveisTecnicosForm(forms.ModelForm):
    class Meta:
        model = ResponsaveisTecnicos
        fields = ['NOME', 'CNPJ','NUM_REGISTRO']
        widgets = {
        }

        
class ProdutorRuralForm(forms.ModelForm):
    class Meta:
        model = ProdutorRural
        fields = ['NOME','NUM_REGISTRO', 'PROPRIEDADE']
        widgets = {
        }
        
class PropriedadeForm(forms.ModelForm):
    class Meta:
        model = Propriedade
        fields = ['DESCRICAO', 'CNPJ','LOCAL', 'LATITUDE', 'LONGITUDE']
        widgets = {
        }
        
class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = ['CULTURA', 'PRODUTO_COMERCIAL','ALVO', 'AREA_TRATAR', 'VOLUME_CALDA', 'INTERVALO_SEGURANCA', 'MODALIDADE_APLICACAO', 'EQUIPAMENTO_APLICACAO', 'QUANTIDADE_ADQUIRIR', 'NUMERO_APLICACOES', 'EPOCA_APLICACAO']
        widgets = {
        }