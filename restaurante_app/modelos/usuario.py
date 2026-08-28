class Usuario:
    def __init__(self, identificacion: str, nombre: str):
        if not identificacion.strip():
            raise ValueError("La identificación no puede estar vacía.")
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        self._identificacion = identificacion
        self._nombre = nombre

    @property
    def identificacion(self) -> str:
        return self._identificacion

    @property
    def nombre(self) -> str:
        return self._nombre

    def a_diccionario(self) -> dict:
        return {
            "identificacion": self._identificacion,
            "nombre": self._nombre
        }

    @staticmethod
    def desde_diccionario(datos: dict) -> 'Usuario':
        try:
            return Usuario(
                identificacion=datos["identificacion"],
                nombre=datos["nombre"]
            )
        except KeyError as e:
            raise KeyError(f"Falta la clave esperada en el JSON de usuario: {e}")