from servicios.restaurante import Restaurante

def mostrar_menu():
    print("\n--- SISTEMA RESTAURANTE APP ---")
    print("1. Registrar Usuario")
    print("2. Listar Usuarios")
    print("3. Registrar Producto")
    print("4. Listar Productos")
    print("5. Realizar Venta")
    print("6. Consultar Ventas por Usuario")
    print("7. Salir")

def main():
    restaurante = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            identificacion = input("Ingrese identificación del usuario: ").strip()
            nombre = input("Ingrese nombre del usuario: ").strip()
            try:
                if restaurante.registrar_usuario(identificacion, nombre):
                    print("Usuario registrado exitosamente.")
                else:
                    print("Error: Ya existe un usuario con esa identificación.")
            except ValueError as e:
                print(f"Error de validación: {e}")

        elif opcion == "2":
            usuarios = restaurante.obtener_usuarios()
            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                print("\n--- LISTA DE USUARIOS ---")
                for u in usuarios:
                    print(f"ID: {u.identificacion} | Nombre: {u.nombre}")

        elif opcion == "3":
            codigo = input("Ingrese código del producto: ").strip()
            nombre = input("Ingrese nombre del producto: ").strip()
            try:
                precio = float(input("Ingrese precio: "))
                stock = int(input("Ingrese stock disponible: "))
                if restaurante.registrar_producto(codigo, nombre, precio, stock):
                    print("Producto registrado exitosamente.")
                else:
                    print("Error: Ya existe un producto con ese código.")
            except ValueError as e:
                print(f"Error: Ingrese valores numéricos válidos. ({e})")

        elif opcion == "4":
            productos = restaurante.obtener_productos()
            if not productos:
                print("No hay productos registrados.")
            else:
                print("\n--- LISTA DE PRODUCTOS ---")
                for p in productos:
                    print(f"Código: {p.codigo} | Nombre: {p.nombre} | Precio: ${p.precio:.2f} | Stock: {p.stock}")

        elif opcion == "5":
            identificacion = input("Ingrese ID del usuario comprador: ").strip()
            codigo = input("Ingrese código del producto a comprar: ").strip()
            try:
                cantidad = int(input("Ingrese cantidad a vender: "))
                if restaurante.vender_producto(codigo, identificacion, cantidad):
                    print("Venta realizada y stock actualizado con éxito.")
                else:
                    print("Error: Operación rechazada. Verifique que usuario y producto existan, y que exista stock suficiente.")
            except ValueError:
                print("Error: La cantidad debe ser un entero válido.")

        elif opcion == "6":
            identificacion = input("Ingrese ID del usuario a consultar: ").strip()
            usuario = restaurante.buscar_usuario(identificacion)
            if usuario is None:
                print("Error: Usuario no encontrado.")
            else:
                ventas = restaurante.consultar_ventas_usuario(identificacion)
                print(f"\n--- VENTAS DEL USUARIO: {usuario.nombre} ({usuario.identificacion}) ---")
                if not ventas:
                    print("El usuario no ha realizado compras.")
                else:
                    for v in ventas:
                        prod = restaurante.buscar_producto(v.producto_codigo)
                        nombre_prod = prod.nombre if prod else "Desconocido"
                        print(f"Producto: {nombre_prod} (Código: {v.producto_codigo}) | Cantidad: {v.cantidad}")

        elif opcion == "7":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()