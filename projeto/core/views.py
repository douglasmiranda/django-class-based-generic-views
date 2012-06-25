# -*- coding: utf-8 -*-
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    """
    O artigo que faz o uso desse código pode ser conferido em:
    http://douglasmiranda.com/artigo/login-required-mixin-django-class-based-generic-views-iv/

    Criei este Mixin para utilizar em views em que somente usuários
    autenticados possam acessar. Para saber mais sobre Mixins:
    https://docs.djangoproject.com/en/1.3/topics/class-based-views/#more-than-just-html

    Este Mixin modificará o comportamento do método 'dispatch' que existe
    em outras 'class based generic views', ou seja, antes de enviar a resposta
    que a view deveria retornar ele verifica se o usuário atual está autenticado.

    Isto é feito através do decorator 'login_required'.

    Se não estiver autenticado você será redirecionado para algo como:
    /accounts/login/?next=/app-exemplo/exemplo-login-required/

    PS: isso vai depender do seu settings.LOGIN_URL, por padrão ele tem o valor
    '/accounts/login/', sinta-se à vontade para alterar e ver como muda.

    Daí você cria seu formulário de login que deve estar mapeado de acordo com seu
    settings.LOGIN_URL e pronto, terá uma view que se você não estiver logado, será
    redirecionado para o formulário de login com sucesso.
    """
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)
