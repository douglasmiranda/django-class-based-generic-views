from django.conf.urls.defaults import patterns, url
from views.lista_de_reproducao import ListasDeReproducao

urlpatterns = patterns('',
	url(r'^listas-de-reproducao/', ListasDeReproducao.as_view(), name='app_exemplo-listview-exemplo-1'),
)