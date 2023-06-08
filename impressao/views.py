from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ResponsaveisTecnicosForm, ProdutorRuralForm, PropriedadeForm, DiagnosticoForm

def formulario_impressao(request):
    if request.method == 'POST':
        form_resp = ResponsaveisTecnicosForm(request.POST)
        if form_resp.is_valid():
            instancia = form_resp.save(commit=False)
            
            instancia.NUM_REGISTRO = form_prop.NUM_REGISTRO
            instancia.save()
        form_prod = ProdutorRuralForm(request.POST)
        if form_prod.is_valid():
            instancia1 = form_prod.save(commit=False)
            
            instancia1.PROPRIEDADE = form_prop.CNPJ
            instancia1.save()
        form_prop = PropriedadeForm(request.POST)
        if form_prop.is_valid():
            instancia1 = form_prop.save(commit=False)
           
            instancia1.LOCAL = form_diag.id
            instancia1.save()
        form_diag = DiagnosticoForm(request.POST)
        form_resp.save()
        form_prod.save()
        form_prop.save()
        form_diag.save()
        messages.success(request, 'Formulario cadastrado com sucesso.')
        return redirect(' name')
    else:
        form_resp = ResponsaveisTecnicosForm()
        form_prod = ProdutorRuralForm()
        form_prop = PropriedadeForm()
        form_diag = DiagnosticoForm()
    return render(request, 'tela_formulario.html', {'form_resp':form_resp, 'form_prod':form_prod, 'form_prop':form_prop, 'form_diag': form_diag})
   
from django.views.generic import DetailView
from .models import ResponsaveisTecnicos, ProdutorRural, Propriedade, Diagnostico

class DetalhesView(DetailView):
    template_name = 'impressao.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Recuperando os objetos relacionados
        responsavel = ResponsaveisTecnicos.objects.get(pk=self.kwargs['pk'])
        produtor = ProdutorRural.objects.get(pk=self.kwargs['pk'])
        propriedade = Propriedade.objects.get(pk=self.kwargs['pk'])
        diagnostico = Diagnostico.objects.get(pk=self.kwargs['pk'])

        # Passando os objetos para o contexto do template
        context['responsavel'] = responsavel
        context['produtor'] = produtor
        context['propriedade'] = propriedade
        context['diagnostico'] = diagnostico

        return context
