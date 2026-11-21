from cliente import Cliente
from servicio import Servicio
from excepciones import ReservaError, guardar_log


class Reserva:
    def __init__(self, cliente, servicio):
        if not isinstance(cliente, Cliente):
            raise ReservaError("La reserva necesita un cliente valido.")

        if not isinstance(servicio, Servicio):
            raise ReservaError("La reserva necesita un servicio valido.")

        if not servicio.disponible:
            raise ReservaError("El servicio no se encuentra disponible.")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = servicio.cantidad
        self.estado = "Pendiente"
        self.costo = 0
        guardar_log("Se creo una reserva en estado pendiente.")

    def confirmar(self, descuento=0):
        try:
            if self.estado != "Pendiente":
                raise ReservaError("Solo se pueden confirmar reservas pendientes.")

            if not self.servicio.disponible:
                raise ReservaError("El servicio ya no esta disponible.")

            self.costo = self.servicio.calcular_costo(descuento=descuento)
            self.estado = "Confirmada"
            self.servicio.disponible = False
            guardar_log("Reserva confirmada correctamente.")
            return self.costo

        except ReservaError as error:
            guardar_log(f"Error al confirmar reserva: {error}")
            raise

        except Exception as error:
            guardar_log(f"Error inesperado al confirmar reserva: {error}")
            raise ReservaError("No fue posible confirmar la reserva.") from error

    def cancelar(self):
        try:
            if self.estado == "Cancelada":
                raise ReservaError("La reserva ya esta cancelada.")

            if self.estado == "Confirmada":
                self.servicio.disponible = True

            self.estado = "Cancelada"
            guardar_log("Reserva cancelada correctamente.")

        except ReservaError as error:
            guardar_log(f"Error al cancelar reserva: {error}")
            raise

    def mostrar_reserva(self):
        print("Cliente:", self.cliente.obtener_nombre())
        print("Servicio:", self.servicio.nombre)
        print("Duracion:", self.duracion)
        print("Estado:", self.estado)
        print("Costo:", f"${self.costo:,.0f}")
