import pandas as pd
import os

ARCHIVO_EXCEL = "inventario.xlsx"
COLUMNAS = ["codigo", "producto", "precio_compra", "precio_venta", "stock"]


def _inicializar_excel():
    if not os.path.exists(ARCHIVO_EXCEL):
        df = pd.DataFrame(columns=COLUMNAS)
        df.to_excel(ARCHIVO_EXCEL, index=False)


def cargar_datos():
    _inicializar_excel()
    try:
        df = pd.read_excel(ARCHIVO_EXCEL)
        if not df.empty:
            df["codigo"] = df["codigo"].astype(str)
        return df
    except Exception:
        return pd.DataFrame(columns=COLUMNAS)


def guardar_datos(df):
    try:
        df.to_excel(ARCHIVO_EXCEL, index=False)
    except Exception as e:
        raise Exception(f"Error al guardar el archivo: {e}")


def existe_producto(codigo):
    df = cargar_datos()
    codigo = str(codigo).strip()
    return codigo in df["codigo"].values


def leer_producto(codigo):
    df = cargar_datos()
    codigo = str(codigo).strip()
    producto = df[df["codigo"] == codigo]
    if producto.empty:
        return None
    return producto.iloc[0].to_dict()


def escribir_producto(codigo, producto, precio_compra, precio_venta, stock):
    df = cargar_datos()
    nuevo = pd.DataFrame([{
        "codigo": str(codigo),
        "producto": str(producto),
        "precio_compra": precio_compra,
        "precio_venta": precio_venta,
        "stock": stock
    }])
    
    if df.empty:
        df = nuevo
    else:
        df = pd.concat([df, nuevo], ignore_index=True)
    
    guardar_datos(df)


def actualizar_producto(codigo, datos):
    df = cargar_datos()
    for clave, valor in datos.items():
        df.at[df[df["codigo"] == codigo].index[0], clave] = valor
    guardar_datos(df)


def eliminar_producto(codigo):
    df = cargar_datos()
    df = df[df["codigo"] != codigo]
    guardar_datos(df)


def aumentar_precios_porcentaje(porcentaje):
    df = cargar_datos()
    if df.empty:
        return 0
    df["precio_venta"] = df["precio_venta"] * (1 + porcentaje / 100)
    guardar_datos(df)
    return len(df)
