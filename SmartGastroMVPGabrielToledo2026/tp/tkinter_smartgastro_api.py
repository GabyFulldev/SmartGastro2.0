import tkinter as tk
from tkinter import messagebox
import requests

API_URL = "http://127.0.0.1:5000/api/productos"


class SmartGastroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SmartGastro con API Flask")
        self.root.geometry("650x500")

        tk.Label(root, text="SMARTGASTRO - API REST", font=("Arial", 18, "bold")).pack(pady=10)

        frame = tk.Frame(root)
        frame.pack(pady=10)

        tk.Label(frame, text="ID").grid(row=0, column=0)
        tk.Label(frame, text="Nombre").grid(row=1, column=0)
        tk.Label(frame, text="Precio").grid(row=2, column=0)
        tk.Label(frame, text="Stock").grid(row=3, column=0)

        self.entry_id = tk.Entry(frame)
        self.entry_nombre = tk.Entry(frame)
        self.entry_precio = tk.Entry(frame)
        self.entry_stock = tk.Entry(frame)

        self.entry_id.grid(row=0, column=1)
        self.entry_nombre.grid(row=1, column=1)
        self.entry_precio.grid(row=2, column=1)
        self.entry_stock.grid(row=3, column=1)

        tk.Button(root, text="Agregar producto vía POST", command=self.agregar_producto_api).pack(pady=5)
        tk.Button(root, text="Cargar inventario vía GET", command=self.cargar_productos_api).pack(pady=5)

        self.lista = tk.Listbox(root, width=80, height=15)
        self.lista.pack(pady=15)

    def agregar_producto_api(self):
        try:
            producto = {
                "id": int(self.entry_id.get()),
                "nombre": self.entry_nombre.get(),
                "precio": float(self.entry_precio.get()),
                "stock": int(self.entry_stock.get())
            }

            respuesta = requests.post(API_URL, json=producto)

            if respuesta.status_code == 201:
                messagebox.showinfo("Éxito", "Producto agregado usando POST")
                self.limpiar_campos()
                self.cargar_productos_api()
            else:
                messagebox.showerror("Error", "No se pudo agregar el producto")

        except ValueError:
            messagebox.showerror("Error", "Datos inválidos")
        except requests.exceptions.ConnectionError:
            messagebox.showerror("Error", "La API Flask no está ejecutándose")

    def cargar_productos_api(self):
        try:
            respuesta = requests.get(API_URL)

            if respuesta.status_code == 200:
                productos = respuesta.json()

                self.lista.delete(0, tk.END)

                for p in productos:
                    texto = f"ID: {p['id']} | Nombre: {p['nombre']} | Precio: ${p['precio']} | Stock: {p['stock']}"
                    self.lista.insert(tk.END, texto)

            else:
                messagebox.showerror("Error", "No se pudo obtener el inventario")

        except requests.exceptions.ConnectionError:
            messagebox.showerror("Error", "La API Flask no está ejecutándose")

    def limpiar_campos(self):
        self.entry_id.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_stock.delete(0, tk.END)


root = tk.Tk()
app = SmartGastroApp(root)
root.mainloop()