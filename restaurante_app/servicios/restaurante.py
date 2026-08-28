from typing import List, Optional
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class Restaurante:
    def __init__(self):
        self._productos: List[Producto] = ArchivoServicio.cargar_productos()
        self._usuarios: List[Usuario] = ArchivoServicio.cargar_usuarios()
        self._ventas: List[Venta] = ArchivoServicio.cargar_ventas()

    def registrar_producto(self, codigo: str, nombre: str, precio: float, stock: int) -> bool:
        if self.buscar_producto(codigo) is not None:
            return False
        nuevo_producto = Producto(codigo, nombre, precio, stock)
        self._productos.append(nuevo_producto)
        ArchivoServicio.guardar_productos(self._productos)
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    def obtener_productos(self) -> List[Producto]:
        return self._productos

    def registrar_usuario(self, identificacion: str, nombre: str) -> bool:
        if self.buscar_usuario(identificacion) is not None:
            return False
        nuevo_usuario = Usuario(identificacion, nombre)
        self._usuarios.append(nuevo_usuario)
        ArchivoServicio.guardar_usuarios(self._usuarios)
        return True

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None

    def obtener_usuarios(self) -> List[Usuario]:
        return self._usuarios

    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> bool:
        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto(codigo_producto)

        if usuario is None or producto is None:
            return False

        if cantidad <= 0 or producto.stock < cantidad:
            return False

        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        self._ventas.append(venta)

        producto.vender(cantidad)

        ArchivoServicio.guardar_ventas(self._ventas)
        ArchivoServicio.guardar_productos(self._productos)
        return True

    def consultar_ventas_usuario(self, identificacion_usuario: str) -> List[Venta]:
        ventas_usuario: List[Venta] = []
        for venta in self._ventas:
            if venta.usuario_id == identificacion_usuario:
                ventas_usuario.append(venta)
        return ventas_usuario