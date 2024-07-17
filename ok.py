import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mail:
    def envoyer_email(self,destinataire, message):
        # Informations de connexion
        expediteur = "ejquestejquest@gmail.com"
        mot_de_passe = "ucbvpnstwvwdnqgo"

        # Création du message
        msg = MIMEMultipart()
        msg['From'] = expediteur
        msg['To'] = destinataire
        msg['Subject'] = "RESERVATION DE HOTEL"

        # Attacher le message au corps de l'email
        msg.attach(MIMEText(message, 'plain'))

        try:
            # Connexion au serveur SMTP de Gmail
            serveur = smtplib.SMTP('smtp.gmail.com', 587)
            serveur.starttls()
            serveur.login(expediteur, mot_de_passe)

            # Envoi de l'email
            texte = msg.as_string()
            serveur.sendmail(expediteur, destinataire, texte)
            serveur.quit()

            print("Email envoyé avec succès!")
        except Exception as e:
            print(f"Erreur lors de l'envoi de l'email: {e}")