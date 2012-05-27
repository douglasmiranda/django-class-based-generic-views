from django.conf.urls.defaults import patterns, url
from views.list_and_detail import ListasDeReproducao, DetalhesListasDeReproducao

urlpatterns = patterns('',
    url(r'^listas-de-reproducao/', ListasDeReproducao.as_view(), name='app_exemplo-listview-exemplo-1'),
    url(r'^lista-de-reproducao/(?P<pk>\d+)/$', DetalhesListasDeReproducao.as_view(), name='app_exemplo-detailview-exemplo-1'),
)
