from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from ok import Mail
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



class Fenetre_chambre:
    def __init__(self, root):
        self.root = root
        self.root.title("SYSTEME DE GESTION D'HOTEL")
        self.root.geometry("1128x520+230+220")

        # =====variable=====
        self.var_Id = IntVar()
        self.var_contact = StringVar()
        self.var_Date_Entree = StringVar()
        self.var_Date_Sortie = StringVar()
        self.var_Chambre = StringVar()
        self.var_Chambre_Utiliser = StringVar()
        self.var_Diner = StringVar()
        self.var_NombreDeJour = StringVar()
        self.var_Fermer = StringVar()
        self.var_PourBoire = StringVar()
        self.var_Montant = StringVar()
        self.var_Total = StringVar()

        # =========Titre ambony eo iny===========
        lbl_title = Label(self.root, text="RESERVER UNE CHAMBRE", font=("times new roman", 18, "bold"), bg="black",
                          fg="WHITE", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # =========label ===========
        labelframeleft = LabelFrame(self.root, relief=RIDGE, text="Information de la chambre",
                                    font=("times new roman", 12, "bold"), padx=2, )
        labelframeleft.place(x=5, y=50, width=400, height=490)

        # =========label et Date_Entree (ttk io mampisy style mirehitsy bleu amin'ny label io) ===========

        # Contact
        lbl_cust_contact = Label(labelframeleft, text="Contact Client :", font=("arial", 10, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)
        entry_contact = ttk.Entry(labelframeleft, textvariable=self.var_contact, width=20, font=("arial", 10, "bold"))
        entry_contact.grid(row=0, column=1, sticky=W)

        # boutton mampiseho donne reny
        btnfetchData = Button(labelframeleft, command=self.Fetch_Contact, text="Afficher", font=("arial", 8, "bold"),
                              bg="gray", fg="white", width=9)
        btnfetchData.place(x=280, y=4)

        # date d'entre
        # check_in_date=Label(labelframeleft,text="Date d'entré :",font=("arial",10,"bold"),padx=2,pady=6)
        # check_in_date.grid(row=1,column=0,sticky=W)
        # txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_Date_Entree,width=29,font=("arial",10,"bold"))
        # txtcheck_in_date.grid(row=1,column=1)
        check_in_date = ttk.Label(labelframeleft, text="Date d'entrée :", font=("arial", 10, "bold"))
        check_in_date.grid(row=1, column=0, sticky=tk.W, padx=2, pady=6)

        txtcheck_in_date = DateEntry(labelframeleft, textvariable=self.var_Date_Entree, width=29,
                                     font=("arial", 10, "bold"), date_pattern='dd/mm/yyyy')
        txtcheck_in_date.grid(row=1, column=1)



        # type de chambre
        lbl_roomtype = Label(labelframeleft, text="Type de chambre :", font=("arial", 10, "bold"), padx=2, pady=6)
        lbl_roomtype.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT Type_de_la_chambre FROM details")
        id = my_cursor.fetchall()

        combo_RoomType = ttk.Combobox(labelframeleft, font=("arial", 10, "bold"), textvariable=self.var_Chambre,
                                      width=27, state="readonly")
        combo_RoomType["value"] = id
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        # Chambre_Utiliser
        lblRoomChambre_Utiliser = Label(labelframeleft, text="Chambre Utiliser :", font=("arial", 10, "bold"), padx=2,
                                        pady=6)
        lblRoomChambre_Utiliser.grid(row=4, column=0, sticky=W)
        # txtChambre_Utiliser=ttk.Entry(labelframeleft,width=29,textvariable=self.var_Chambre_Utiliser,font=("arial",10,"bold"))
        # txtChambre_Utiliser.grid(row=4,column=1)

        conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT Numero_de_la_chambre FROM details")
        rows = my_cursor.fetchall()

        combo_RoomNo = ttk.Combobox(labelframeleft, font=("arial", 10, "bold"), textvariable=self.var_Chambre_Utiliser,
                                    width=27, state="readonly")
        combo_RoomNo["value"] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)

        # diner
        lbldiner = Label(labelframeleft, text="Diner (Repas):", font=("arial", 10, "bold"), padx=2, pady=6)
        lbldiner.grid(row=5, column=0, sticky=W)

        combo_diner = ttk.Combobox(labelframeleft, font=("arial", 10, "bold"), textvariable=self.var_Diner, width=27,
                                   state="readonly")
        combo_diner["value"] = ("Pizza", "spaghetti", "Sushi", "Soupe")
        combo_diner.current(0)
        combo_diner.grid(row=5, column=1)

        # NombreDeJour
        lblNombreDeJour = Label(labelframeleft, text="Nombre de Jour :", font=("arial", 10, "bold"), padx=2, pady=6)
        lblNombreDeJour.grid(row=6, column=0, sticky=W)
        NombreDeJour = ttk.Entry(labelframeleft, width=29, textvariable=self.var_NombreDeJour,
                                 font=("arial", 10, "bold"))
        NombreDeJour.grid(row=6, column=1)

        # ======== boutton CRUD reny==========
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=390, height=40)

        btnAdd = Button(btn_frame, command=self.add_data, text="Ajouter", font=("arial", 12, "bold"), bg="green",
                        fg="white", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, command=self.update, text="Modifier", font=("arial", 11, "bold"), bg="purple",
                           fg="white", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, command=self.mDelete, text="Supprimer", font=("arial", 11, "bold"), bg="red",
                           fg="white", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Vider", command=self.reset, font=("arial", 12, "bold"), bg="black",
                          fg="white", width=9)
        btnReset.grid(row=0, column=3, padx=1)

        # photo a droite
        img3 = Image.open(r"./image/VueDEhors.jpg")
        img3 = img3.resize((450, 250), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimag = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimag.place(x=750, y=55, width=450, height=250)

        # ======== Table amin'ny CRUD==========
        # =========label ===========
        Table_Frame = LabelFrame(self.root, relief=RIDGE, text="Table des Informations des Chambres & Recherche",
                                 font=("times new roman", 12, "bold"), padx=2, )
        Table_Frame.place(x=410, y=280, width=800, height=260)

        # Recherche
        label_searchBy = Label(Table_Frame, text="Recherche par : ", font=("arial", 10, "bold"), bg="gray", fg="white")
        label_searchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(Table_Frame, font=("arial", 10, "bold"), textvariable=self.search_var, width=24,
                                    state="readonly")
        combo_search["value"] = ("Contact", "Chambre_Utiliser")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        entry_search = ttk.Entry(Table_Frame, width=24, textvariable=self.txt_search, font=("arial", 10, "bold"))
        entry_search.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, command=self.search, text="Recherche", font=("arial", 10, "bold"), bg="green",
                           fg="white", width=9)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, command=self.fetch_data, text="Tous afficher", font=("arial", 10, "bold"),
                            bg="purple", fg="white", width=9)
        btnShowAll.grid(row=0, column=4, padx=1)

        # =====Afficher la table===========
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=850, height=160)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table, columns=("Id","Contact", "Date_Entree", "Chambre", "Chambre_Utiliser", "Diner", "NombreDeJour",
        "Montant", "Total"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Id", text="Id")
        self.room_table.heading("Contact", text="Contact")
        self.room_table.heading("Date_Entree", text="Date_Entree")
        self.room_table.heading("Chambre", text="Chambre")
        self.room_table.heading("Chambre_Utiliser", text="Chambre_Utiliser")
        self.room_table.heading("Diner", text="Diner")
        self.room_table.heading("NombreDeJour", text="NombreDeJour")


        self.room_table["show"] = "headings"

        self.room_table.column("Id", width=100)
        self.room_table.column("Contact", width=100)
        self.room_table.column("Date_Entree", width=100)
        self.room_table.column("Chambre", width=100)
        self.room_table.column("Chambre_Utiliser", width=100)
        self.room_table.column("Diner", width=100)
        self.room_table.column("NombreDeJour", width=100)

        self.room_table.pack(fill=BOTH, expand=1)

        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # l'ajout des donnees
    def add_data(self):
        if self.var_contact.get() == "" or self.var_Date_Entree.get() == "":
            messagebox.showerror("Erreur", "Veuillez remplir les champs", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                my_cursor = conn.cursor()
                # Assurez-vous que l'ordre des colonnes correspond à celui de votre table 'chambre'
                my_cursor.execute(
                    "INSERT INTO chambre (Contact, Date_Entree, Chambre, Chambre_Utiliser, Diner, NombreDeJour) VALUES (%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_contact.get(),
                        self.var_Date_Entree.get(),
                        self.var_Chambre.get(),
                        self.var_Chambre_Utiliser.get(),
                        self.var_Diner.get(),
                        self.var_NombreDeJour.get()
                    ))
                conn.commit()
                self.fetch_data()
                messagebox.showinfo("Success", "L'Addition a été ajoutée avec succès", parent=self.root)

                # pour le email
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                my_cursor = conn.cursor()
                query = ("SELECT Email FROM client WHERE Numero=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                message = """
                        Bonjour,

                        Nous sommes ravis de vous accueillir à {}. Merci d'avoir choisi de séjourner chez nous pour votre prochain voyage à {}.

                        Votre réservation pour {} a été confirmée. Nous mettons tout en œuvre pour rendre votre séjour agréable et mémorable.

                        À votre arrivée, notre équipe sera à votre disposition pour répondre à vos besoins et vous fournir toutes les informations nécessaires pour profiter pleinement de votre séjour. N'hésitez pas à nous contacter si vous avez des préférences particulières ou des questions avant votre arrivée.

                        Nous vous souhaitons un voyage sûr et confortable jusqu'à {}. Nous avons hâte de vous accueillir et de faire de votre séjour une expérience exceptionnelle.

                        Cordialement,
                        L'équipe de {}
                        """.format("AMAZONE TULEAR", row[0], self.var_Date_Entree, row[0],
                                   "AMAZONE")

                app = Mail()
                app.envoyer_email(row[0], message)



            except Exception as es:
                messagebox.showwarning("Attention", f"Erreur lors de l'ajout : {str(es)}", parent=self.root)

    # affichage des donnes sur la table
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM chambre")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
        for i in rows:
            self.room_table.insert("", END, values=i)
        conn.commit()
        conn.close()

    # affichage donnees fa amin'ny table eo ho amin'ny champ eo
    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]
        self.var_Id.set(row[0])
        self.var_contact.set(row[1])
        self.var_Date_Entree.set(row[2])
        self.var_Chambre.set(row[3])
        self.var_Chambre_Utiliser.set(row[4])
        self.var_Diner.set(row[5])
        self.var_NombreDeJour.set(row[6])

    # toy ty modification koa lahy eeeee
    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Erreur", "Veuillez remplir le numéro", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "UPDATE chambre SET Date_Entree=%s, Chambre=%s, Chambre_Utiliser=%s, Diner=%s, NombreDeJour=%s WHERE Contact=%s",
                    (
                        self.var_Date_Entree.get(),
                        self.var_Chambre.get(),
                        self.var_Chambre_Utiliser.get(),
                        self.var_Diner.get(),
                        self.var_NombreDeJour.get(),
                        self.var_contact.get()
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()

                # pour le email
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                my_cursor = conn.cursor()
                query = ("SELECT Email FROM client WHERE Numero=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                message = """
                       Bonjour,

                       Nous vous informons que votre réservation à {} a été modifiée.

                
                       Si vous avez des questions ou des préoccupations, n'hésitez pas à nous contacter.

                       Cordialement,
                       L'équipe de {}
                       """.format("AMAZONE", "AMAZONE TULEAR")

                app = Mail()
                app.envoyer_email(row[0], message)

                messagebox.showinfo("Modification", "La modification a réussi", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Attention", f"Veuillez vérifier l'erreur : {str(es)}", parent=self.root)

        # supprimer toy lahy

    def mDelete(self):
        mDelete = messagebox.askyesno("Système Gestion d'Hôtel", "Voulez-vous supprimer ce client ?", parent=self.root)
        if mDelete:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                my_cursor = conn.cursor()
                query = "DELETE FROM chambre WHERE Contact=%s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                conn.commit()
                self.fetch_data()  # Met à jour l'affichage après la suppression
                conn.close()
                messagebox.showinfo("Suppression", "La suppression a réussi", parent=self.root)

                # pour le email
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                my_cursor = conn.cursor()
                query = ("SELECT Email FROM client WHERE Numero=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                message = """
                    Bonjour,

                    Nous vous informons que votre réservation à {} a été annulée pour la raison suivante : {}.

                    Nous sommes désolés pour tout inconvénient que cela pourrait vous causer. Veuillez nous contacter si vous avez des questions ou si nous pouvons vous aider d'une autre manière.

                    Cordialement,
                    L'équipe de {}
                    """.format("AMAZONE", "PAR VOUS", "AMAZONE")

                app = Mail()
                app.envoyer_email(row[0], message)

            except Exception as es:
                messagebox.showwarning("Attention", f"Erreur lors de la suppression : {str(es)}", parent=self.root)
        else:
            return

    def reset(self):
        self.var_contact.set("")
        self.var_Date_Entree.set("")
        self.var_Date_Sortie.set("")
        self.var_Chambre.set("")
        self.var_Chambre_Utiliser.set("")
        self.var_Diner.set("")
        self.var_NombreDeJour.set("")
        self.var_PourBoire.set("")
        self.var_Montant.set("")
        self.var_Total.set("")

        # ========== tous les donnees==========

    def Fetch_Contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Erreur", "Veuillez remplir le contact", parent=self.root)
        else:
            # pour le Nom
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            query = ("SELECT Nom FROM client WHERE Numero=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Erreur", "Ce contact n'est pas trouvé", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataFrame = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataFrame.place(x=415, y=60, width=320, height=200)

                lblName = Label(showDataFrame, text="Nom :", font=("arial", 12, "bold"))
                lblName.place(x=0, y=0)

                lbl = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=0)

                # pour le Prenom
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                my_cursor = conn.cursor()
                query = ("SELECT Prenom FROM client WHERE Numero=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGenre = Label(showDataFrame, text="Prenom :", font=("arial", 12, "bold"))
                lblGenre.place(x=0, y=30)

                lbl2 = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=30)

                # pour le Genre
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                my_cursor = conn.cursor()
                query = ("SELECT Genre FROM client WHERE Numero=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGenre = Label(showDataFrame, text="Genre :", font=("arial", 12, "bold"))
                lblGenre.place(x=0, y=60)

                lbl2 = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=60)

                # pour le email
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                my_cursor = conn.cursor()
                query = ("SELECT Email FROM client WHERE Numero=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGenre = Label(showDataFrame, text="Email :", font=("arial", 12, "bold"))
                lblGenre.place(x=0, y=90)

                lbl2 = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=90)

                # pour le Nationalite
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                my_cursor = conn.cursor()
                query = ("SELECT Nationalite FROM client WHERE Numero=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGenre = Label(showDataFrame, text="Nationalité:", font=("arial", 12, "bold"))
                lblGenre.place(x=0, y=120)

                lbl2 = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=120)

                # pour l'Addresse
                conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
                my_cursor = conn.cursor()
                query = ("SELECT Addresse FROM client WHERE Numero=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGenre = Label(showDataFrame, text="Addresse :", font=("arial", 12, "bold"))
                lblGenre.place(x=0, y=150)

                lbl2 = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=150)

        # recherche iny koa toy

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
        my_cursor = conn.cursor()

        my_cursor.execute("SELECT * FROM chambre WHERE " + str(self.search_var.get()) + " LIKE '%" + str(
            self.txt_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def total(self):
        inDate = self.var_Date_Entree.get()
        outDate = self.var_Date_Sortie.get()
        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
        self.var_NombreDeJour.set(abs(outDate - inDate).days)

        if (self.var_Diner.get() == "Pizza" and self.var_Chambre.get() == "Luxe"):
            q1 = float(3000)
            q2 = float(30000)
            q3 = float(self.var_NombreDeJour.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Ar " + str("%.2f" % ((q5) * 0.09))
            ST = "Ar " + str("%.2f" % ((q5)))
            TT = "Ar " + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_PourBoire.set(Tax)
            self.var_Montant.set(ST)
            self.var_Total.set(TT)

        elif (self.var_Diner.get() == "Pizza" and self.var_Chambre.get() == "Double"):
            q1 = float(3000)
            q2 = float(25000)
            q3 = float(self.var_NombreDeJour.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Ar " + str("%.2f" % ((q5) * 0.09))
            ST = "Ar " + str("%.2f" % ((q5)))
            TT = "Ar " + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_PourBoire.set(Tax)
            self.var_Montant.set(ST)
            self.var_Total.set(TT)

        elif (self.var_Diner.get() == "Pizza" and self.var_Chambre.get() == "Solitaire"):
            q1 = float(3000)
            q2 = float(20000)
            q3 = float(self.var_NombreDeJour.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Ar " + str("%.2f" % ((q5) * 0.09))
            ST = "Ar " + str("%.2f" % ((q5)))
            TT = "Ar " + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_PourBoire.set(Tax)
            self.var_Montant.set(ST)
            self.var_Total.set(TT)

        elif (self.var_Diner.get() == "Spaghetti" and self.var_Chambre.get() == "Solitaire"):
            q1 = float(5000)
            q2 = float(10000)
            q3 = float(self.var_NombreDeJour.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Ar " + str("%.2f" % ((q5) * 0.09))
            ST = "Ar " + str("%.2f" % ((q5)))
            TT = "Ar " + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_PourBoire.set(Tax)
            self.var_Montant.set(ST)
            self.var_Total.set(TT)

        elif (self.var_Diner.get() == "Spaghetti" and self.var_Chambre.get() == "Double"):
            q1 = float(5000)
            q2 = float(15000)
            q3 = float(self.var_NombreDeJour.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Ar " + str("%.2f" % ((q5) * 0.09))
            ST = "Ar " + str("%.2f" % ((q5)))
            TT = "Ar " + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_PourBoire.set(Tax)
            self.var_Montant.set(ST)
            self.var_Total.set(TT)

        elif (self.var_Diner.get() == "Spaghetti" and self.var_Chambre.get() == "Luxe"):
            q1 = float(5000)
            q2 = float(20000)
            q3 = float(self.var_NombreDeJour.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Ar " + str("%.2f" % ((q5) * 0.09))
            ST = "Ar " + str("%.2f" % ((q5)))
            TT = "Ar " + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_PourBoire.set(Tax)
            self.var_Montant.set(ST)
            self.var_Total.set(TT)

        elif (self.var_Diner.get() == "Sushi" and self.var_Chambre.get() == "Solitaire"):
            q1 = float(5000)
            q2 = float(12000)
            q3 = float(self.var_NombreDeJour.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Ar " + str("%.2f" % ((q5) * 0.09))
            ST = "Ar " + str("%.2f" % ((q5)))
            TT = "Ar " + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_PourBoire.set(Tax)
            self.var_Montant.set(ST)
            self.var_Total.set(TT)

        elif (self.var_Diner.get() == "Sushi" and self.var_Chambre.get() == "Double"):
            q1 = float(5000)
            q2 = float(17000)
            q3 = float(self.var_NombreDeJour.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Ar " + str("%.2f" % ((q5) * 0.09))
            ST = "Ar " + str("%.2f" % ((q5)))
            TT = "Ar " + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_PourBoire.set(Tax)
            self.var_Montant.set(ST)
            self.var_Total.set(TT)

        elif (self.var_Diner.get() == "Sushi" and self.var_Chambre.get() == "Luxe"):
            q1 = float(5000)
            q2 = float(22000)
            q3 = float(self.var_NombreDeJour.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Ar " + str("%.2f" % ((q5) * 0.09))
            ST = "Ar " + str("%.2f" % ((q5)))
            TT = "Ar " + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_PourBoire.set(Tax)
            self.var_Montant.set(ST)
            self.var_Total.set(TT)

        elif (self.var_Diner.get() == "Soupe" and self.var_Chambre.get() == "Solitaire"):
            q1 = float(2000)
            q2 = float(8000)
            q3 = float(self.var_NombreDeJour.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Ar " + str("%.2f" % ((q5) * 0.09))
            ST = "Ar " + str("%.2f" % ((q5)))
            TT = "Ar " + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_PourBoire.set(Tax)
            self.var_Montant.set(ST)
            self.var_Total.set(TT)

        elif (self.var_Diner.get() == "Soupe" and self.var_Chambre.get() == "Double"):
            q1 = float(2000)
            q2 = float(13000)
            q3 = float(self.var_NombreDeJour.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Ar " + str("%.2f" % ((q5) * 0.09))
            ST = "Ar " + str("%.2f" % ((q5)))
            TT = "Ar " + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_PourBoire.set(Tax)
            self.var_Montant.set(ST)
            self.var_Total.set(TT)

        elif (self.var_Diner.get() == "Soupe" and self.var_Chambre.get() == "Luxe"):
            q1 = float(2000)
            q2 = float(18000)
            q3 = float(self.var_NombreDeJour.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Ar " + str("%.2f" % ((q5) * 0.09))
            ST = "Ar " + str("%.2f" % ((q5)))
            TT = "Ar " + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_PourBoire.set(Tax)
            self.var_Montant.set(ST)
            self.var_Total.set(TT)


if __name__ == "__main__":
    root = Tk()
    obj = Fenetre_chambre(root)
    root.mainloop()