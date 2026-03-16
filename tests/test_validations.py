import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import inventory_manager
import excel_manager


class TestValidaciones:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.test_codigo = "TEST001"
        if excel_manager.existe_producto(self.test_codigo):
            excel_manager.eliminar_producto(self.test_codigo)
        yield
        if excel_manager.existe_producto(self.test_codigo):
            excel_manager.eliminar_producto(self.test_codigo)

    def test_empty_code(self):
        with pytest.raises(ValueError, match="El código no puede estar vacío"):
            inventory_manager.agregar_producto("", "Producto Test", 100, 150, 10)

    def test_empty_code_with_spaces(self):
        with pytest.raises(ValueError, match="El código no puede estar vacío"):
            inventory_manager.agregar_producto("   ", "Producto Test", 100, 150, 10)

    def test_duplicate_code(self):
        inventory_manager.agregar_producto(self.test_codigo, "Producto Test", 100, 150, 10)
        
        with pytest.raises(ValueError, match="El código ya existe"):
            inventory_manager.agregar_producto(self.test_codigo, "Producto Test 2", 200, 250, 20)

    def test_empty_producto(self):
        with pytest.raises(ValueError, match="El nombre del producto no puede estar vacío"):
            inventory_manager.agregar_producto(self.test_codigo, "", 100, 150, 10)

    def test_negative_purchase_price(self):
        with pytest.raises(ValueError, match="El precio de compra no puede ser negativo"):
            inventory_manager.agregar_producto(self.test_codigo, "Producto Test", -100, 150, 10)

    def test_negative_sale_price(self):
        with pytest.raises(ValueError, match="El precio de venta no puede ser negativo"):
            inventory_manager.agregar_producto(self.test_codigo, "Producto Test", 100, -150, 10)

    def test_purchase_price_greater_than_sale(self):
        with pytest.raises(ValueError, match="El precio de compra no puede ser mayor que el precio de venta"):
            inventory_manager.agregar_producto(self.test_codigo, "Producto Test", 200, 150, 10)

    def test_negative_stock(self):
        with pytest.raises(ValueError, match="El stock no puede ser negativo"):
            inventory_manager.agregar_producto(self.test_codigo, "Producto Test", 100, 150, -10)

    def test_non_numeric_purchase_price(self):
        with pytest.raises(ValueError, match="Los precios y stock deben ser numéricos"):
            inventory_manager.agregar_producto(self.test_codigo, "Producto Test", "abc", 150, 10)

    def test_non_numeric_sale_price(self):
        with pytest.raises(ValueError, match="Los precios y stock deben ser numéricos"):
            inventory_manager.agregar_producto(self.test_codigo, "Producto Test", 100, "xyz", 10)

    def test_non_numeric_stock(self):
        with pytest.raises(ValueError, match="Los precios y stock deben ser numéricos"):
            inventory_manager.agregar_producto(self.test_codigo, "Producto Test", 100, 150, "abc")

    def test_valid_product(self):
        exito, mensaje = inventory_manager.agregar_producto(
            self.test_codigo, "Producto Test", 100, 150, 10
        )
        assert exito is True
        assert "exitosamente" in mensaje.lower()

    def test_actualizar_precio_negativo(self):
        inventory_manager.agregar_producto(self.test_codigo, "Producto Test", 100, 150, 10)
        
        with pytest.raises(ValueError, match="El precio no puede ser negativo"):
            inventory_manager.actualizar_precio(self.test_codigo, -50)

    def test_actualizar_precio_no_numerico(self):
        inventory_manager.agregar_producto(self.test_codigo, "Producto Test", 100, 150, 10)
        
        with pytest.raises(ValueError, match="El precio debe ser numérico"):
            inventory_manager.actualizar_precio(self.test_codigo, "abc")

    def test_actualizar_stock_negativo(self):
        inventory_manager.agregar_producto(self.test_codigo, "Producto Test", 100, 150, 10)
        
        with pytest.raises(ValueError, match="El stock no puede ser negativo"):
            inventory_manager.actualizar_stock(self.test_codigo, -5)

    def test_actualizar_stock_no_entero(self):
        inventory_manager.agregar_producto(self.test_codigo, "Producto Test", 100, 150, 10)
        
        with pytest.raises(ValueError, match="El stock debe ser numérico"):
            inventory_manager.actualizar_stock(self.test_codigo, "abc")

    def test_aumentar_precios_negativo(self):
        inventory_manager.agregar_producto(self.test_codigo, "Producto Test", 100, 150, 10)
        
        with pytest.raises(ValueError, match="El porcentaje no puede ser negativo"):
            inventory_manager.aumentar_precios(-10)

    def test_aumentar_precios_no_numerico(self):
        inventory_manager.agregar_producto(self.test_codigo, "Producto Test", 100, 150, 10)
        
        with pytest.raises(ValueError, match="El porcentaje debe ser un número"):
            inventory_manager.aumentar_precios("abc")
