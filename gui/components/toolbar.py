import tkinter as tk
import customtkinter as ctk


class Toolbar(tk.Frame):
    def __init__(self, parent, on_add_product=None, on_refresh=None, on_sort=None, on_update_prices=None):
        super().__init__(parent, bg="#000000")
        self.on_add_product = on_add_product
        self.on_refresh = on_refresh
        self.on_sort = on_sort
        self.on_update_prices = on_update_prices
        self._setup_ui()

    def _setup_ui(self):
        self.add_button = ctk.CTkButton(
            self,
            text="+ Agregar producto",
            height=45,
            font=("Helvetica", 12, "bold"),
            fg_color="#2fa572",
            hover_color="#238551",
            text_color="white",
            command=self._on_add_click
        )
        self.add_button.pack(side="left", padx=(0, 15))

        sort_options = [
            "Ordenar por...",
            "Precio venta mayor",
            "Precio venta menor",
            "Stock mayor",
            "Stock menor"
        ]
        self.sort_var = tk.StringVar(value="Ordenar")

        self.sort_menu = ctk.CTkOptionMenu(
            self,
            values=sort_options,
            variable=self.sort_var,
            height=45,
            font=("Helvetica", 11),
            command=self._on_sort_change
        )
        self.sort_menu.pack(side="left", padx=5)

        self.update_prices_button = ctk.CTkButton(
            self,
            text="Actualizar precios",
            height=45,
            font=("Helvetica", 11),
            fg_color="#e6a700",
            hover_color="#b38300",
            text_color="white",
            command=self._on_update_prices_click
        )
        self.update_prices_button.pack(side="left", padx=5)

        self.refresh_button = ctk.CTkButton(
            self,
            text="↻ Actualizar",
            height=45,
            font=("Helvetica", 11),
            fg_color="#1f538d",
            hover_color="#143b6f",
            text_color="white",
            command=self._on_refresh_click
        )
        self.refresh_button.pack(side="left", padx=5)

    def _on_add_click(self):
        if self.on_add_product:
            self.on_add_product()

    def _on_update_prices_click(self):
        if self.on_update_prices:
            self.on_update_prices()

    def _on_refresh_click(self):
        if self.on_refresh:
            self.on_refresh()

    def _on_sort_change(self, value):
        if value == "Ordenar por...":
            return
        sort_map = {
            "Precio venta mayor": "precio_venta_mayor",
            "Precio venta menor": "precio_venta_menor",
            "Stock mayor": "stock_mayor",
            "Stock menor": "stock_menor"
        }
        if self.on_sort:
            self.on_sort(sort_map.get(value))
