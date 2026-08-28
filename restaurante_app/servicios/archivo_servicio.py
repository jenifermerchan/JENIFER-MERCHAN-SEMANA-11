import json
import os
from typing import List
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

class ArchivoServicio:
    RUTA_PRODUCTOS = os.path.join("datos", "productos.json")
    RUTA_USUARIOS = os.path.join("datos", "usuarios.json")
    RUTA_VENTAS = os.path.join("datos", "ventas.json")

    @staticmethod
    def _asegurar_directorio():
        os.makedirs("datos", exist_ok=True)

    @classmethod
    def cargar_productos(cls) -> List[Producto]:
        cls._asegurar_directorio()
        productos = []
        try:
            with open(cls.RUTA_PRODUCTOS, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                for item in datos:
                    productos.append(Producto.desde_diccionario(item))
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Error: El archivo productos.json tiene un formato no válido.")
            return []
        except PermissionError:
            print("Error: Permisos insuficientes para leer productos.json.")
            return []
        except KeyError as e:
            print(f"Error en estructura de producto: {e}")
            return []
        return productos

    @classmethod
    def guardar_productos(cls, productos: List[Producto]) -> None:
        cls._asegurar_directorio()
        try:
            datos = [p.a_diccionario() for p in productos]
            with open(cls.RUTA_PRODUCTOS, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
        except PermissionError:
            print("Error: Permisos insuficientes para escribir en productos.json.")

    @classmethod
    def cargar_usuarios(cls) -> List[Usuario]:
        cls._asegurar_directorio()
        usuarios = []
        try:
            with open(cls.RUTA_USUARIOS, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                for item in datos:
                    usuarios.append(Usuario.desde_diccionario(item))
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Error: El archivo usuarios.json tiene un formato no válido.")
            return []
        except PermissionError:
            print("Error: Permisos insuficientes para leer usuarios.json.")
            return []
        except KeyError as e:
            print(f"Error en estructura de usuario: {e}")
            return []
        return usuarios

    @classmethod
    def guardar_usuarios(cls, usuarios: List[Usuario]) -> None:
        cls._asegurar_directorio()
        try:
            datos = [u.a_diccionario() for u in usuarios]
            with open(cls.RUTA_USUARIOS, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
        except PermissionError:
            print("Error: Permisos insuficientes para escribir en usuarios.json.")

    @classmethod
    def cargar_ventas(cls) -> List[Venta]:
        cls._asegurar_directorio()
        ventas = []
        try:
            with open(cls.RUTA_VENTAS, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                for item in datos:
                    ventas.append(Venta.desde_diccionario(item))
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Error: El archivo ventas.json tiene un formato no válido.")
            return []
        except PermissionError:
            print("Error: Permisos insuficientes para leer ventas.json.")
            return []
        except KeyError as e:
            print(f"Error en estructura de venta: {e}")
            return []
        return ventas

    @classmethod
    def guardar_ventas(cls, ventas: List[Venta]) -> None:
        cls._asegurar_directorio()
        try:
            datos = [v.a_diccionario() for v in ventas]
            with open(cls.RUTA_VENTAS, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
        except PermissionError:
            print("Error: Permisos insuficientes para escribir en ventas.json.")