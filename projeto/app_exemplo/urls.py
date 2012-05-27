from django.conf.urls.defaults import patterns, url
from views.list_and_detail import ListasDeReproducao, DetalhesListasDeReproducao
from views.json import ListasDeReproducaoJson

urlpatterns = patterns('',
    # list_and_detail.py
    url(r'^listas-de-reproducao/', ListasDeReproducao.as_view(), name='app_exemplo-listview'),
    url(r'^lista-de-reproducao/(?P<pk>\d+)/$', DetalhesListasDeReproducao.as_view(), name='app_exemplo-detailview'),
    # json.py
    url(r'^json/listas-de-reproducao/', ListasDeReproducaoJson.as_view(), name='app_exemplo-json-listview'),
)
