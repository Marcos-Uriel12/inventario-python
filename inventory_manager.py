import excel_manager


def ver_productos():
    df = excel_manager.cargar_datos()
    if df.empty:
        return []
    return df.to_dict("records")


def buscar_producto(codigo):
    return excel_manager.leer_producto(codigo)


def agregar_producto(codigo, producto, precio_compra, precio_venta, stock):
    if not codigo or not codigo.strip():
        return False, "El código no puede estar vacío"
    
    codigo = codigo.strip()
    
    if excel_manager.existe_producto(codigo):
        return False, "El código ya existe"
    
    if not producto or not producto.strip():
        return False, "El nombre del producto no puede estar vacío"
    
    try:
        precio_compra = float(precio_compra)
        precio_venta = float(precio_venta)
        stock = int(stock)
    except ValueError:
        return False, "Los precios y stock deben ser numéricos"
    
    if precio_compra < 0 or precio_venta < 0:
        return False, "Los precios no pueden ser negativos"
    
    if precio_compra > precio_venta:
        return False, "El precio de compra no puede ser mayor al precio de venta"
    
    if stock < 0:
        return False, "El stock no puede ser negativo"
    
    try:
        excel_manager.escribir_producto(codigo, producto.strip(), precio_compra, precio_venta, stock)
        return True, "Producto agregado exitosamente"
    except Exception as e:
        return False, f"Error al guardar: {e}"


def eliminar_producto(codigo):
    if not codigo or not codigo.strip():
        return False, "El código no puede estar vacío"
    
    codigo = codigo.strip()
    
    if not excel_manager.existe_producto(codigo):
        return False, "El producto no existe"
    
    try:
        excel_manager.eliminar_producto(codigo)
        return True, "Producto eliminado exitosamente"
    except Exception as e:
        return False, f"Error al eliminar: {e}"


def actualizar_precio(codigo, nuevo_precio):
    if not codigo or not codigo.strip():
        return False, "El código no puede estar vacío"
    
    codigo = codigo.strip()
    
    if not excel_manager.existe_producto(codigo):
        return False, "El producto no existe"
    
    try:
        nuevo_precio = float(nuevo_precio)
    except ValueError:
        return False, "El precio debe ser numérico"
    
    if nuevo_precio < 0:
        return False, "El precio no puede ser negativo"
    
    try:
        excel_manager.actualizar_producto(codigo, {"precio_venta": nuevo_precio})
        return True, "Precio actualizado exitosamente"
    except Exception as e:
        return False, f"Error al actualizar: {e}"


def actualizar_stock(codigo, nueva_cantidad):
    if not codigo or not codigo.strip():
        return False, "El código no puede estar vacío"
    
    codigo = codigo.strip()
    
    if not excel_manager.existe_producto(codigo):
        return False, "El producto no existe"
    
    try:
        nueva_cantidad = int(nueva_cantidad)
    except ValueError:
        return False, "El stock debe ser numérico"
    
    if nueva_cantidad < 0:
        return False, "El stock no puede ser negativo"
    
    try:
        excel_manager.actualizar_producto(codigo, {"stock": nueva_cantidad})
        return True, "Stock actualizado exitosamente"
    except Exception as e:
        return False, f"Error al actualizar: {e}"


def aumentar_precios(porcentaje):
    try:
        porcentaje = float(porcentaje)
    except ValueError:
        return False, "El porcentaje debe ser un número"
    
    if porcentaje < 0:
        return False, "El porcentaje no puede ser negativo"
    
    df = excel_manager.cargar_datos()
    if df.empty:
        return False, "No hay productos en el inventario"
    
    try:
        cantidad = excel_manager.aumentar_precios_porcentaje(porcentaje)
        return True, f"Precios aumentados en {porcentaje}% para {cantidad} productos"
    except Exception as e:
        return False, f"Error al actualizar precios: {e}"
