import tkinter as tk
from tkinter import ttk


class ProductTable(tk.Frame):
    def __init__(self, parent, on_update=None, on_delete=None):
        super().__init__(parent)
        self.on_update = on_update
        self.on_delete = on_delete

        self._setup_ui()

    def _setup_ui(self):
        style = ttk.Style()
        style.theme_use("default")
        style.configure(
            "Treeview",
            background="#2b2b2b",
            foreground="white",
            fieldbackground="#2b2b2b",
            rowheight=35,
            font=("Helvetica", 12)
        )
        style.configure(
            "Treeview.Heading",
            background="#1f538d",
            foreground="white",
            font=("Helvetica", 12, "bold")
        )
        style.map("Treeview", background=[("selected", "#1f538d")])

        scrollbar_y = ttk.Scrollbar(self, orient="vertical")
        scrollbar_y.pack(side="right", fill="y")

        scrollbar_x = ttk.Scrollbar(self, orient="horizontal")
        scrollbar_x.pack(side="bottom", fill="x")

        self.tree = ttk.Treeview(
            self,
            columns=("codigo", "producto", "precio_compra", "precio_venta", "stock"),
            show="headings",
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )

        scrollbar_y.config(command=self.tree.yview)
        scrollbar_x.config(command=self.tree.xview)

        self.tree.heading("codigo", text="Código")
        self.tree.heading("producto", text="Nombre")
        self.tree.heading("precio_compra", text="Precio Compra")
        self.tree.heading("precio_venta", text="Precio Venta")
        self.tree.heading("stock", text="Stock")

        self.tree.column("codigo", width=100, anchor="center")
        self.tree.column("producto", width=300, anchor="w")
        self.tree.column("precio_compra", width=120, anchor="e")
        self.tree.column("precio_venta", width=120, anchor="e")
        self.tree.column("stock", width=100, anchor="center")

        self.tree.pack(fill="both", expand=True)

        self.tree.bind("<Button-3>", self._show_context_menu)
        self.tree.bind("<Double-Button-1>", self._show_context_menu)

    def insert_producto(self, producto):
        values = (
            str(producto.get("codigo", "")),
            str(producto.get("producto", "")),
            f"${producto.get('precio_compra', 0):.2f}",
            f"${producto.get('precio_venta', 0):.2f}",
            int(producto.get("stock", 0))
        )
        self.tree.insert("", "end", values=values)

    def clear(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def _show_context_menu(self, event):
        item = self.tree.identify_row(event.y)
        if not item:
            return

        self.tree.selection_set(item)
        values = self.tree.item(item)["values"]

        producto = {
            "codigo": str(values[0]),
            "producto": str(values[1]),
            "precio_compra": float(values[2].replace("$", "")),
            "precio_venta": float(values[3].replace("$", "")),
            "stock": int(values[4])
        }

        menu = tk.Menu(self, tearoff=0, font=("Helvetica", 14))
        menu.configure(bg="#2b2b2b", fg="white")
        
        if self.on_update:
            menu.add_command(label="Actualizar", font=("Helvetica", 14), command=lambda p=producto: self.on_update(p))
        if self.on_delete:
            menu.add_command(label="Eliminar", font=("Helvetica", 14), command=lambda p=producto: self.on_delete(p))
        
        menu.post(event.x_root, event.y_root)
