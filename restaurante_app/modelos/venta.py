class Venta:
    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad vendida debe ser mayor que cero.")

        self._usuario_id = usuario_id
        self._producto_codigo = producto_codigo
        self._cantidad = cantidad

    @property
    def usuario_id(self) -> str:
        return self._usuario_id

    @property
    def producto_codigo(self) -> str:
        return self._producto_codigo

    @property
    def cantidad(self) -> int:
        return self._cantidad

    def a_diccionario(self) -> dict:
        return {
            "usuario_id": self._usuario_id,
            "producto_codigo": self._producto_codigo,
            "cantidad": self._cantidad
        }

    @staticmethod
    def desde_diccionario(datos: dict) -> 'Venta':
        try:
            return Venta(
                usuario_id=datos["usuario_id"],
                producto_codigo=datos["producto_codigo"],
                cantidad=int(datos["cantidad"])
            )
        except KeyError as e:
            raise KeyError(f"Falta la clave esperada en el JSON de venta: {e}")