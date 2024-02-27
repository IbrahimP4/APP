import tkinter as tk

def calculer_moyennes():
    # Moyenne AP
    note_TP = float(entry_note_TP_AP.get())
    note_projet = float(entry_note_projet_AP.get())
    note_DSi = float(entry_note_DSi_AP.get())
    note_DSf = float(entry_note_DSf_AP.get())
    TP = note_TP * 0.125
    projet = note_projet * 0.375
    DSi = note_DSi * 0.25
    DSf = note_DSf * 0.25
    Moyenne_AP = TP + projet + DSi + DSf

    # Moyenne Maths
    note_DSi = float(entry_note_DSi_Maths.get())
    DSi = note_DSi
    note_DSf = float(entry_note_DSf_Maths.get())
    DSf = note_DSf
    note_ET = float(entry_note_ET.get())
    ET = note_ET
    Moyenne_Maths = ((DSi + DSf)/2) + ET

    # Moyenne TWEB
    note_TP = float(entry_note_TP_TWEB.get())
    TP = note_TP * 0.3
    note_projet = float(entry_note_projet_TWEB.get())
    Projet = note_projet * 0.3
    note_DS = float(entry_note_DS_TWEB.get())
    DS = note_DS * 0.4
    Moyenne_TWEB = TP + Projet + DS

    Moyenne_BCC1 = ((Moyenne_Maths * 12) + (Moyenne_AP * 8) + (Moyenne_TWEB * 4)) / 24

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"Moyenne AP: {Moyenne_AP}\n")
    result_text.insert(tk.END, f"Moyenne Maths: {Moyenne_Maths}\n")
    result_text.insert(tk.END, f"Moyenne TWEB: {Moyenne_TWEB}\n")
    result_text.insert(tk.END, f"Moyenne BCC1: {Moyenne_BCC1}\n")

root = tk.Tk()
root.title("Calculateur de Moyennes")

# Create labels and entry fields for each subject
for subject in ["AP", "Maths", "TWEB"]:
    tk.Label(root, text=f"Notes pour {subject}:").pack()
    for note_type in ["TP", "Projet", "DSi", "DSf"]:
        tk.Label(root, text=f"Note de {note_type}:").pack()
        globals()[f"entry_note_{note_type}_{subject}"] = tk.Entry(root)
        globals()[f"entry_note_{note_type}_{subject}"].pack()

# Create button to calculate averages
button = tk.Button(root, text="Calculer les moyennes", command=calculer_moyennes)
button.pack()

# Create text widget to display results
result_text = tk.Text(root)
result_text.pack()

root.mainloop()