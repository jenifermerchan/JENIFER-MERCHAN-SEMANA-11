class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if stock < 0:
            raise ValueError("El stock inicial no puede ser negativo.")

        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def precio(self) -> float:
        return self._precio

    @property
    def stock(self) -> int:
        return self._stock

    def vender(self, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor que cero.")
        if cantidad > self._stock:
            raise ValueError("No hay suficiente stock disponible.")
        self._stock -= cantidad

    def a_diccionario(self) -> dict:
        return {
            "codigo": self._codigo,
            "nombre": self._nombre,
            "precio": self._precio,
            "stock": self._stock
        }

    @staticmethod
    def desde_diccionario(datos: dict) -> 'Producto':
        try:
            return Producto(
                codigo=datos["codigo"],
                nombre=datos["nombre"],
                precio=float(datos["precio"]),
                stock=int(datos["stock"])
            )
        except KeyError as e:
            raise KeyError(f"Falta la clave esperada en el JSON de producto: {e}")