# coding: utf-8
from django.views.generic import ListView
from app_exemplo.models import ListaDeReproducao


class ListasDeReproducao(ListView):
	"""
	Você pode usar o atributo "template_name" para informar a
	localização do template personalizado que você quer utilizar.

	Caso não queira informar, que é o que eu fiz aqui, por padrão
	o Django tentará encontrar um template com um nome neste padrão:
	'NomeDoModel_TipoDeView.html'. Como o nosso model é o
	'ListaDeReproducao' e nossa view é uma ListView ele buscará por:
	'listadereproducao_list.html'. Você pode conferir em:
	app_exemplo/templates/app_exemplo/

	Para informar a localização do template com o nome personalizado
	basta fazer como na linha comentada abaixo.
	"""
	# template_name = 'app_exemplo/lista_de_reproducao.html'

	"""
	Uma ListView, obviamente, precisa de dados para serem listados.

	Se estes dados estão vindo de algum model, nós precisamos informar
	o model que queremos extrair esta lista de objetos.

	Em nosso caso o model é o 'ListaDeReproducao'.
	"""
	model = ListaDeReproducao

	"""
	Um outro atributo que pode substituir o model é o queryset.

	Com ele é possível passar a lita de objetos a serem listados.
	A vantagem é que você já pode personalizar a recuperação desses
	dados, informando por exemplo um .filter(), .order(), entre outros
	métodos disponíveis no model.
	"""
	# queryset = ListaDeReproducao.objects.all()