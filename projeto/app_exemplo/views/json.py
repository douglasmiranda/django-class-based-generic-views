# coding: utf-8
from django.http import HttpResponse
from django.core import serializers
from list_and_detail import ListasDeReproducao


class ListasDeReproducaoJson(ListasDeReproducao):
    context_object_name = 'listas_de_reproducao'

    def get(self, request, *args, **kwargs):
        # self.object_list = self.get_queryset()
        # context = self.get_context_data(object_list=self.object_list)
        data = serializers.serialize("json", self.get_queryset())
        return HttpResponse(data, content_type='application/json')
