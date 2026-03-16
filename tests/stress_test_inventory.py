import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import inventory_manager
import excel_manager
import pandas as pd


def clear_inventory():
    df = pd.DataFrame(columns=["codigo", "producto", "precio_compra", "precio_venta", "stock"])
    excel_manager.guardar_datos(df)


@pytest.fixture(autouse=True)
def setup_and_teardown():
    clear_inventory()
    yield
    clear_inventory()


class TestStressInventory:

    def test_add_100_products(self):
        """STEP 3: Agregar 100 productos"""
        for i in range(1, 101):
            codigo = f"P{i:04d}"
            exito, mensaje = inventory_manager.agregar_producto(
                codigo, f"Producto_{i}", 10, 20, 5
            )
            assert exito is True, f"Error agregando {codigo}: {mensaje}"

        print(f"Agregados 100 productos")

    def test_verify_product_count(self):
        """STEP 3 + STEP 4: Agregar 100 productos y verificar cantidad"""
        for i in range(1, 101):
            codigo = f"P{i:04d}"
            inventory_manager.agregar_producto(codigo, f"Producto_{i}", 10, 20, 5)

        productos = inventory_manager.ver_productos()
        assert len(productos) == 100, f"Esperado 100 productos, obtenido {len(productos)}"

        print(f"Cantidad verificada: {len(productos)} productos")

    def test_search_performance(self):
        """STEP 5: Probar búsqueda de productos"""
        for i in range(1, 101):
            codigo = f"P{i:04d}"
            inventory_manager.agregar_producto(codigo, f"Producto_{i}", 10, 20, 5)

        producto_10 = inventory_manager.buscar_producto("P0010")
        assert producto_10 is not None, "Producto P0010 no encontrado"
        assert producto_10["producto"] == "Producto_10"

        producto_50 = inventory_manager.buscar_producto("P0050")
        assert producto_50 is not None, "Producto P0050 no encontrado"
        assert producto_50["producto"] == "Producto_50"

        producto_99 = inventory_manager.buscar_producto("P0099")
        assert producto_99 is not None, "Producto P0099 no encontrado"
        assert producto_99["producto"] == "Producto_99"

        print("Búsqueda de productos exitosa")

    def test_mass_price_update(self):
        """STEP 6: Actualización masiva de precios"""
        for i in range(1, 101):
            codigo = f"P{i:04d}"
            inventory_manager.agregar_producto(codigo, f"Producto_{i}", 10, 20, 5)

        exito, mensaje = inventory_manager.aumentar_precios(10)
        assert exito is True, f"Error al aumentar precios: {mensaje}"

        producto = inventory_manager.buscar_producto("P0001")
        assert producto is not None
        precio_esperado = 22.0
        assert abs(producto["precio_venta"] - precio_esperado) < 0.01, \
            f"Precio esperado {precio_esperado}, obtenido {producto['precio_venta']}"

        print(f"Precios actualizados: 20 -> {producto['precio_venta']}")

    def test_update_operations(self):
        """STEP 7: Probar operaciones de actualización"""
        for i in range(1, 101):
            codigo = f"P{i:04d}"
            inventory_manager.agregar_producto(codigo, f"Producto_{i}", 10, 20, 5)

        exito, mensaje = inventory_manager.actualizar_precio("P0001", 25)
        assert exito is True, f"Error al actualizar precio: {mensaje}"

        producto_actualizado = inventory_manager.buscar_producto("P0001")
        assert producto_actualizado["precio_venta"] == 25

        exito, mensaje = inventory_manager.actualizar_stock("P0002", 15)
        assert exito is True, f"Error al actualizar stock: {mensaje}"

        producto_stock = inventory_manager.buscar_producto("P0002")
        assert producto_stock["stock"] == 15

        print("Operaciones de actualización exitosas")

    def test_delete_operations(self):
        """STEP 8: Eliminar 10 productos"""
        for i in range(1, 101):
            codigo = f"P{i:04d}"
            inventory_manager.agregar_producto(codigo, f"Producto_{i}", 10, 20, 5)

        for i in range(1, 11):
            codigo = f"P{i:04d}"
            exito, mensaje = inventory_manager.eliminar_producto(codigo)
            assert exito is True, f"Error al eliminar {codigo}: {mensaje}"

        productos = inventory_manager.ver_productos()
        assert len(productos) == 90, f"Esperado 90 productos, obtenido {len(productos)}"

        producto_eliminado = inventory_manager.buscar_producto("P0005")
        assert producto_eliminado is None, "Producto P0005 debería estar eliminado"

        print(f"Eliminados 10 productos, restantes: {len(productos)}")

    def test_data_integrity(self):
        """STEP 9: Verificar integridad de datos"""
        for i in range(1, 101):
            codigo = f"P{i:04d}"
            inventory_manager.agregar_producto(codigo, f"Producto_{i}", 10, 20, 5)

        productos = inventory_manager.ver_productos()
        assert len(productos) == 100

        for p in productos:
            assert p["codigo"], "Código vacío"
            assert p["producto"], "Nombre de producto vacío"
            assert isinstance(p["precio_compra"], (int, float)), "precio_compra no es numérico"
            assert isinstance(p["precio_venta"], (int, float)), "precio_venta no es numérico"
            assert isinstance(p["stock"], (int, float)), "stock no es numérico"
            assert p["precio_compra"] >= 0, "precio_compra negativo"
            assert p["precio_venta"] >= 0, "precio_venta negativo"
            assert p["stock"] >= 0, "stock negativo"

        df = pd.read_excel("inventario.xlsx", index_col=0)
        assert len(df) == 100, "Archivo Excel no tiene 100 registros"
        assert list(df.columns) == ["codigo", "producto", "precio_compra", "precio_venta", "stock"]

        print("Integridad de datos verificada")

    def test_full_stress_workflow(self):
        """STEP 11: Workflow completo de stress test"""
        for i in range(1, 101):
            codigo = f"P{i:04d}"
            inventory_manager.agregar_producto(codigo, f"Producto_{i}", 10, 20, 5)

        productos = inventory_manager.ver_productos()
        assert len(productos) == 100

        producto = inventory_manager.buscar_producto("P0050")
        assert producto is not None

        inventory_manager.aumentar_precios(10)
        producto = inventory_manager.buscar_producto("P0050")
        assert abs(producto["precio_venta"] - 22.0) < 0.01

        inventory_manager.actualizar_precio("P0001", 30)
        producto = inventory_manager.buscar_producto("P0001")
        assert producto["precio_venta"] == 30

        inventory_manager.actualizar_stock("P0002", 50)
        producto = inventory_manager.buscar_producto("P0002")
        assert producto["stock"] == 50

        for i in range(1, 11):
            inventory_manager.eliminar_producto(f"P{i:04d}")

        productos = inventory_manager.ver_productos()
        assert len(productos) == 90

        print("\n=== Stress test completed successfully ===")

    @pytest.mark.skip(reason="Optional - solo para verificar escalabilidad")
    def test_500_products(self):
        """STEP 10: Test opcional con 500 productos"""
        for i in range(1, 501):
            codigo = f"P{i:04d}"
            exito, mensaje = inventory_manager.agregar_producto(
                codigo, f"Producto_{i}", 10, 20, 5
            )
            assert exito is True, f"Error agregando {codigo}: {mensaje}"

        productos = inventory_manager.ver_productos()
        assert len(productos) == 500

        inventory_manager.aumentar_precios(10)

        df = pd.read_excel("inventario.xlsx")
        assert len(df) == 500

        print(f"Test de 500 productos completado exitosamente")
