import inventory_manager


def mostrar_menu():
    print("\n" + "=" * 40)
    print("       SISTEMA DE INVENTARIO")
    print("=" * 40)
    print("1. Ver productos")
    print("2. Buscar producto")
    print("3. Agregar producto")
    print("4. Eliminar producto")
    print("5. Actualizar precio")
    print("6. Actualizar stock")
    print("7. Aumentar precios por porcentaje")
    print("8. Salir")
    print("=" * 40)


def mostrar_productos():
    productos = inventory_manager.ver_productos()
    if not productos:
        print("\nNo hay productos en el inventario.")
        return
    
    print("\n" + "-" * 70)
    print(f"{'Código':<10} {'Producto':<20} {'Compra':<10} {'Venta':<10} {'Stock':<8}")
    print("-" * 70)
    for p in productos:
        print(f"{p['codigo']:<10} {p['producto']:<20} ${p['precio_compra']:<9.2f} ${p['precio_venta']:<9.2f} {p['stock']:<8}")
    print("-" * 70)


def buscar_producto():
    codigo = input("Ingrese el código del producto: ").strip()
    if not codigo:
        print("El código no puede estar vacío.")
        return
    
    producto = inventory_manager.buscar_producto(codigo)
    if producto:
        print("\nProducto encontrado:")
        print(f"  Código: {producto['codigo']}")
        print(f"  Nombre: {producto['producto']}")
        print(f"  Precio de compra: ${producto['precio_compra']:.2f}")
        print(f"  Precio de venta: ${producto['precio_venta']:.2f}")
        print(f"  Stock: {producto['stock']}")
    else:
        print("Producto no encontrado.")


def agregar_producto():
    print("\n--- Agregar Producto ---")
    codigo = input("Código: ").strip()
    producto = input("Nombre del producto: ").strip()
    
    if not codigo:
        print("El código no puede estar vacío.")
        return
    
    if not producto:
        print("El nombre del producto no puede estar vacío.")
        return
    
    try:
        precio_compra = float(input("Precio de compra: "))
        precio_venta = float(input("Precio de venta: "))
        stock = int(input("Stock: "))
    except ValueError:
        print("Error: Precio y stock deben ser números válidos.")
        return
    
    exito, mensaje = inventory_manager.agregar_producto(codigo, producto, precio_compra, precio_venta, stock)
    print(mensaje)


def eliminar_producto():
    print("\n--- Eliminar Producto ---")
    codigo = input("Ingrese el código del producto a eliminar: ").strip()
    
    if not codigo:
        print("El código no puede estar vacío.")
        return
    
    producto = inventory_manager.buscar_producto(codigo)
    if not producto:
        print("Producto no encontrado.")
        return
    
    print(f"\nProducto a eliminar: {producto['producto']}")
    confirmacion = input("¿Está seguro de eliminar? (S/N): ").strip().upper()
    try:
        if confirmacion == "S":
            exito, mensaje = inventory_manager.eliminar_producto(codigo)
            print(mensaje)
        elif confirmacion == "N":
            print("Operación cancelada.")
    except Exception as e:
        print("Error caracter incorrecto")


def actualizar_precio():
    print("\n--- Actualizar Precio ---")
    codigo = input("Ingrese el código del producto: ").strip()
    
    try:
        nuevo_precio = float(input("Nuevo precio de venta: "))
    except ValueError:
        print("Error: El precio debe ser un número válido.")
        return
    
    exito, mensaje = inventory_manager.actualizar_precio(codigo, nuevo_precio)
    print(mensaje)


def actualizar_stock():
    print("\n--- Actualizar Stock ---")
    codigo = input("Ingrese el código del producto: ").strip()
    
    try:
        nuevo_stock = int(input("Nuevo stock: "))
    except ValueError:
        print("Error: El stock debe ser un número entero válido.")
        return
    
    exito, mensaje = inventory_manager.actualizar_stock(codigo, nuevo_stock)
    print(mensaje)


def aumentar_precios():
    print("\n--- Aumentar Precios por Porcentaje ---")
    
    productos = inventory_manager.ver_productos()
    if not productos:
        print("No hay productos en el inventario.")
        return
    
    try:
        porcentaje = float(input("Ingrese el porcentaje de aumento: "))
    except ValueError:
        print("Error: El porcentaje debe ser un número.")
        return
    
    if porcentaje < 0:
        print("Error: El porcentaje no puede ser negativo.")
        return
    
    print(f"\nSe aumentarán los precios de {len(productos)} productos en {porcentaje}%")
    print(f"\nPrecios actuales:")
    for p in productos[:5]:
        print(f"  {p['codigo']}: ${p['precio_venta']:.2f}")
    if len(productos) > 5:
        print(f"  ... y {len(productos) - 5} más")
    
    confirmacion = input("\n¿Está seguro? (S/N): ").strip().upper()
    try:
        if confirmacion == "S":
            exito, mensaje = inventory_manager.aumentar_precios(porcentaje)
            print(mensaje)
        elif confirmacion == "N":
            print("Operación cancelada.")
    except Exception as e:
        print("Error caracter incorrecto")

def iniciar():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            buscar_producto()
        elif opcion == "3":
            agregar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            actualizar_precio()
        elif opcion == "6":
            actualizar_stock()
        elif opcion == "7":
            aumentar_precios()
        elif opcion == "8":
            print("\n¡Gracias por usar el sistema de inventario!")
            break
        else:
            print("\nOpción inválida. Por favor seleccione una opción del 1 al 8.")
