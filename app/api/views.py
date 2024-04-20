from rest_framework import viewsets
from rest_framework.response import Response
from app.api.service import FrutasService, VerdurasService
from app.models import Verduras, Frutas, Entrega, Pagamento, Item
from app.api.serializers import VerdurasSerializer, FrutasSerializer, EntregaSerializer, PagamentoSerializer, ItemSerializer
from app.api.interfaces import IFrutasService, IVerdurasService

class BaseCreateViewSet(viewsets.ModelViewSet):
    serializer_class = None
    queryset = None

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return response

class BaseUpdateViewSet(viewsets.ModelViewSet):
    serializer_class = None
    queryset = None

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return response

class BaseRetrieveViewSet(viewsets.ModelViewSet):
    serializer_class = None
    queryset = None

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return response

class BaseDestroyViewSet(viewsets.ModelViewSet):
    serializer_class = None
    queryset = None

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return response

class VerdurasViewSet(BaseCreateViewSet):
    queryset = Verduras.objects.all()
    serializer_class = VerdurasSerializer
    verduras_service = VerdurasService()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        metrica = self.verduras_service.calcular_metrica()
        return Response({'message': 'Verdura criada com sucesso!', 'metrica': metrica})

class FrutasViewSet(BaseUpdateViewSet):
    queryset = Frutas.objects.all()
    serializer_class = FrutasSerializer
    frutas_service = FrutasService()

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        self.frutas_service.atualizar_quantidade()
        return response

class EntregaViewSet(BaseRetrieveViewSet):
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        serialized_data = EntregaSerializer(response.data, many=True).data
        for entrega_info in serialized_data:
            entrega_info['nome_cliente'] = entrega_info.pop('nome_cliente')
            entrega_info['endereco'] = entrega_info.pop('endereco_entrega')
        return Response(serialized_data)

class PagamentoViewSet(BaseDestroyViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return Response({'message': 'Pagamento excluído com sucesso!'})

class ItemViewSet(BaseRetrieveViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        item_data = response.data
        item_data['quantidade'] *= 2
        return Response(item_data)
