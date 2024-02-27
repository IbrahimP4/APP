import tkinter as tk
from tkinter import messagebox

def calculer_BCC():
    try:
        # Récupération des notes
        général_m11 = ((float(entry_un.get()) + float(entry_deux.get())) / 2) + float(entry_trois.get())
        général_info = float(entry_quatre.get()) * 0.3 + (0.7 * (float(entry_cinq.get()) * 0.4 + float(entry_six.get()) * 0.6))
        général_disc = float(entry_sept.get())
        général_codage = float(entry_huit.get())

        # Calcul du BCC
        BCC = (général_m11 * 12) + (général_info * 9) + (général_disc * 3) + (général_codage * 3)
        BCC1 = BCC / 27

        # Affichage des résultats
        if BCC1 >= 10:
            messagebox.showinfo("Résultat", f"Mashallah tu as validé ton BCC avec {BCC1} de moyenne")
        else:
            messagebox.showinfo("Résultat", f"Allah y Sehel pour les ratrappages tu as {BCC1} de moyenne")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des notes valides.")

root = tk.Tk()
root.title("Calcul du BCC")

# Création des Entry widgets pour chaque matière
entry_un = tk.Entry(root, width=10)
entry_un.grid(row=0, column=1, padx=5, pady=5)
label_un = tk.Label(root, text="DSi de maths")
label_un.grid(row=0, column=0, padx=5, pady=5)

entry_deux = tk.Entry(root, width=10)
entry_deux.grid(row=1, column=1, padx=5, pady=5)
label_deux = tk.Label(root, text="DSf de maths")
label_deux.grid(row=1, column=0, padx=5, pady=5)

entry_trois = tk.Entry(root, width=10)
entry_trois.grid(row=2, column=1, padx=5, pady=5)
label_trois = tk.Label(root, text="Points ET")
label_trois.grid(row=2, column=0, padx=5, pady=5)

entry_quatre = tk.Entry(root, width=10)
entry_quatre.grid(row=3, column=1, padx=5, pady=5)
label_quatre = tk.Label(root, text="TP informatique")
label_quatre.grid(row=3, column=0, padx=5, pady=5)

entry_cinq = tk.Entry(root, width=10)
entry_cinq.grid(row=4, column=1, padx=5, pady=5)
label_cinq = tk.Label(root, text="DSi d'informatique")
label_cinq.grid(row=4, column=0, padx=5, pady=5)

entry_six = tk.Entry(root, width=10)
entry_six.grid(row=5, column=1, padx=5, pady=5)
label_six = tk.Label(root, text="DSf d'informatique")
label_six.grid(row=5, column=0, padx=5, pady=5)

entry_sept = tk.Entry(root, width=10)
entry_sept.grid(row=6, column=1, padx=5, pady=5)
label_sept = tk.Label(root, text="DS de maths discrète")
label_sept.grid(row=6, column=0, padx=5, pady=5)

entry_huit = tk.Entry(root, width=10)
entry_huit.grid(row=7, column=1, padx=5, pady=5)
label_huit = tk.Label(root, text="DS de codage")
label_huit.grid(row=7, column=0, padx=5, pady=5)

# Bouton pour calculer le BCC
bouton_calculer = tk.Button(root, text="Calculer BCC", command=calculer_BCC)
bouton_calculer.grid(row=8, column=0, columnspan=2, pady=10)

root.mainloop()
