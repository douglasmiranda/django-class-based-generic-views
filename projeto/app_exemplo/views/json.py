# coding: utf-8
from django.http import HttpResponse
from django.core import serializers
from list_and_detail import ListasDeReproducao


class ListasDeReproducaoJson(ListasDeReproducao):
    """
    ListasDeReproducaoJson é nossa view que reaproveita o que fizemos
    em app_exemplo.views.list_and_detail.ListasDeReproducao para
    transformarmos o retorno em JSON.

    Assim como podemos ver n o arquivo list_and_detail.py aqui também
    poderíamos alterar várias características e comportamentos da view
    por meio de seus atributos e métodos. (vide ListasDeReproducao,
    DetalhesListasDeReproducao de app_exemplo.views.list_and_detail)
    """
    context_object_name = 'listas_de_reproducao'

    def get(self, request, *args, **kwargs):
        """
        Poderíamos obter os objetos de contexto e alterá-los como desejarmos.
        # self.object_list = self.get_queryset()
        # context = self.get_context_data(object_list=self.object_list)
        Para criarmos um objeto personalizado a ser serializado no formato JSON.

        Mas o que gostaríamos de fazer neste exemplo simples é apenas obter o queryset
        de elementos já herdado de ListasDeReproducao e transformá-lo em nossa saída ideal.

        Assim na próxima linha eu utilizo um serializador do Django para isto.
        """
        data = serializers.serialize("json", self.get_queryset())
        """
        E, basicamente, agora eu apenas transformo o retorno da minha view
        em 'application/json'. O conteúdo desta resposta é o retorno de
        self.get_queryset() já serializado no formato JSON.

        Algo como:
        [
            {
                "pk":1,
                "model":"app_exemplo.listadereproducao",
                "fields":{
                    "modificado":"2010-03-13 12:12:45",
                    "audios":[
                        1,
                        2,
                        3
                    ],
                    "criado":"2010-01-26 15:25:26",
                    "titulo":"Animiais",
                    "slug":"Animais",
                    "descricao":"Alguns efeitos sonoros de animais."
                }
            },
            {
                "pk":2,
                "model":"app_exemplo.listadereproducao",
                "fields":{
                    "modificado":"2010-05-30 08:16:53",
                    "audios":[
                        4,
                        5,
                        6,
                        7
                    ],
                    "criado":"2010-01-05 14:12:28",
                    "titulo":"Clicks",
                    "slug":"clicks",
                    "descricao":"Efeitos sonoros de CLICKs."
                }
            },
            {
                "pk":3,
                "model":"app_exemplo.listadereproducao",
                "fields":{
                    "modificado":"2011-06-27 12:17:15",
                    "audios":[
                        8,
                        9
                    ],
                    "criado":"2011-05-27 12:17:15",
                    "titulo":"Armas disparando",
                    "slug":"armas-disparando",
                    "descricao":"Sons de armas disparando."
                }
            },
            {
                "pk":4,
                "model":"app_exemplo.listadereproducao",
                "fields":{
                    "modificado":"2012-01-27 12:21:10",
                    "audios":[
                        10,
                        11
                    ],
                    "criado":"2012-01-27 12:21:10",
                    "titulo":"Sons de armas (GERAL)",
                    "slug":"sons-de-armas-geral",
                    "descricao":"Sons de armas em geral. Recarregando, disparando e armas de grande porte. "
                }
            }

        ]

        Para um exemplo isto serve, mas talvez você realmente queira personalizar isto
        antes de transformá-lo em JSON. Por exemplo se você quer serializar um queryset
        de usuários, dependendo de como sua query foi composta, pode trazer o campo 'senha'
        e, talvez, você queira omití-lo deste retorno. Contudo creio que não será um problema
        uma vez que com self.get_queryset() você consegue manipular bem estes resultados, antes
        de serializá-los.

        PS: Não gosto de usar XML, porém, para transformar isto em um exemplo de retorno XML
        bastaria apenas substituir onde está 'json' por 'xml'. Assim:
        # serializers.serialize("xml", self.get_queryset())
        # return HttpResponse(data, content_type='application/xml')
        """
        return HttpResponse(data, content_type='application/json')
