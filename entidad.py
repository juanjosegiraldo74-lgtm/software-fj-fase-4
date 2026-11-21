from abc import ABC, abstractmethod


class Entidad(ABC):
    """Clase base para las entidades del sistema."""

    def __init__(self, identificacion):
        self.identificacion = identificacion

    @abstractmethod
    def mostrar_informacion(self):
        pass
