from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import ClienteError, ServicioError, ReservaError, guardar_log


def ejecutar_operacion(numero, nombre, funcion):
    print(f"\\nOPERACION {numero}: {nombre}")

    try:
        funcion()
    except (ClienteError, ServicioError, ReservaError) as error:
        print("Error controlado:", error)
        guardar_log(f"Error controlado en operacion {numero}: {error}")
    except Exception as error:
        print("Error inesperado:", error)
        guardar_log(f"Error inesperado en operacion {numero}: {error}")
    else:
        print("Operacion realizada correctamente.")
    finally:
        print("Fin de la operacion.")


def main():
    print("======================================")
    print(" SISTEMA DE GESTION - SOFTWARE FJ")
    print("======================================")

    # Datos iniciales para realizar las pruebas.
    cliente1 = Cliente("Leidy Linares", "123456")
    cliente2 = Cliente("Carlos Perez", "654321")

    sala = ReservaSala("Sala principal", 3)
    equipo = AlquilerEquipo("Computador portatil", 2)
    asesoria = AsesoriaEspecializada("Asesoria de Python", 2)

    reserva1 = Reserva(cliente1, sala)

    # 1. Mostrar un cliente registrado.
    ejecutar_operacion(
        1, "Mostrar informacion del primer cliente",
        lambda: print(cliente1.mostrar_informacion())
    )

    # 2. Mostrar otro cliente registrado.
    ejecutar_operacion(
        2, "Mostrar informacion del segundo cliente",
        lambda: print(cliente2.mostrar_informacion())
    )

    # 3. Intentar registrar un cliente con nombre vacio.
    ejecutar_operacion(
        3, "Registrar un cliente con datos incorrectos",
        lambda: Cliente("", "123456")
    )

    # 4. Calcular el costo de una sala.
    ejecutar_operacion(
        4, "Calcular costo de reserva de sala",
        lambda: print("Costo:", f"${sala.calcular_costo():,.0f}")
    )

    # 5. Calcular el costo del alquiler de un equipo.
    ejecutar_operacion(
        5, "Calcular costo de alquiler de equipo",
        lambda: print("Costo:", f"${equipo.calcular_costo():,.0f}")
    )

    # 6. Calcular el costo de una asesoria.
    ejecutar_operacion(
        6, "Calcular costo de asesoria especializada",
        lambda: print("Costo:", f"${asesoria.calcular_costo():,.0f}")
    )

    # 7. Intentar calcular un servicio con cantidad negativa.
    ejecutar_operacion(
        7, "Calcular un servicio con cantidad incorrecta",
        lambda: sala.calcular_costo(-2)
    )

    # 8. Confirmar una reserva correctamente.
    ejecutar_operacion(
        8, "Confirmar una reserva",
        lambda: print("Total:", f"${reserva1.confirmar():,.0f}")
    )

    # 9. Intentar confirmar otra vez una reserva ya confirmada.
    ejecutar_operacion(
        9, "Confirmar por segunda vez la misma reserva",
        lambda: reserva1.confirmar()
    )

    # 10. Cancelar la reserva.
    ejecutar_operacion(
        10, "Cancelar la reserva",
        lambda: reserva1.cancelar()
    )

    # 11. Intentar crear una reserva con un servicio incorrecto.
    ejecutar_operacion(
        11, "Crear una reserva con un servicio no valido",
        lambda: Reserva(cliente1, "Servicio inexistente")
    )

    print("\\n========== RESUMEN DE LA RESERVA ==========")
    reserva1.mostrar_reserva()
    print("\\nLos eventos y errores quedaron guardados en la carpeta logs.")


if __name__ == "__main__":
    main()
