from entidad import Entidad
from excepciones import ClienteError, guardar_log


class Cliente(Entidad):
    def __init__(self, nombre, documento):
        nombre = nombre.strip() if isinstance(nombre, str) else ""
        documento = str(documento).strip()

        if nombre == "":
            raise ClienteError("El nombre del cliente no puede estar vacio.")

        if len(documento) < 5:
            raise ClienteError("El documento debe tener minimo 5 caracteres.")

        super().__init__(documento)
        self.__nombre = nombre
        self.__documento = documento
        guardar_log(f"Cliente registrado: {nombre}")

    def obtener_nombre(self):
        return self.__nombre

    def obtener_documento(self):
        return self.__documento

    def mostrar_informacion(self):
        return f"Cliente: {self.__nombre} | Documento: {self.__documento}"
