import tkinter as tk
import customtkinter as ctk


class SearchBar(tk.Frame):
    def __init__(self, parent, on_search=None):
        super().__init__(parent, bg="#000000")
        self.on_search = on_search
        self._setup_ui()

    def _setup_ui(self):
        label = tk.Label(
            self,
            text="🔍",
            font=("Helvetica", 14),
            bg="#000000",
            fg="white"
        )
        label.pack(side="left", padx=(0, 5))

        self.entry = ctk.CTkEntry(
            self,
            placeholder_text="Buscar por código o nombre...",
            width=350,
            height=40,
            font=("Helvetica", 12),
            placeholder_text_color="#888888",
            text_color="white",
            fg_color="#1a1a1a",
            border_color="#333333"
        )
        self.entry.pack(side="left", fill="x", expand=True)

        self.entry.bind("<KeyRelease>", self._on_key_release)

    def _on_key_release(self, event):
        if self.on_search:
            self.on_search(self.entry.get())
