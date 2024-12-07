from django.shortcuts import render
from django.views.generic import TemplateView
from market.models import Gear
# Create your views here.

class IndexView(TemplateView):
    template_name="index.html"
    
    def get_context_data(self, **kwargs):
        # Obtenha o contexto padrão
        context = super().get_context_data(**kwargs)
        # Adicione variáveis personalizadas ao contexto
        context['breadcrumb'] = ["Home", "Loja"]
        return context