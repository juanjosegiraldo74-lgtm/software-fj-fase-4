from datetime import datetime
from pathlib import Path

# Carpeta y archivo donde se guardan los eventos y errores.
CARPETA_LOGS = Path(__file__).parent / "logs"
ARCHIVO_LOG = CARPETA_LOGS / "eventos.log"


class ClienteError(Exception):
    pass


class ServicioError(Exception):
    pass


class ReservaError(Exception):
    pass


def guardar_log(mensaje):
    """Guarda un evento o error en logs/eventos.log."""
    CARPETA_LOGS.mkdir(exist_ok=True)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(ARCHIVO_LOG, "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha}] {mensaje}\\n")
