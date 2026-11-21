# Sistema Integral de Gestion de Clientes, Servicios y Reservas

**Proyecto:** Software FJ  
**Actividad:** Fase 4 - Manejo de excepciones en programacion orientada a objetos

## Descripcion

Este proyecto es un programa en Python para gestionar clientes, servicios y reservas de Software FJ. Permite registrar clientes, calcular el costo de diferentes servicios, crear reservas, confirmarlas y cancelarlas.

El programa trabaja con objetos y clases. No utiliza una base de datos. Los eventos y errores se guardan en un archivo de texto dentro de la carpeta `logs`.

## Estructura del proyecto

```text
software_fj_fase_4/
│
├── entidad.py
├── excepciones.py
├── cliente.py
├── servicio.py
├── reserva.py
├── main.py
├── README.md
└── logs/
    └── eventos.log  (se crea al ejecutar el programa)
```

## Archivos

- **entidad.py:** contiene la clase abstracta Entidad.
- **excepciones.py:** contiene los errores personalizados y la funcion para guardar registros.
- **cliente.py:** permite registrar clientes y validar sus datos.
- **servicio.py:** contiene la clase abstracta Servicio y los tres tipos de servicios.
- **reserva.py:** permite crear, confirmar, cancelar y consultar reservas.
- **main.py:** ejecuta el programa y realiza operaciones de prueba.
- **logs/:** almacena los eventos y errores del programa.

## Servicios disponibles

1. Reserva de sala: $50.000 por hora.
2. Alquiler de equipo: $30.000 por dia.
3. Asesoria especializada: $80.000 por hora.

Los calculos incluyen un impuesto predeterminado del 19% y permiten aplicar descuentos.

## Conceptos de programacion utilizados

- Programacion orientada a objetos.
- Abstraccion mediante clases abstractas.
- Herencia entre clases.
- Encapsulamiento de los datos del cliente.
- Polimorfismo mediante el metodo `calcular_costo`.
- Excepciones personalizadas.
- Manejo de errores con `try`, `except`, `else` y `finally`.
- Registro de eventos y errores en un archivo de texto.

En Python, el metodo `calcular_costo` utiliza parametros opcionales para permitir diferentes formas de calculo, como cambiar la cantidad, el descuento o el impuesto.

## Como ejecutar el programa

1. Descargar o clonar este repositorio.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Verificar que Python este instalado.
4. Abrir la terminal en la carpeta del proyecto.
5. Ejecutar:

```bash
python main.py
```

Al ejecutar el programa se realizan 11 operaciones de prueba, incluyendo casos correctos y casos que generan errores controlados. La carpeta `logs` y el archivo `eventos.log` se crean automaticamente cuando el programa registra el primer evento.

## Autoria

Proyecto academico desarrollado para la actividad Fase 4 del curso de Programacion.
