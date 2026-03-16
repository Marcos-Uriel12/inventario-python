import customtkinter as ctk
import inventory_manager
from .error_dialog import show_error_popup


class DeleteProductDialog(ctk.CTkToplevel):
    def __init__(self, parent, producto, on_success=None):
        super().__init__(parent)
        self.producto = producto
        self.on_success = on_success
        self.title("Eliminar Producto")
        self.geometry("400x250")
        self.resizable(False, False)
        self.configure(fg_color="#000000")
        self.transient(parent)
        self.grab_set()

        self._setup_ui()

    def _setup_ui(self):
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        title_label = ctk.CTkLabel(
            main_frame,
            text="ELIMINAR PRODUCTO",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        title_label.pack(pady=(0, 20))

        info_label = ctk.CTkLabel(
            main_frame,
            text=f"¿Está seguro de eliminar el producto?\n\n"
                 f"Código: {self.producto['codigo']}\n"
                 f"Nombre: {self.producto['producto']}",
            font=ctk.CTkFont(size=12)
        )
        info_label.pack(pady=10)

        button_frame = ctk.CTkFrame(main_frame, fg_color="#000000")
        button_frame.pack(pady=20)

        yes_button = ctk.CTkButton(
            button_frame,
            text="SI",
            font=ctk.CTkFont(size=14, weight="bold"),
            width=120,
            height=45,
            fg_color="#d32f2f",
            hover_color="#b71c1c",
            text_color="white",
            command=self._on_yes
        )
        yes_button.pack(side="left", padx=10)

        no_button = ctk.CTkButton(
            button_frame,
            text="NO",
            font=ctk.CTkFont(size=14, weight="bold"),
            width=120,
            height=45,
            fg_color="#1f538d",
            hover_color="#143b6f",
            text_color="white",
            command=self.destroy
        )
        no_button.pack(side="left", padx=10)

    def _on_yes(self):
        codigo = self.producto["codigo"]

        try:
            exito, mensaje = inventory_manager.eliminar_producto(codigo)

            if exito:
                self.destroy()
                if self.on_success:
                    self.on_success()
        except ValueError as e:
            show_error_popup(self, str(e))
