import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_import_gui():
    from gui import app
    assert app is not None


def test_import_main_window():
    from gui.main_window import MainWindow
    assert MainWindow is not None


def test_import_product_table():
    from gui.components.product_table import ProductTable
    assert ProductTable is not None


def test_import_search_bar():
    from gui.components.search_bar import SearchBar
    assert SearchBar is not None


def test_import_toolbar():
    from gui.components.toolbar import Toolbar
    assert Toolbar is not None


def test_import_add_product_dialog():
    from gui.dialogs.add_product_dialog import AddProductDialog
    assert AddProductDialog is not None


def test_import_update_product_dialog():
    from gui.dialogs.update_product_dialog import UpdateProductDialog
    assert UpdateProductDialog is not None


def test_import_delete_product_dialog():
    from gui.dialogs.delete_product_dialog import DeleteProductDialog
    assert DeleteProductDialog is not None
