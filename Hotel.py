from tkinter import *
from PIL import Image, ImageTk
from client import Fenetre_Client
from chambre import Fenetre_chambre
from details import Fenetre_Details
from tkinter import messagebox

class GestionHotelSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("SYSTÈME DE GESTION D'HÔTEL")
        self.root.geometry("1550x800+0+0")
        self.root.configure(bg="#f0f0f0")

        # Titre
        lbl_title = Label(self.root, text="HOTEL AMAZONE", font=("Arial", 40, "bold"), bg="#282c34", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1550, height=70)

        # Cadre principal
        main_frame = Frame(self.root, bd=4, relief=RIDGE, bg="#ffffff")
        main_frame.place(x=0, y=70, width=1550, height=730)

        # Menu
        lbl_menu = Label(main_frame, text="MENU", font=("Helvetica", 20, "bold"), bg="#282c34", fg="white", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230, height=50)

        # Cadre des boutons
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE, bg="#f0f0f0")
        btn_frame.place(x=0, y=50, width=230, height=680)

        # Boutons
        btn_style = {"font": ("Helvetica", 14, "bold"), "bg": "#007acc", "fg": "white", "bd": 0, "cursor": "hand1"}
        cust_btn = Button(btn_frame, text="NOS CLIENTS", command=self.cust_details, width=22, **btn_style)
        cust_btn.grid(row=0, column=0, pady=10)

        room_btn = Button(btn_frame, text="RESERVER", command=self.roombooking, width=22, **btn_style)
        room_btn.grid(row=1, column=0, pady=10)

        details_btn = Button(btn_frame, text="CHAMBRES", command=self.details, width=22, **btn_style)
        details_btn.grid(row=2, column=0, pady=10)

        report_btn = Button(btn_frame, text="FACTURE", width=22, **btn_style)
        report_btn.grid(row=3, column=0, pady=10)

        logout_btn = Button(btn_frame, text="DÉCONNEXION", command=self.logout, width=22, **btn_style)
        logout_btn.grid(row=4, column=0, pady=10)

        # Image principale
        img3 = Image.open(r"image/FantoriaAminPiscine.jpg")
        img3 = img3.resize((1310, 680), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimag1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimag1.place(x=230, y=0, width=1310, height=680)

        # Images du menu
        img4 = Image.open(r"image/SalleReceptionChicRouge.jpg")
        img4 = img4.resize((230, 340), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lblimag2 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimag2.place(x=0, y=230, width=230, height=340)

        img5 = Image.open(r"image/ChambreVueMer.jpg")
        img5 = img5.resize((230, 340), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lblimag3 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimag3.place(x=0, y=570, width=230, height=340)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Fenetre_Client(self.new_window)

    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Fenetre_chambre(self.new_window)

    def details(self):
        self.new_window = Toplevel(self.root)
        self.app = Fenetre_Details(self.new_window)

    def logout(self):
        logout = messagebox.askyesno("Système de Gestion d'Hôtel", "Voulez-vous vous déconnecter ?", parent=self.root)
        if logout > 0:
            self.root.destroy()
        else:
            if not logout:
                return

if __name__ == "__main__":
    root = Tk()
    obj = GestionHotelSystem(root)
    root.mainloop()
