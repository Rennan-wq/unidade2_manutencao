from abc import ABC, abstractmethod

class IVerdurasService(ABC):
    @abstractmethod
    def calcular_metrica(self):
        pass

class IFrutasService(ABC):
    @abstractmethod
    def atualizar_quantidade(self):
        pass
