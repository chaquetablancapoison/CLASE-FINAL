import tkinter as tk
from tkinter import ttk, messagebox

from services.user_service import UserService


class AppWindow(tk.Tk):

    def __init__(self, service: UserService) -> None:
        super().__init__()

        self.service = service

        self.title("Tkinter con POO + Capas")
        self.geometry("720x560")
        self.resizable(False, False)

        self.create_widgets()
        self.render_data_table()

    def create_widgets(self):

        ttk.Label(
            self,
            text="Registro de Usuarios",
            font=("Arial", 18, "bold")
        ).grid(
            row=0,
            column=0,
            columnspan=4,
            padx=10,
            pady=(20, 15)
        )

        ttk.Label(
            self,
            text="Nombre:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="e"
        )

        self.entry_fname = ttk.Entry(self, width=25)
        self.entry_fname.grid(
            row=1,
            column=1,
            padx=10,
            pady=10,
            sticky="w"
        )

        ttk.Label(
            self,
            text="Apellido:"
        ).grid(
            row=1,
            column=2,
            padx=10,
            pady=10,
            sticky="e"
        )

        self.entry_lname = ttk.Entry(self, width=25)
        self.entry_lname.grid(
            row=1,
            column=3,
            padx=10,
            pady=10,
            sticky="w"
        )

        ttk.Label(
            self,
            text="Edad:"
        ).grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
            sticky="e"
        )

        self.entry_age = ttk.Entry(self, width=25)
        self.entry_age.grid(
            row=2,
            column=1,
            padx=10,
            pady=10,
            sticky="w"
        )

        ttk.Label(
            self,
            text="Correo:"
        ).grid(
            row=2,
            column=2,
            padx=10,
            pady=10,
            sticky="e"
        )

        self.entry_email = ttk.Entry(self, width=25)
        self.entry_email.grid(
            row=2,
            column=3,
            padx=10,
            pady=10,
            sticky="w"
        )
        
        ttk.Button(
            self,
            text="Ingresar usuario",
            command=self.create_new_user
        ).grid(
            row=3,
            column=0,
            columnspan=4,
            padx=10,
            pady=20
        )

        self.tree = ttk.Treeview(
            self,
            columns=("fname", "lname", "age", "email"),
            show="headings",
            height=12
        )

        self.tree.heading("fname", text="Nombre")
        self.tree.heading("lname", text="Apellido")
        self.tree.heading("age", text="Edad")
        self.tree.heading("email", text="Email")

        self.tree.column("fname", width=130, anchor="center")
        self.tree.column("lname", width=130, anchor="center")
        self.tree.column("age", width=70, anchor="center")
        self.tree.column("email", width=300, anchor="center")

        self.tree.grid(
            row=4,
            column=0,
            columnspan=4,
            padx=15,
            pady=(5, 20),
            sticky="nsew"
        )

    def create_new_user(self):

        fname = self.entry_fname.get().strip()
        lname = self.entry_lname.get().strip()
        age_text = self.entry_age.get().strip()
        email = self.entry_email.get().strip()

        if not fname or not lname or not age_text or not email:
            messagebox.showwarning(
                "Campos incompletos",
                "Completa todos los campos."
            )
            return

        try:
            age = int(age_text)
        except ValueError:
            messagebox.showerror(
                "Edad inválida",
                "La edad debe ser un número entero."
            )
            return

        self.service.create_one(fname, lname, age, email)

        self.render_data_table()
        self.clear_entries()

    def clear_entries(self):

        self.entry_fname.delete(0, tk.END)
        self.entry_lname.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

        self.entry_fname.focus()

    def render_data_table(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        users = self.service.find_all()

        for user in users:
            self.tree.insert(
                "",
                "end",
                values=(
                    user.fname,
                    user.lname,
                    user.age,
                    user.email
                )
            )


if __name__ == "__main__":
    pass
