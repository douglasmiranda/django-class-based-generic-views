# coding: utf-8
from django.views.generic import ListView, DetailView
from models import ListaDeReproducao


class ListasDeReproducao(ListView):
	"""
	ListasDeReproducao é a nossa class based generic view que herda de
	ListView que pode ser encontrada em: django/views/generic/list.py

	É bem simples utilizar a generic view ListView para listar objetos.
	Tanto que neste exemplo o código é basicamente este:

	class ListasDeReproducao(ListView):
		model = ListaDeReproducao

	O resto são as explicações e opções de personalização que você
	pode fazer com ListView.
	"""

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

	"""
	O 'context_object_name' é o nome da variável de contexto que estará
	disponível para você manipular em seu template, em nosso caso
	no 'listadereproducao_list.html'.

	Quando você não informa um nome personalizado, que foi o que fizemos,
	a variável vai se chamar 'object_list' que será uma lista de objetos.
	Ela também poderá ser chamada por um nome composto da seguinte maneira:
	NOME_DO_MODEL_list, em nosso caso "listadereproducao_list".

	Para representar visualmente, em nosso exemplo será algo como isto:
	{
		# OUTROS OBJETOS DE CONTEXTO,
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

	Podemos manipular, por exemplo, assim:
	<ul>
	{% for lista_de_reproducao in object_list %}
		<li>
			<p>{{ lista_de_reproducao.titulo }}</p>
			<p>{{ lista_de_reproducao.descricao }}</p>
		</li>
	{% endfor %}
	</ul>

	Então se quisermos que "object_list" vire, por exemplo, "listas_de_reproducao"
	faça como na linha comentada abaixo:
	"""
	# context_object_name = 'listas_de_reproducao'

	"""
	Sobre Objetos de contexto

	Se você quiser obter o 'context_object_name' ou o 'queryset', você poderia
	simplesmente usar dos métodos: "get_queryset, get_context_object_name" que podem
	ser encontrados, para melhor visualização, em django/views/generic/list.py.

	Caso queira fazer mais do que apenas obter, se quizer, em algum momento modificar,
	tratar casos específicos ou mesmo deixar mais explícito os objetos de contexto que
	estarão disponíveis em seu template, você pode utilizar o "get_context_data"

	Por exemplo:
	"""
	# def get_context_data(self, **kwargs):
	# 	context = super(ListasDeReproducao, self).get_context_data(**kwargs)
	# 	# Aqui você fará inclusão, alteração ou exclusão de contextos como desejar
	# 	context['ultima_lista_de_reproducao'] = ListaDeReproducao.objects.latest()
	# 	return context

	"""
	Se quiser saber em tempo de execução quais os objetos de contexto
	que estão sendo passados para seu template, você pode definir este método
	e mandar imprimir em console para que você possa ver assim que acessar a url.

	def get_context_data(self, **kwargs):
		context = super(ListasDeReproducao, self).get_context_data(**kwargs)
		# imprimindo no console o que há no dicionário de contextos
		print context

		return context

	Você verá algo desse tipo:
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

	"""
	Toda lista de objetos tende a aumentar, para isto precisamos controlar a
	exibição desses objetos em tela com a paginação.

	Para isto basta fornecer ao atributo 'paginate_by' a quantidade de objetos
	que você quer que seja listada por página. Por exemplo:
	paginate_by = 15
	Listará 15 objetos por página.

	Se quiser ver em nosso exemplo isto em uso experimente descomentar a linha
	abaixo, e serão exibidos 2 objetos por página.
	"""
	# paginate_by = 4
	"""
	No template, em um exemplo bem simples de páginação você poderia fazer algo como:
	{% if is_paginated %}
	<div class="paginacao">
		<span class="paginacao-links">
			{% if page_obj.has_previous %}
			<a href="?page={{ page_obj.previous_page_number }}">anterior</a>
			{% endif %}
			<span class="page-current">
				P&aacute;gina {{ page_obj.number }} de {{ page_obj.paginator.num_pages }}.
			</span>
			{% if page_obj.has_next %}
			<a href="?page={{ page_obj.next_page_number }}">pr&oacute;xima</a>
			{% endif %}
		</span>
	</div>
	{% endif %}
	Que terá como resultado algo como: "Página 1 de 2. próxima"
	"""

	"""
	Sobre paginação

	A criatividade é bastante aplicada neste ponto, então você além de explorar as opções
	de personalização do template pode alterar conforme quiser o limite desta paginação
	inclusive em tempo de execução com o "paginate_queryset". Nas linhas comentadas abaixo
	exemplifico isto, tentando obter da url o parâmetro "limite" para ser usado como paginação,
	caso não exista eu uso a paginação padrão.
	"""
	# def paginate_queryset(self, queryset, page_size):
	# 	page_size = self.request.GET.get('limite', page_size)
	# 	paginate_queryset = super(ListasDeReproducao, self).paginate_queryset(queryset, page_size)
	# 	return paginate_queryset


class DetalhesListasDeReproducao(DetailView):
	"""
	DetalhesListasDeReproducao é a nossa class based generic view que
	herda de DetailView que pode ser encontrada em: django/views/generic/detail.py

	É bem simples utilizar a generic view DetailView para exibir informações de um
	objeto ou mais, baseado no "slug" ou na chave primária "pk". Geralmente precisamos
	disso quando, à partir, de um lista de objetos temos de exibir mais informações
	de um objeto especificamente ou mesmo gerar o permalink dele. Como por exemplo a
	página interna de uma notícia. Em nosso caso queremos mais detalhes sobre a lista
	de reprodução para visualizar mais informações e os áudios contidos na lista.

	O código deste exemplo é basicamente este:

	class DetalhesListasDeReproducao(DetailView):
		model = ListaDeReproducao

	O resto são as explicações e opções de personalização que você
	pode fazer com DetailView, que há alguns atributos semelhantes no ListView.
	"""

	"""
	A personalização deste atributo é feita da mesma forma que no ListView,
	veja mais na view ListasDeReproducao.

	O que muda é que se você não definir, automaticamente ela vai buscar o seguinte
	template: "listadereproducao_detail.html" que é a soma do nome do Model + o tipo
	de view: Model: ListaDeReproducao e View: DetailView
	"""
	# template_name = 'app_exemplo/lista_de_reproducao_detalhes.html'

	"""
	Como na ListView: ListasDeReproducao, aqui também é necessário informar o model
	do qual extrairemos as informações desejadas.
	"""
	model = ListaDeReproducao

	"""
	Como no ListView aqui você pode escolher entre fornecer o model e/ou o queryset.

	Mas manipular queryset no DetailView seria para casos bem específicos, pois filtragem
	e outras coisas que podem ser feitas com o queryset são geralmente feitas já na hora
	de listar, no caso, em uma ListView e no DetailView o objeto selecionado já é o definitivo
	e queremos somente extrair informações dele. Para fazer maiores personalizações no objeto
	de contexto gerado pela DetailView é necessário manipular os objetos de contexto com
	o método "get_context_data".
	"""
	# queryset = ListaDeReproducao.objects.all()

	"""
	Se você não der um nome para o objeto de contexto para manipular nos templates o nome dele
	será o nome do model, neste caso "listadereproducao", em lower case mesmo. Ou poderá ser acessado
	também como "object".

	Se você visualizar as variáveis de contexto que estão sendo passadas para seu template verá
	algo assim:

	{
		'listadereproducao': <ListaDeReproducao: Armas disparando>,
		'object': <ListaDeReproducao: Armas disparando>
	}

	Você pode personalizá-lo como na linha comentada abaixo:
	"""
	# context_object_name = 'lista_de_reproducao'

	"""
	Sobre Objetos de contexto

	O objeto de contexto na DetailView é diferente da ListView, pois no conteúdo extraído do
	Model não temos uma lista e sim um objeto, já que a intenção é listar os detalhes de um
	objeto específico.

	Não quer dizer que você não possa definir o método "get_context_data" e personalizar os
	objetos de contexto:
	"""
	# def get_context_data(self, **kwargs):
	# 	context = super(DetalhesListasDeReproducao, self).get_context_data(**kwargs)
	# 	# Aqui você fará inclusão, alteração ou exclusão de contextos como desejar
	# 	context['listas_de_outras_coisas'] = OutroModel.objects.all()
	# 	return context