from django.views.generic import ListView
from app_exemplo.models import ListaDeReproducao


class ListasDeReproducao(ListView):
	"""
	# template_name = 'blog/todos-artigos.html'
	# context_object_name = 'listas_de_reproducao'
	# queryset = ListaDeReproducao.objects.all()
	# paginate_by = 4

	def get_context_data(self, **kwargs):
		context = super(ListasDeReproducao, self).get_context_data(**kwargs)
		print context
		return context

	 {
	 	'paginator': None,
	 	'page_obj': None,
	 	'is_paginated': False,
	 	'object_list':
	 		[<ListaDeReproducao: Animiais>,
	 		<ListaDeReproducao: Clicks>,
	 		<ListaDeReproducao: Armas disparando>,
	 		<ListaDeReproducao: Sons de armas (GERAL)>],
	 	'listadereproducao_list':
	 		[<ListaDeReproducao: Animiais>,
	 		<ListaDeReproducao: Clicks>,
	 		<ListaDeReproducao: Armas disparando>,
	 		<ListaDeReproducao: Sons de armas (GERAL)>]
	 }
	"""
	model = ListaDeReproducao