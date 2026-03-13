import tkinter as tk
from tkinter import ttk, messagebox


class AppTkinter:

    def __init__(self, servicio):
        self.servicio = servicio

        self.root = tk.Tk()
        self.root.title("Sistema de Gestión de Garaje")
        self.root.geometry("600x400")

        self.crear_interfaz()

    def run(self):
        self.root.mainloop()

    def crear_interfaz(self):

        cont = ttk.Frame(self.root, padding=10)
        cont.pack(fill="both", expand=True)

        # VARIABLES
        self.var_placa = tk.StringVar()
        self.var_marca = tk.StringVar()
        self.var_propietario = tk.StringVar()

        # FORMULARIO
        frm = ttk.LabelFrame(cont, text="Registrar Vehículo", padding=10)
        frm.pack(fill="x", pady=10)

        ttk.Label(frm, text="Placa").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(frm, textvariable=self.var_placa).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frm, text="Marca").grid(row=1, column=0, padx=5, pady=5)
        ttk.Entry(frm, textvariable=self.var_marca).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frm, text="Propietario").grid(row=2, column=0, padx=5, pady=5)
        ttk.Entry(frm, textvariable=self.var_propietario).grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(frm, text="Agregar Vehículo", command=self.agregar_vehiculo).grid(row=3, column=0, pady=10)

        ttk.Button(frm, text="Limpiar", command=self.limpiar_campos).grid(row=3, column=1, pady=10)

        ttk.Button(frm, text="Agregar Vehículo", command=self.agregar_vehiculo).grid(row=3, column=0, pady=10)

        ttk.Button(frm, text="Eliminar Vehículo", command=self.eliminar_vehiculo).grid(row=3, column=1, pady=10)

        ttk.Button(frm, text="Limpiar", command=self.limpiar_campos).grid(row=3, column=2, pady=10)

        # TABLA
        tabla_frame = ttk.LabelFrame(cont, text="Vehículos Registrados", padding=10)
        tabla_frame.pack(fill="both", expand=True)

        self.tabla = ttk.Treeview(
            tabla_frame,
            columns=("placa", "marca", "propietario"),
            show="headings"
        )

        self.tabla.heading("placa", text="Placa")
        self.tabla.heading("marca", text="Marca")
        self.tabla.heading("propietario", text="Propietario")

        self.tabla.pack(fill="both", expand=True)

    # FUNCIONES
    def agregar_vehiculo(self):

        try:

            self.servicio.agregar_vehiculo(
                self.var_placa.get(),
                self.var_marca.get(),
                self.var_propietario.get()
            )

            self.refrescar_tabla()
            self.limpiar_campos()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def get_selected_placa(self):

        sel = self.tabla.selection()

        if not sel:
            return None

        valores = self.tabla.item(sel[0], "values")

        return valores[0] if valores else None

    def eliminar_vehiculo(self):

        placa = self.get_selected_placa()

        if not placa:
            messagebox.showwarning("Atención", "Seleccione un vehículo en la tabla.")
            return

        if not messagebox.askyesno("Confirmar", f"¿Eliminar vehículo {placa}?"):
            return

        try:

            self.servicio.eliminar_vehiculo(placa)

            self.refrescar_tabla()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def refrescar_tabla(self):

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for v in self.servicio.listar_vehiculos():
            self.tabla.insert("", "end", values=(v.placa, v.marca, v.propietario))

    def limpiar_campos(self):

        self.var_placa.set("")
        self.var_marca.set("")
        self.var_propietario.set("")