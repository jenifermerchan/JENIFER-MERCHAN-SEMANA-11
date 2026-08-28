# Restaurante App - Semana 11

## Estudiante:
**JENIFER ESTEFANIA MERCHAN JAUREGUI** 

## Descripción del Sistema
`restaurante_app` es un sistema desarrollado en Python que simula la gestión básica de un restaurante. En esta versión, 
el sistema evoluciona incorporando relaciones entre usuarios y productos mediante la creación de la entidad `Venta`, 
control de stock en tiempo real y persistencia completa en archivos JSON.

## Estructura del Proyecto
```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
```
## Responsabilidad de los Componentes
-`modelos/producto.py`: Define la clase `Producto`, maneja encapsulamiento, atributos (incluyendo `stock`), métodos de 
deserialización/serialización y control de inventario.

-`modelos/usuario.py`: Define la clase `Usuario` y sus validaciones.

-`modelos/venta.py`: Representa la transacción entre un `Usuario` y un `Producto` (`usuario_id, producto_codigo, cantidad`).

-`servicios/archivo_servicio.py`: Encargado de leer y escribir en los archivos JSON (`productos.json, usuarios.json, ventas.json`) 
usando `json.dump()` y `json.load()`.

-`servicios/restaurante.py`: Centraliza las colecciones en memoria, aplica reglas de negocio (validar datos, procesar ventas, 
reducir stock, filtrar ventas por usuario) y coordina la actualización en archivos.

-`main.py`: Interfaz por consola que interactúa con el usuario y realiza llamadas exclusivas a los métodos del servicio
`Restaurante`.

## Funcionamiento del Stock y Relación Usuario-Producto mediante la Venta
Cada producto posee una cantidad disponible (`stock`). Cuando un usuario realiza una compra:

-Se valida que el usuario y el producto existan en el sistema.

-Se verifica que la cantidad solicitada sea mayor a cero y menor o igual al stock disponible.

-Se crea un objeto `Venta` que vincula el `usuario_id` con el `producto_codigo`.

-El producto disminuye su stock en la cantidad especificada (`vender()`).

-La venta y el stock actualizado se persisten de manera inmediata en los archivos JSON correspondientes.

## Persistencia de Datos
La persistencia se maneja de forma automática:

-Al registrar un usuario: actualiza `usuarios.json`.

-Al registrar un producto: actualiza `productos.json`.

-Al realizar una venta exitosa: actualiza tanto `ventas.json` como `productos.json`.

-Al iniciar la aplicación, los objetos son reconstruidos en memoria a partir de los datos almacenados en la carpeta `datos`.

## Excepciones Controladas
-`FileNotFoundError`: Retorna colecciones vacías si los archivos JSON aún no se han creado. 

-`json.JSONDecodeError`: Captura archivos JSON corruptos o no válidos.    

-`PermissionError`: Controla fallos de lectura o escritura por falta de permisos en el sistema operativo.    

-`KeyError`: Detecta claves faltantes durante la conversión de diccionarios JSON a objetos.    

-`ValueError`: Impide la creación o actualización con montos, cantidades o números no válidos o vacíos.    

## Forma de Ejecución
Ejecutar el archivo principal desde la terminal: `python main.py`.

## Pruebas Realizadas
-Comprobación de Persistencia Inicial: Creación de usuarios y productos, cierre y reapertura del sistema comprobando que
los datos persistieran correctamente.  

-Venta Válida: Venta de 2 unidades sobre un producto con stock de 54. Se comprobó la reducción del stock a 52, la creación 
del registro en `ventas.json` y la correcta asignación al usuario.  

-Venta Inválida (Stock Insuficiente): Intento de venta de una cantidad superior al stock restante. El sistema rechazó la 
transacción, conservando intactos los registros y el stock actual.   

-Consulta de Ventas: Filtrado de compras por usuario validando la correcta recuperación e iteración de la colección de 
ventas.  