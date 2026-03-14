# Importación de librerías necesarias para la interfaz gráfica
import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk

# Clase que representa la interfaz gráfica del sistema
class AppTkinter:

    # Constantes de estilo
    COLOR_FONDO       = "#F0F4F8"
    COLOR_PANEL       = "#FFFFFF"
    COLOR_PRIMARIO    = "#0E6534"         
    COLOR_PELIGRO     = "#7E0000"          
    COLOR_TEXTO       = "#000E24"
    COLOR_SUBTEXTO    = "#3B3B3B"
    COLOR_BORDE       = "#CBD5E1"
    COLOR_TABLA_FILA  = "#F8FAFC"
    FUENTE_TITULO     = ("Segoe UI", 22, "bold")
    FUENTE_LABEL      = ("Segoe UI", 12)
    FUENTE_LABEL_BOLD = ("Segoe UI", 14, "bold")
    FUENTE_BOTON      = ("Segoe UI", 14, "bold")
    FUENTE_TABLA      = ("Segoe UI", 12)

    # Constructor de la aplicación
    def __init__(self, servicio):
        # Recibe la capa de servicio para interactuar con la lógica del sistema
        self.servicio = servicio

        # Creación de la ventana principal
        self.root = tk.Tk()
        self.root.title("🚘 Sistema de Gestión de Garaje 🚗")
        self.root.geometry("850x600")
        self.root.resizable(True, True)
        self.root.configure(bg=self.COLOR_FONDO)
        self.root.minsize(650, 550)

        # Construye todos los elementos de la interfaz
        self.crear_interfaz()

    # Método que inicia la ejecución de la interfaz
    def run(self):
        self.root.mainloop()

    # Método encargado de crear todos los componentes visuales
    def crear_interfaz(self):

    # Estilos
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("green.TFrame", background=self.COLOR_PRIMARIO)
        style.configure("panel.TFrame",  background=self.COLOR_PANEL)
        style.configure("Treeview",
            font=self.FUENTE_TABLA,
            rowheight=25,
            background=self.COLOR_PANEL,
            foreground=self.COLOR_TEXTO,
            fieldbackground=self.COLOR_PANEL
        )
        style.configure("Treeview.Heading",
            font=self.FUENTE_LABEL_BOLD,
            foreground=self.COLOR_PRIMARIO,
            background=self.COLOR_FONDO
        )

        # Contenedor principal
        cont = ttk.Frame(self.root, style="green.TFrame", padding=10)
        cont.pack(fill="both", expand=True)

        # Encabezado
        tk.Label(
            cont,
            text="🚗  Sistema de Gestión de Garaje",
            font=self.FUENTE_TITULO,
            background=self.COLOR_PRIMARIO,
            fg="white",
        ).pack(pady=(5, 0))

        tk.Label(
            cont,
            text="Registro y control de vehículos",
            font=self.FUENTE_LABEL_BOLD,
            background=self.COLOR_PRIMARIO,
            fg="white",
        ).pack(pady=(0, 10))

        # Variables del formulario
        self.var_placa = tk.StringVar()
        self.var_marca = tk.StringVar()
        self.var_propietario = tk.StringVar()

        # Formulario con estilos
        frm = tk.LabelFrame(
            cont,
            text=" Registrar vehículo ",
            font=self.FUENTE_LABEL_BOLD,
            bg=self.COLOR_PANEL,
            fg=self.COLOR_TEXTO,
            relief="groove",
            padx=10,
            pady=10
        )
        frm.pack(fill="x", padx=20, pady=10)

        # Columna 0 - etiquetas
        tk.Label(frm, text="Placa *",       font=self.FUENTE_LABEL, bg=self.COLOR_PANEL, fg=self.COLOR_TEXTO).grid(row=0, column=0, padx=10, pady=6, sticky="e")
        tk.Label(frm, text="Marca *",       font=self.FUENTE_LABEL, bg=self.COLOR_PANEL, fg=self.COLOR_TEXTO).grid(row=1, column=0, padx=10, pady=6, sticky="e")
        tk.Label(frm, text="Propietario *", font=self.FUENTE_LABEL, bg=self.COLOR_PANEL, fg=self.COLOR_TEXTO).grid(row=2, column=0, padx=10, pady=6, sticky="e")

        # Columna 1 - entradas
        ttk.Entry(frm, textvariable=self.var_placa,  font=self.FUENTE_LABEL,      width=30).grid(row=0, column=1, padx=10, pady=6, sticky="w")
        ttk.Entry(frm, textvariable=self.var_marca,   font=self.FUENTE_LABEL,     width=30).grid(row=1, column=1, padx=10, pady=6, sticky="w")
        ttk.Entry(frm, textvariable=self.var_propietario,  font=self.FUENTE_LABEL, width=30).grid(row=2, column=1, padx=10, pady=6, sticky="w")

        # Botones
        btn_frame = tk.Frame(frm, bg=self.COLOR_PANEL)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=10)

        ctk.CTkButton(
            btn_frame,
            text="✅  Agregar Vehículo",
            font=self.FUENTE_BOTON,
            fg_color=self.COLOR_PRIMARIO,
            hover_color="#0a4f28",
            corner_radius=20,
            command=self.agregar_vehiculo
        ).pack(side="left", padx=8)

        ctk.CTkButton(
            btn_frame,
            text="🗑  Eliminar Vehículo",
            font=self.FUENTE_BOTON,
            fg_color=self.COLOR_PELIGRO,
            hover_color="#5a0000",
            corner_radius=20,
            command=self.eliminar_vehiculo
        ).pack(side="left", padx=8)

        ctk.CTkButton(
            btn_frame,
            text="🧹  Limpiar",
            font=self.FUENTE_BOTON,
            fg_color=self.COLOR_SUBTEXTO,
            hover_color="#222222",
            corner_radius=20,
            command=self.limpiar_campos
        ).pack(side="left", padx=8)

        # Tabla
        tabla_frame = tk.LabelFrame(
            cont,
            text=" Vehículos registrados ",
            font=self.FUENTE_LABEL_BOLD,
            bg=self.COLOR_PANEL,
            fg=self.COLOR_TEXTO,
            relief="groove",
            padx=10,
            pady=10
        )
        tabla_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.tabla = ttk.Treeview(
            tabla_frame,
            columns=("placa", "marca", "propietario"),
            show="headings",
            style="Treeview"
        )

        self.tabla.heading("placa", text="🪪  Placa")
        self.tabla.heading("marca", text="🚘  Marca")
        self.tabla.heading("propietario", text="👤  Propietario")

        self.tabla.column("placa", width=150, anchor="center")
        self.tabla.column("marca", width=150, anchor="center")
        self.tabla.column("propietario", width=250, anchor="center")

        # Scrollbar
        scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)

        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    # Funciones del sistema, evento que agrega el vehículo
    def agregar_vehiculo(self):

        try:

            # Llama al servicio para registrar el vehículo
            self.servicio.agregar_vehiculo(
                self.var_placa.get(),
                self.var_marca.get(),
                self.var_propietario.get()
            )

            # Actualiza la tabla
            self.refrescar_tabla()

            # Limpia el formulario
            self.limpiar_campos()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Obtiene la placa del vehículo seleccionado en la tabla
    def get_selected_placa(self):

        sel = self.tabla.selection()

        if not sel:
            return None

        valores = self.tabla.item(sel[0], "values")

        return valores[0] if valores else None

    # Evento para eliminar un vehículo
    def eliminar_vehiculo(self):

        placa = self.get_selected_placa()

        if not placa:
            messagebox.showwarning("Atención", "Seleccione un vehículo en la tabla.")
            return

        if not messagebox.askyesno("Confirmar", f"¿Eliminar vehículo {placa}?"):
            return

        try:

            # Llama al servicio para eliminar el vehículo
            self.servicio.eliminar_vehiculo(placa)

            # Actualiza la tabla
            self.refrescar_tabla()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Actualiza la tabla con los vehículos registrados
    def refrescar_tabla(self):

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for v in self.servicio.listar_vehiculos():
            self.tabla.insert("", "end", values=(v.placa, v.marca, v.propietario))

    # Limpia los campos del formulario
    def limpiar_campos(self):

        self.var_placa.set("")
        self.var_marca.set("")
        self.var_propietario.set("")