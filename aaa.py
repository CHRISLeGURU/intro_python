import tkinter as tk

# Dictionnaire des utilisateurs
utilisateurs = {
  "CHRIS": "1235",
  "JAYSON": "007BOND"
}

# Fonction de vérification de login
def login():
  nom_utilisateur = nom_utilisateur_entry.get()
  mot_de_passe = mot_de_passe_entry.get()

  if nom_utilisateur in utilisateurs and utilisateurs[nom_utilisateur] == mot_de_passe:
    # Afficher un message de succès
    message_label.config(text="Login réussi !")
  else:
    # Afficher un message d'erreur
    message_label.config(text="Nom d'utilisateur ou mot de passe incorrect")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Login")


# Ajout des champs de saisie
nom_utilisateur_label = tk.Label(fenetre, text="Nom d'utilisateur:")
nom_utilisateur_entry = tk.Entry(fenetre)

mot_de_passe_label = tk.Label(fenetre, text="Mot de passe:")
mot_de_passe_entry = tk.Entry(fenetre, show="*")

# Ajout du bouton de login
bouton_login = tk.Button(fenetre, text="Login", command=login)

# Ajout du message d'information
message_label = tk.Label(fenetre, text="")

# Disposition des éléments
nom_utilisateur_label.grid(row=0, column=0)
nom_utilisateur_entry.grid(row=0, column=1)

mot_de_passe_label.grid(row=1, column=0)
mot_de_passe_entry.grid(row=1, column=1)

bouton_login.grid(row=2, column=1)

message_label.grid(row=3, column=1)

# Lancement de la boucle principale
fenetre.mainloop()