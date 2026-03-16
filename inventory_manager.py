import excel_manager


def ver_productos():
    df = excel_manager.cargar_datos()
    if df.empty:
        return []
    df = df.reset_index()
    return df.to_dict("records")


def buscar_producto(codigo):
    return excel_manager.leer_producto(codigo)


def agregar_producto(codigo, producto, precio_compra, precio_venta, stock):
    if not codigo or not codigo.strip():
        raise ValueError("El código no puede estar vacío")
    
    codigo = codigo.strip()
    
    if excel_manager.existe_producto(codigo):
        raise ValueError("El código ya existe")
    
    if not producto or not producto.strip():
        raise ValueError("El nombre del producto no puede estar vacío")
    
    try:
        precio_compra = float(precio_compra)
        precio_venta = float(precio_venta)
        stock = int(stock)
    except ValueError:
        raise ValueError("Los precios y stock deben ser numéricos")
    
    if precio_compra < 0:
        raise ValueError("El precio de compra no puede ser negativo")
    
    if precio_venta < 0:
        raise ValueError("El precio de venta no puede ser negativo")
    
    if precio_compra > precio_venta:
        raise ValueError("El precio de compra no puede ser mayor que el precio de venta")
    
    if stock < 0:
        raise ValueError("El stock no puede ser negativo")
    
    try:
        excel_manager.escribir_producto(codigo, producto.strip(), precio_compra, precio_venta, stock)
        return True, "Producto agregado exitosamente"
    except Exception as e:
        return False, f"Error al guardar: {e}"


def eliminar_producto(codigo):
    if not codigo or not codigo.strip():
        raise ValueError("El código no puede estar vacío")
    
    codigo = codigo.strip()
    
    if not excel_manager.existe_producto(codigo):
        raise ValueError("El producto no existe")
    
    try:
        excel_manager.eliminar_producto(codigo)
        return True, "Producto eliminado exitosamente"
    except Exception as e:
        return False, f"Error al eliminar: {e}"


def actualizar_precio(codigo, nuevo_precio):
    if not codigo or not codigo.strip():
        raise ValueError("El código no puede estar vacío")
    
    codigo = codigo.strip()
    
    if not excel_manager.existe_producto(codigo):
        raise ValueError("El producto no existe")
    
    try:
        nuevo_precio = float(nuevo_precio)
    except ValueError:
        raise ValueError("El precio debe ser numérico")
    
    if nuevo_precio < 0:
        raise ValueError("El precio no puede ser negativo")
    
    try:
        excel_manager.actualizar_producto(codigo, {"precio_venta": nuevo_precio})
        return True, "Precio actualizado exitosamente"
    except Exception as e:
        return False, f"Error al actualizar: {e}"


def actualizar_stock(codigo, nueva_cantidad):
    if not codigo or not codigo.strip():
        raise ValueError("El código no puede estar vacío")
    
    codigo = codigo.strip()
    
    if not excel_manager.existe_producto(codigo):
        raise ValueError("El producto no existe")
    
    try:
        nueva_cantidad = int(nueva_cantidad)
    except ValueError:
        raise ValueError("El stock debe ser numérico")
    
    if nueva_cantidad < 0:
        raise ValueError("El stock no puede ser negativo")
    
    try:
        excel_manager.actualizar_producto(codigo, {"stock": nueva_cantidad})
        return True, "Stock actualizado exitosamente"
    except Exception as e:
        return False, f"Error al actualizar: {e}"


def aumentar_precios(porcentaje):
    try:
        porcentaje = float(porcentaje)
    except ValueError:
        raise ValueError("El porcentaje debe ser un número")
    
    if porcentaje < 0:
        raise ValueError("El porcentaje no puede ser negativo")
    
    df = excel_manager.cargar_datos()
    if df.empty:
        raise ValueError("No hay productos en el inventario")
    
    try:
        cantidad = excel_manager.aumentar_precios_porcentaje(porcentaje)
        return True, f"Precios aumentados en {porcentaje}% para {cantidad} productos"
    except Exception as e:
        return False, f"Error al actualizar precios: {e}"


def actualizar_producto(codigo, producto, precio_compra, precio_venta, stock):
    if not codigo or not codigo.strip():
        raise ValueError("El código no puede estar vacío")
    
    codigo = codigo.strip()
    
    if not excel_manager.existe_producto(codigo):
        raise ValueError("El producto no existe")
    
    if not producto or not producto.strip():
        raise ValueError("El nombre del producto no puede estar vacío")
    
    try:
        precio_compra = float(precio_compra)
        precio_venta = float(precio_venta)
        stock = int(stock)
    except ValueError:
        raise ValueError("Los precios y stock deben ser numéricos")
    
    if precio_compra < 0:
        raise ValueError("El precio de compra no puede ser negativo")
    
    if precio_venta < 0:
        raise ValueError("El precio de venta no puede ser negativo")
    
    if precio_compra > precio_venta:
        raise ValueError("El precio de compra no puede ser mayor que el precio de venta")
    
    if stock < 0:
        raise ValueError("El stock no puede ser negativo")
    
    try:
        excel_manager.actualizar_producto(codigo, {
            "producto": producto.strip(),
            "precio_compra": precio_compra,
            "precio_venta": precio_venta,
            "stock": stock
        })
        return True, "Producto actualizado exitosamente"
    except Exception as e:
        return False, f"Error al actualizar: {e}"
