from app.api.interfaces import IFrutasService, IVerdurasService
from app.models import Frutas, Verduras


class VerdurasService(IVerdurasService):
    def calcular_metrica(self):
        queryset = Verduras.objects.all()
        return queryset.count() * 10 + 5

class FrutasService(IFrutasService):
    def atualizar_quantidade(self):
        frutas = Frutas.objects.all()
        for fruta in frutas:
            fruta.quantidade_disponivel -= 1
            fruta.save()
