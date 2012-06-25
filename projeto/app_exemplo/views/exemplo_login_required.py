from django.views.generic import TemplateView
from core.views import LoginRequiredMixin


class ViewQueExigeAutenticacao(LoginRequiredMixin, TemplateView):
    """
    O artigo que faz o uso desse código pode ser conferido em:
    http://douglasmiranda.com/artigo/login-required-mixin-django-class-based-generic-views-iv/

    Utilizando o recurso de herança multipla do Python nós adicionamos
    o Mixin 'LoginRequiredMixin' que criamos em core.views.

    Lembrando que a ordem importa, para mais informações busque saber de
    'herança múltipla em python'. Veja mais em core.views.
    """
    template_name = 'template_para_pagina_login_required.html'
