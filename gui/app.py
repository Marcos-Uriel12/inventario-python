import customtkinter as ctk
from .main_window import MainWindow


def launch():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    app = ctk.CTk()
    app.title("Sistema de Inventario")
    app.geometry("1200x700")
    app.configure(fg_color="#000000")

    main_window = MainWindow(app)
    main_window.pack(fill="both", expand=True)

    app.mainloop()
