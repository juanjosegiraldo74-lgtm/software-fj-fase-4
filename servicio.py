from abc import abstractmethod
from entidad import Entidad
from excepciones import ServicioError, guardar_log


class Servicio(Entidad):
    def __init__(self, identificacion, nombre, cantidad):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ServicioError("El servicio debe tener un nombre.")

        if not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise ServicioError("La cantidad o duracion debe ser mayor que cero.")

        super().__init__(identificacion)
        self.nombre = nombre.strip()
        self.cantidad = cantidad
        self.disponible = True

    @abstractmethod
    def calcular_costo(self, cantidad=None, descuento=0, impuesto=0.19):
        pass

    def validar_calculo(self, cantidad, descuento, impuesto):
        if not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise ServicioError("La cantidad debe ser mayor que cero.")
        if not isinstance(descuento, (int, float)) or descuento < 0 or descuento > 100:
            raise ServicioError("El descuento debe estar entre 0 y 100.")
        if not isinstance(impuesto, (int, float)) or impuesto < 0:
            raise ServicioError("El impuesto no puede ser negativo.")

    def calcular_total(self, cantidad, precio):
        total = cantidad * precio
        return total - (total * self._descuento / 100) + (
        (total - (total * self._descuento / 100)) * self._impuesto
    )
    def mostrar_informacion(self):
        return f"Servicio: {self.nombre} | Cantidad: {self.cantidad}"


class ReservaSala(Servicio):
    def __init__(self, nombre, horas):
        super().__init__("S01", nombre, horas)

    def calcular_costo(self, cantidad=None, descuento=0, impuesto=0.19):
        if cantidad is None:
            cantidad = self.cantidad
        self.validar_calculo(cantidad, descuento, impuesto)
        total = cantidad * 50000
        total = total - (total * descuento / 100)
        total = total + (total * impuesto)
        guardar_log("Se calculo el costo de reserva de sala.")
        return total


class AlquilerEquipo(Servicio):
    def __init__(self, nombre, dias):
        super().__init__("E01", nombre, dias)

    def calcular_costo(self, cantidad=None, descuento=0, impuesto=0.19):
        if cantidad is None:
            cantidad = self.cantidad
        self.validar_calculo(cantidad, descuento, impuesto)
        total = cantidad * 30000
        total = total - (total * descuento / 100)
        total = total + (total * impuesto)
        guardar_log("Se calculo el costo de alquiler de equipo.")
        return total


class AsesoriaEspecializada(Servicio):
    def __init__(self, nombre, horas):
        super().__init__("A01", nombre, horas)

    def calcular_costo(self, cantidad=None, descuento=0, impuesto=0.19):
        if cantidad is None:
            cantidad = self.cantidad
        self.validar_calculo(cantidad, descuento, impuesto)
        total = cantidad * 80000
        total = total - (total * descuento / 100)
        total = total + (total * impuesto)
        guardar_log("Se calculo el costo de asesoria especializada.")
        return total
