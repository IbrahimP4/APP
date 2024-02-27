import tkinter as tk
from tkinter import messagebox

def calculer_moyenne():
    try:
        note_TP_AP = float(entry_TP_AP.get())
        note_projet_AP = float(entry_projet_AP.get())
        note_DSi_AP = float(entry_DSi_AP.get())
        note_DSf_AP = float(entry_DSf_AP.get())
        note_DSi_Maths = float(entry_DSi_Maths.get())
        note_DSf_Maths = float(entry_DSf_Maths.get())
        note_ET_Maths = float(entry_ET_Maths.get())
        note_TP_TWEB = float(entry_TP_TWEB.get())
        note_projet_TWEB = float(entry_projet_TWEB.get())
        note_DS_TWEB = float(entry_DS_TWEB.get())

        Moyenne_AP = note_TP_AP * 0.125 + note_projet_AP * 0.375 + note_DSi_AP * 0.25 + note_DSf_AP * 0.25
        Moyenne_Maths = ((note_DSi_Maths + note_DSf_Maths)/2) + note_ET_Maths
        Moyenne_TWEB = note_TP_TWEB * 0.3 + note_projet_TWEB * 0.3 + note_DS_TWEB * 0.4

        Moyenne_BCC1 = ((Moyenne_Maths * 12) + (Moyenne_AP * 8) + (Moyenne_TWEB * 4)) / 24

        if Moyenne_BCC1 >= 10:
            messagebox.showinfo("Résultat", f"Mashallah tu as {Moyenne_BCC1} de moyenne générale avec {Moyenne_Maths} de moyenne en Maths, {Moyenne_AP} de moyenne en AP et {Moyenne_TWEB} de moyenne en TWEB")
        else:
            messagebox.showinfo("Résultat", f"Tu n'a pas validé car tu as {Moyenne_BCC1} de moyenne générale avec {Moyenne_Maths} de moyenne en Maths, {Moyenne_AP} de moyenne en AP et {Moyenne_TWEB} de moyenne en TWEB")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres valides pour toutes les notes.")

root = tk.Tk()

label_TP_AP = tk.Label(root, text="Note de TP AP :")
label_TP_AP.pack()
entry_TP_AP = tk.Entry(root)
entry_TP_AP.pack()

label_projet_AP = tk.Label(root, text="Note de projet AP :")
label_projet_AP.pack()
entry_projet_AP = tk.Entry(root)
entry_projet_AP.pack()

label_DSi_AP = tk.Label(root, text="Note de DSi AP :")
label_DSi_AP.pack()
entry_DSi_AP = tk.Entry(root)
entry_DSi_AP.pack()

label_DSf_AP = tk.Label(root, text="Note de DSf AP :")
label_DSf_AP.pack()
entry_DSf_AP = tk.Entry(root)
entry_DSf_AP.pack()

label_DSi_Maths = tk.Label(root, text="Note de DSi Maths :")
label_DSi_Maths.pack()
entry_DSi_Maths = tk.Entry(root)
entry_DSi_Maths.pack()

label_DSf_Maths = tk.Label(root, text="Note de DSf Maths :")
label_DSf_Maths.pack()
entry_DSf_Maths = tk.Entry(root)
entry_DSf_Maths.pack()

label_ET_Maths = tk.Label(root, text="Note d'ET Maths :")
label_ET_Maths.pack()
entry_ET_Maths = tk.Entry(root)
entry_ET_Maths.pack()

label_TP_TWEB = tk.Label(root, text="Note de TP TWEB :")
label_TP_TWEB.pack()
entry_TP_TWEB = tk.Entry(root)
entry_TP_TWEB.pack()

label_projet_TWEB = tk.Label(root, text="Note de projet TWEB :")
label_projet_TWEB.pack()
entry_projet_TWEB = tk.Entry(root)
entry_projet_TWEB.pack()

label_DS_TWEB = tk.Label(root, text="Note de DS TWEB :")
label_DS_TWEB.pack()
entry_DS_TWEB = tk.Entry(root)
entry_DS_TWEB.pack()

button = tk.Button(root, text="Calculer la moyenne", command=calculer_moyenne)
button.pack()

root.mainloop()