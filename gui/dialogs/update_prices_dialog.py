import customtkinter as ctk
import inventory_manager
from .error_dialog import show_error_popup


class UpdatePricesDialog(ctk.CTkToplevel):
    def __init__(self, parent, on_success=None):
        super().__init__(parent)
        self.on_success = on_success
        self.title("Actualizar precios")
        self.geometry("400x280")
        self.resizable(False, False)
        self.configure(fg_color="#000000")
        self.transient(parent)
        self.grab_set()

        self._setup_ui()
        self._center_window()

    def _center_window(self):
        self.update_idletasks()
        x = self.winfo_screenwidth() // 2 - self.winfo_width() // 2
        y = self.winfo_screenheight() // 2 - self.winfo_height() // 2
        self.geometry(f"+{x}+{y}")

    def _setup_ui(self):
        main_frame = ctk.CTkFrame(self, fg_color="#000000")
        main_frame.pack(fill="both", expand=True, padx=30, pady=25)

        title_label = ctk.CTkLabel(
            main_frame,
            text="ACTUALIZAR PRECIOS",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="white"
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 25))

        label_font = ctk.CTkFont(size=16)
        entry_font = ctk.CTkFont(size=14)

        percentage_label = ctk.CTkLabel(
            main_frame,
            text="Porcentaje de aumento:",
            font=label_font,
            text_color="white"
        )
        percentage_label.grid(row=1, column=0, sticky="w", pady=10)

        self.percentage_entry = ctk.CTkEntry(
            main_frame,
            height=45,
            font=entry_font,
            fg_color="#1a1a1a",
            text_color="white",
            border_color="#333333",
            placeholder_text_color="#888888",
            placeholder_text="10 = aumentar precios un 10%"
        )
        self.percentage_entry.grid(row=1, column=1, sticky="ew", pady=10, padx=(10, 0))

        main_frame.columnconfigure(1, weight=1)

        button_frame = ctk.CTkFrame(main_frame, fg_color="#000000")
        button_frame.grid(row=2, column=0, columnspan=2, pady=25, sticky="ew")
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)

        apply_button = ctk.CTkButton(
            button_frame,
            text="APLICAR AUMENTO",
            font=ctk.CTkFont(size=14, weight="bold"),
            height=40,
            fg_color="#2fa572",
            hover_color="#238551",
            text_color="white",
            command=self._on_apply
        )
        apply_button.grid(row=0, column=0, padx=(0, 10), ipadx=10)

        cancel_button = ctk.CTkButton(
            button_frame,
            text="CANCELAR",
            font=ctk.CTkFont(size=14, weight="bold"),
            height=40,
            fg_color="#c93535",
            hover_color="#a12828",
            text_color="white",
            command=self.destroy
        )
        cancel_button.grid(row=0, column=1, padx=(10, 0), ipadx=10)

    def _on_apply(self):
        percentage = self.percentage_entry.get()

        if not percentage:
            return

        try:
            exito, mensaje = inventory_manager.aumentar_precios(percentage)

            if exito:
                self.destroy()
                if self.on_success:
                    self.on_success()
        except ValueError as e:
            show_error_popup(self, str(e))
