from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class Fenetre_Details:
    def __init__(self, root):
        self.root = root
        self.root.title("SYSTEME DE GESTION D'HOTEL")
        self.root.geometry("1128x520+230+220")
        self.root.configure(bg="#f0f0f0")
        self.btnUpdate = StringVar()
        self.btnDelete = StringVar()

        # Titre
        lbl_title = Label(self.root, text="GESTION DES CHAMBRES", font=("Helvetica", 24, "bold"), bg="black", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1128, height=50)



        # Label Frame pour ajouter une chambre
        labelframeleft = LabelFrame(self.root, relief=RIDGE, text="Ajouter une chambre", font=("Helvetica", 14, "bold"), padx=2, bg="#f0f0f0")
        labelframeleft.place(x=5, y=60, width=540, height=350)

        # Numéro de la chambre
        lbl_NumeroChambre = Label(labelframeleft, text="Numéro de la chambre :", font=("Arial", 12, "bold"), padx=2, pady=6, bg="#f0f0f0")
        self.var_Numero_de_la_chambre = StringVar()
        lbl_NumeroChambre.grid(row=0, column=0, sticky=W)
        entry_NumeroChambre = ttk.Entry(labelframeleft, textvariable=self.var_Numero_de_la_chambre, width=20, font=("Arial", 12))
        entry_NumeroChambre.grid(row=0, column=1, sticky=W)


        # Type de la chambre
        lbl_Type_chambre = Label(labelframeleft, text="Type de la chambre :", font=("Arial", 12, "bold"), padx=2, pady=6, bg="#f0f0f0")
        self.var_Type_de_la_chambre = StringVar()
        lbl_Type_chambre.grid(row=2, column=0, sticky=W)
        entry_Type_chambre = ttk.Entry(labelframeleft, textvariable=self.var_Type_de_la_chambre, width=20, font=("Arial", 12))
        entry_Type_chambre.grid(row=2, column=1, sticky=W)

        # Boutons CRUD
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE, bg="#f0f0f0")
        btn_frame.place(x=0, y=200, width=390, height=40)

        btn_style = {"font": ("Arial", 12, "bold"), "width": 9, "cursor": "hand1"}
        btnAdd = Button(btn_frame, command=self.add_data, text="Ajouter", bg="green", fg="white", **btn_style)
        btnAdd.grid(row=0, column=0, padx=1)
        self.btnUpdate = Button(btn_frame, command=self.update, text="Modifier", bg="purple", fg="white", **btn_style)
        self.btnUpdate.grid(row=0, column=1, padx=1)
        self.btnDelete = Button(btn_frame, command=self.mDelete, text="Supprimer", bg="red", fg="white", **btn_style)
        self.btnDelete.grid(row=0, column=2, padx=1)
        btnReset = Button(btn_frame, command=self.reset, text="Reset", bg="black", fg="white", **btn_style)
        btnReset.grid(row=0, column=3, padx=1)

        self.btnUpdate.config(state=DISABLED, bg="grey")
        self.btnDelete.config(state=DISABLED, bg="grey")


        # Table pour afficher les chambres
        Table_Frame = LabelFrame(self.root, relief=RIDGE, text="Affichage des chambres", font=("Helvetica", 14, "bold"), padx=2, bg="#f0f0f0")
        Table_Frame.place(x=550, y=60, width=570, height=350)

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)
        self.room_table = ttk.Treeview(Table_Frame, columns=("Numero_de_la_chambre", "Type_de_la_chambre"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Numero_de_la_chambre", text="Numéro de la chambre")
        self.room_table.heading("Type_de_la_chambre", text="Type de la chambre")

        self.room_table["show"] = "headings"

        self.room_table.column("Numero_de_la_chambre", width=100)
        self.room_table.column("Type_de_la_chambre", width=100)
        self.room_table.pack(fill=BOTH, expand=1)

        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # Ajouter des données
    def add_data(self):
        if  self.var_Type_de_la_chambre.get() == "":
            messagebox.showerror("Erreur", "Veuillez remplir les champs", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO details VALUES(%s,%s)", (
                    self.var_Numero_de_la_chambre.get(),
                    self.var_Type_de_la_chambre.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Chambre ajoutée avec succès", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Attention", f"Veuillez vérifier l'erreur : {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM details")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
        for i in rows:
            self.room_table.insert("", END, values=i)
        conn.commit()
        conn.close()

    # Afficher les données dans les champs d'entrée
    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_Numero_de_la_chambre.set(row[0])
        self.var_Type_de_la_chambre.set(row[1])

        self.btnUpdate.config(state=NORMAL, bg="purple")
        self.btnDelete.config(state=NORMAL, bg="red")

    # Modifier les données
    def update(self):
        if self.var_Type_de_la_chambre.get() == "":
            messagebox.showerror("Erreur", "Veuillez remplir le numéro", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE details SET Type_de_la_chambre=%s WHERE Numero_de_la_chambre=%s", (
                    self.var_Type_de_la_chambre.get(),
                    self.var_Numero_de_la_chambre.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Modification", "La modification a réussi", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Attention", f"Veuillez vérifier l'erreur : {str(es)}", parent=self.root)

    # Supprimer les données
    def mDelete(self):
        mDelete = messagebox.askyesno("Système de Gestion d'Hotel", "Voulez-vous supprimer cette chambre ?", parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            query = "DELETE FROM details WHERE Numero_de_la_chambre=%s"
            value = (self.var_Numero_de_la_chambre.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    # Vider les champs
    def reset(self):
        self.var_Numero_de_la_chambre.set("")
        self.var_Type_de_la_chambre.set("")

if __name__ == "__main__":
    root = Tk()
    obj = Fenetre_Details(root)
    root.mainloop()
