#Django Class-Based Generic Views (Projeto em andamento)

No Django 1.3, as generic views deixaram de ser definidas como funções e passaram a ser classes.

Assim podemos definir atributos, comportamentos e características especiais em nossas views de modo mais elegante, reaproveitável e inteligível.

#Qual o objetivo deste repositório?

Apresentar e exemplificar o uso das diversas classes pré-definidas, ([Class-Based Generic Views](https://docs.djangoproject.com/en/1.3/topics/class-based-views/)), disponíveis no Django para criação de views de um modo bem legal.

##Apresentação

A apresentação em texto será feita por meio de artigos em meu blog, vou publicando e listando os links que já houverem aqui abaixo.

Lista de artigos:

* [ListView](http://douglasmiranda.com/artigo/listview-django-class-based-generic-views-i/) - aprenda diminuir repetição de código em suas views de listagem com ListView

* [DetailView](http://douglasmiranda.com/artigo/detailview-django-class-based-generic-views-ii/) - view que exibe os detalhes de um objeto pelo slug ou pk pode ser bem fácil de se fazer

* [Json View](http://douglasmiranda.com/artigo/json-view-django-class-based-generic-views-iii/) - reaproveitando um ListView e serializando a saída, transformando-a em Json

* [LoginRequiredMixin](http://douglasmiranda.com/artigo/login-required-mixin-django-class-based-generic-views-iv/) - vamos ver como trabalhar com as CBV + o decorator login_required de forma reaproveitável, através de um Mixin

##Exemplos

Os exemplos estarão neste projeto dentro da app "[app_exemplo](https://github.com/douglasmiranda/django-class-based-generic-views/tree/master/projeto/app_exemplo)" no módulo "[views](https://github.com/douglasmiranda/django-class-based-generic-views/tree/master/projeto/app_exemplo/views)".

#Sobre as licenças

Os arquivos de áudio dentro de [media/audios](https://github.com/douglasmiranda/django-class-based-generic-views/tree/master/projeto/media/audios) estão licenciados pela atribuição (Creative Commons Attribution 3.0) e podem ser encontradas em soundbible.com