from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Fenetre_Client:
    def __init__(self, root):
        self.root = root
        self.root.title("SYSTEME DE GESTION D'HOTEL")
        self.root.geometry("1128x520+230+220")

        # ==================variable=========
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_nom=StringVar()
        self.var_prenom=StringVar()
        self.var_genre=StringVar()
        self.var_postal=StringVar()
        self.var_numero=StringVar()
        self.var_email=StringVar()
        self.var_nationalite=StringVar()
        self.var_preuve=StringVar()
        self.var_id=StringVar()
        self.var_addresse=StringVar()
        self.btnUpdate = StringVar()
        self.btnDelete = StringVar()

         #=========Titre ambony eo iny===========
        lbl_title =Label(self.root,text="GESTION DES CLIENTS", font=("times new roman",18,"bold"),bg="black",fg="WHITE",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

         #=========logo ambony iny===========

        #=========label ===========
        labelframeleft=LabelFrame(self.root,relief=RIDGE,text="Information du Client",font=("times new roman",12,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=400,height=490)

        #=========label et entree (ttk io mampisy style mirehitsy bleu amin'ny label io) ===========

        # referenece
        lbl_cust_ref=Label(labelframeleft,text="Reference :",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("arial",10,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

        # nom
        cname=Label(labelframeleft,text="Nom :",font=("arial",10,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        entry_nom=ttk.Entry(labelframeleft,textvariable=self.var_nom,width=29,font=("arial",10,"bold"))
        entry_nom.grid(row=1,column=1)

        # prenom
        lblmname=Label(labelframeleft,text="Prenom :",font=("arial",10,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        entry_prenom=ttk.Entry(labelframeleft,textvariable=self.var_prenom,width=29,font=("arial",10,"bold"))
        entry_prenom.grid(row=2,column=1)

        # genre
        label_gender=Label(labelframeleft,text="Genre :",font=("arial",10,"bold"),padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        combo_genre=ttk.Combobox(labelframeleft,textvariable=self.var_genre,font=("arial",10,"bold"),width=27,state="readonly")
        combo_genre["value"]=("Homme","Femme","Autre")
        combo_genre.current(0)
        combo_genre.grid(row=3,column=1)

        # numero
        label_number=Label(labelframeleft,text="N° Telephone :",font=("arial",10,"bold"),padx=2,pady=6)
        label_number.grid(row=5,column=0,sticky=W)
        entry_numero=ttk.Entry(labelframeleft,textvariable=self.var_numero,width=29,font=("arial",10,"bold"))
        entry_numero.grid(row=5,column=1)

        # email
        label_email=Label(labelframeleft,text="Email :",font=("arial",10,"bold"),padx=2,pady=6)
        label_email.grid(row=6,column=0,sticky=W)
        entry_email=ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=("arial",10,"bold"))
        entry_email.grid(row=6,column=1)

        # nationalite
        label_nationalite=Label(labelframeleft,text="Nationalité :",font=("arial",10,"bold"),padx=2,pady=6)
        label_nationalite.grid(row=7,column=0,sticky=W)

        combo_nationalite=ttk.Combobox(labelframeleft,textvariable=self.var_nationalite,font=("arial",10,"bold"),width=27,state="readonly")
        combo_nationalite["value"]=("Malagasy","Chinoise","Indienne","Américaine","Indonésienne","Pakistanaise","Brésilienne","Nigériane","Bangladaise","Russe","Mexicaine","Japonaise","Philippine","Égyptienne","Vietnamienne","Congolaise (République démocratique du Congo)","Turque","Iranienne","Allemande","Thaïlandaise","Britannique","Française","Italienne")
        combo_nationalite.current(0)
        combo_nationalite.grid(row=7,column=1)


        # identifiant
        label_idproof=Label(labelframeleft,text="Preuve d'Id :",font=("arial",10,"bold"),padx=2,pady=6)
        label_idproof.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_preuve,font=("arial",10,"bold"),width=27,state="readonly")
        combo_id["value"]=("CIN","Passe-port")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)

        # id
        label_id=Label(labelframeleft,text="Numero d'identification :",font=("arial",10,"bold"),padx=2,pady=6)
        label_id.grid(row=9,column=0,sticky=W)
        entry_id=ttk.Entry(labelframeleft,textvariable=self.var_id,width=29,font=("arial",10,"bold"))
        entry_id.grid(row=9,column=1)

        # ======== boutton CRUD reny==========
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=390,height=40)

        btnAdd=Button(btn_frame,command=self.add_data,text="Ajouter",font=("arial",12,"bold"),bg="green",fg="white",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        self.btnUpdate=Button(btn_frame,text="Modifier",command=self.update,font=("arial",11,"bold"),bg="purple",fg="white",width=9)
        self.btnUpdate.grid(row=0,column=1,padx=1)

        self.btnDelete=Button(btn_frame,command=self.mDelete,text="Supprimer",font=("arial",11,"bold"),bg="red",fg="white",width=9)
        self.btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,command=self.reset,text="Reinitialiser",font=("arial",12,"bold"),bg="black",fg="white",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        # Désactiver les boutons Modifier et Supprimer au démarrage
        self.btnUpdate.config(state=DISABLED, bg="grey")
        self.btnDelete.config(state=DISABLED, bg="grey")

        # ======== Table amin'ny CRUD==========
         #=========label ===========
        Table_Frame=LabelFrame(self.root,relief=RIDGE,text="Table des Informations des Clients & Recherche",font=("times new roman",12,"bold"),padx=2,)
        Table_Frame.place(x=410,y=50,width=800,height=500)

        # Recherche
        label_searchBy=Label(Table_Frame,text="Recherche par : ",font=("arial",10,"bold"),bg="gray" ,fg="white")
        label_searchBy.grid(row=0,column=0,sticky=W,padx=2)


        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_Frame,font=("arial",10,"bold"),textvariable=self.search_var,width=24,state="readonly")
        combo_search["value"]=("Nom","Prenom","Reference","Numero")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        entry_search=ttk.Entry(Table_Frame,width=24,textvariable=self.txt_search,font=("arial",10,"bold"))
        entry_search.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Recherche",font=("arial",10,"bold"),command=self.search,bg="green",fg="white",width=9)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,command=self.fetch_data,text="Tous afficher",font=("arial",10,"bold"),bg="purple",fg="white",width=9)
        btnShowAll.grid(row=0,column=4,padx=1)

        # =====Afficher la table===========
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=710,height=390)
        # details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        # details_table.place(x=0,y=50,width=850,height=390)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,columns=("Reference","Nom","Prenom","Genre","Numero","Email","Nationalite","Preuve","Id"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("Reference",text="Reference")
        self.Cust_Details_Table.heading("Nom",text="Nom")
        self.Cust_Details_Table.heading("Prenom",text="Prenom")
        self.Cust_Details_Table.heading("Genre",text="Genre")
        self.Cust_Details_Table.heading("Numero",text="Numero")
        self.Cust_Details_Table.heading("Email",text="Email")
        self.Cust_Details_Table.heading("Nationalite",text="Nationalite")
        self.Cust_Details_Table.heading("Preuve",text="Preuve")
        self.Cust_Details_Table.heading("Id",text="Id")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("Reference",width=100)
        self.Cust_Details_Table.column("Nom",width=100)
        self.Cust_Details_Table.column("Prenom",width=100)
        self.Cust_Details_Table.column("Genre",width=100)
        self.Cust_Details_Table.column("Numero",width=100)
        self.Cust_Details_Table.column("Email",width=100)
        self.Cust_Details_Table.column("Nationalite",width=100)
        self.Cust_Details_Table.column("Preuve",width=100)
        self.Cust_Details_Table.column("Id",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()




    def add_data(self):
        if self.var_numero.get() == "" or self.var_prenom.get() == "":
            messagebox.showerror("Erreur","Veuillez remplir les champs",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO client VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_ref.get(),
                    self.var_nom.get(),
                    self.var_prenom.get(),
                    self.var_genre.get(),
                    self.var_numero.get(),
                    self.var_email.get(),
                    self.var_nationalite.get(),
                    self.var_preuve.get(),
                    self.var_id.get(),
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Client ajouté avec succès",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Attention",f"Veuillez vérifier l'erreur : {str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM client")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_nom.set(row[1]),
        self.var_prenom.set(row[2]),
        self.var_genre.set(row[3]),
        self.var_numero.set(row[4]),
        self.var_email.set(row[5]),
        self.var_nationalite.set(row[6]),
        self.var_preuve.set(row[7]),
        self.var_id.set(row[8])

        self.btnUpdate.config(state=NORMAL, bg="purple")
        self.btnDelete.config(state=NORMAL, bg="red")

    def update(self):
        if self.var_numero.get()=="":
            messagebox.showerror("Erreur","Veuillez remplir le numéro", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="hotel")
                my_cursor=conn.cursor()
                my_cursor.execute("UPDATE client SET Nom=%s,Prenom=%s,Genre=%s,Numero=%s,Email=%s,Nationalite=%s,Preuve=%s,Id=%s WHERE Reference=%s", (

                    self.var_nom.get(),
                    self.var_prenom.get(),
                    self.var_genre.get(),
                    self.var_numero.get(),
                    self.var_email.get(),
                    self.var_nationalite.get(),
                    self.var_preuve.get(),
                    self.var_id.get(),
                    self.var_ref.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Modification","La modification du Client a réussi",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Attention",f"Veuillez vérifier l'erreur : {str(es)}",parent=self.root)

    def mDelete(self):
        mDelete = messagebox.askyesno("Système de Gestion d'Hôtel", "Voulez-vous vraiment supprimer ce client?",
                                      parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
            my_cursor = conn.cursor()
            query = "DELETE FROM client WHERE Reference=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_ref.set(str(random.randint(1000, 9999)))
        self.var_nom.set("")
        self.var_prenom.set("")
        self.var_genre.set("")
        self.var_numero.set("")
        self.var_email.set("")
        self.var_nationalite.set("")
        self.var_preuve.set("")
        self.var_id.set("")

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="hotel")
        my_cursor = conn.cursor()

        search_column = ""
        if self.search_var.get() == "Nom":
            search_column = "Nom"
        elif self.search_var.get() == "Prenom":
            search_column = "Prenom"
        elif self.search_var.get() == "Reference":
            search_column = "Reference"
        elif self.search_var.get() == "Numero":
            search_column = "Numero"

        query = f"SELECT * FROM client WHERE {search_column} LIKE %s"
        value = (f"%{self.txt_search.get()}%",)
        my_cursor.execute(query, value)
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for row in rows:
                self.Cust_Details_Table.insert("", END, values=row)
            conn.commit()
        conn.close()

if __name__ == "__main__":
    root=Tk()
    obj=Fenetre_Client(root)
    root.mainloop()