import customtkinter as ctk
import inventory_manager
from .error_dialog import show_error_popup


class UpdateProductDialog(ctk.CTkToplevel):
    def __init__(self, parent, producto, on_success=None):
        super().__init__(parent)
        self.producto = producto
        self.on_success = on_success
        self.title("Actualizar Producto")
        self.geometry("500x600")
        self.resizable(False, False)
        self.configure(fg_color="#000000")
        self.transient(parent)
        self.grab_set()

        self._setup_ui()

    def _setup_ui(self):
        main_frame = ctk.CTkFrame(self, fg_color="#000000")
        main_frame.pack(fill="both", expand=True, padx=30, pady=25)

        title_label = ctk.CTkLabel(
            main_frame,
            text="ACTUALIZAR PRODUCTO",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="white"
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 30))

        label_font = ctk.CTkFont(size=16)
        entry_font = ctk.CTkFont(size=14)

        codigo_label = ctk.CTkLabel(main_frame, text="Código:", font=label_font, text_color="white")
        codigo_label.grid(row=1, column=0, sticky="w", pady=10)
        self.codigo_entry = ctk.CTkEntry(
            main_frame,
            height=45,
            font=entry_font,
            fg_color="#333333",
            text_color="#888888",
            border_color="#333333",
            state="disabled"
        )
        self.codigo_entry.insert(0, self.producto["codigo"])
        self.codigo_entry.grid(row=1, column=1, sticky="ew", pady=10, padx=(10, 0))

        nombre_label = ctk.CTkLabel(main_frame, text="Nombre:", font=label_font, text_color="white")
        nombre_label.grid(row=2, column=0, sticky="w", pady=10)
        self.nombre_entry = ctk.CTkEntry(
            main_frame,
            height=45,
            font=entry_font,
            fg_color="#1a1a1a",
            text_color="white",
            border_color="#333333"
        )
        self.nombre_entry.insert(0, self.producto["producto"])
        self.nombre_entry.grid(row=2, column=1, sticky="ew", pady=10, padx=(10, 0))

        precio_compra_label = ctk.CTkLabel(main_frame, text="Precio Compra:", font=label_font, text_color="white")
        precio_compra_label.grid(row=3, column=0, sticky="w", pady=10)
        self.precio_compra_entry = ctk.CTkEntry(
            main_frame,
            height=45,
            font=entry_font,
            fg_color="#1a1a1a",
            text_color="white",
            border_color="#333333"
        )
        self.precio_compra_entry.insert(0, str(self.producto["precio_compra"]))
        self.precio_compra_entry.grid(row=3, column=1, sticky="ew", pady=10, padx=(10, 0))

        precio_venta_label = ctk.CTkLabel(main_frame, text="Precio Venta:", font=label_font, text_color="white")
        precio_venta_label.grid(row=4, column=0, sticky="w", pady=10)
        self.precio_venta_entry = ctk.CTkEntry(
            main_frame,
            height=45,
            font=entry_font,
            fg_color="#1a1a1a",
            text_color="white",
            border_color="#333333"
        )
        self.precio_venta_entry.insert(0, str(self.producto["precio_venta"]))
        self.precio_venta_entry.grid(row=4, column=1, sticky="ew", pady=10, padx=(10, 0))

        stock_label = ctk.CTkLabel(main_frame, text="Stock:", font=label_font, text_color="white")
        stock_label.grid(row=5, column=0, sticky="w", pady=10)
        self.stock_entry = ctk.CTkEntry(
            main_frame,
            height=45,
            font=entry_font,
            fg_color="#1a1a1a",
            text_color="white",
            border_color="#333333"
        )
        self.stock_entry.insert(0, str(self.producto["stock"]))
        self.stock_entry.grid(row=5, column=1, sticky="ew", pady=10, padx=(10, 0))

        main_frame.columnconfigure(1, weight=1)

        update_button = ctk.CTkButton(
            main_frame,
            text="ACTUALIZAR PRODUCTO",
            font=ctk.CTkFont(size=18, weight="bold"),
            height=55,
            fg_color="#2fa572",
            hover_color="#238551",
            text_color="white",
            command=self._on_update
        )
        update_button.grid(row=6, column=0, columnspan=2, sticky="ew", pady=30, ipadx=20)

    def _on_update(self):
        codigo = self.producto["codigo"]
        producto = self.nombre_entry.get()
        precio_compra = self.precio_compra_entry.get()
        precio_venta = self.precio_venta_entry.get()
        stock = self.stock_entry.get()

        try:
            exito, mensaje = inventory_manager.actualizar_producto(
                codigo, producto, precio_compra, precio_venta, stock
            )

            if exito:
                self.destroy()
                if self.on_success:
                    self.on_success()
        except ValueError as e:
            show_error_popup(self, str(e))
