import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Engineering Lab Suite - Cresencio")
root.geometry("600x850")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

tab_elec = ttk.Frame(notebook)
tab_chem = ttk.Frame(notebook)
tab_unit = ttk.Frame(notebook)

notebook.add(tab_elec, text='Electronics')
notebook.add(tab_chem, text='Electrochemistry')
notebook.add(tab_unit, text='Unit Converter')

tk.Label(tab_elec, text="Circuit Analysis Tools", font=("Arial", 12, "bold")).pack(pady=10)

tk.Label(tab_elec, text="--- Ohm's Law (V = I * R) ---").pack()
v_ent = tk.Entry(tab_elec); v_ent.insert(0, "Voltage (V)"); v_ent.pack()
i_ent = tk.Entry(tab_elec); i_ent.insert(0, "Current (I)"); i_ent.pack()
r_ent = tk.Entry(tab_elec); r_ent.insert(0, "Resistance (R)"); r_ent.pack()

def solve_ohms():
    try:
        if v_ent.get() == "" or v_ent.get() == "Voltage (V)":
            res = float(i_ent.get()) * float(r_ent.get())
            v_ent.delete(0, tk.END); v_ent.insert(0, str(round(res, 4)))
        elif i_ent.get() == "" or i_ent.get() == "Current (I)":
            res = float(v_ent.get()) / float(r_ent.get())
            i_ent.delete(0, tk.END); i_ent.insert(0, str(round(res, 4)))
        elif r_ent.get() == "" or r_ent.get() == "Resistance (R)":
            res = float(v_ent.get()) / float(i_ent.get())
            r_ent.delete(0, tk.END); r_ent.insert(0, str(round(res, 4)))
    except:
        messagebox.showerror("Error", "Fill 2 boxes to solve the 3rd")

tk.Button(tab_elec, text="Solve Ohm's Law", command=solve_ohms).pack(pady=5)

tk.Label(tab_chem, text="Electrochemistry Solver", font=("Arial", 12, "bold")).pack(pady=10)

tk.Label(tab_chem, text="E_cell = E_cathode - E_anode").pack()
ecath = tk.Entry(tab_chem); ecath.insert(0, "E_cathode"); ecath.pack()
eano = tk.Entry(tab_chem); eano.insert(0, "E_anode"); eano.pack()
ecell = tk.Entry(tab_chem); ecell.insert(0, "E_cell"); ecell.pack()

def solve_potential():
    try:
        if ecell.get() == "" or ecell.get() == "E_cell":
            res = float(ecath.get()) - float(eano.get())
            ecell.delete(0, tk.END); ecell.insert(0, str(round(res, 4)))
        elif ecath.get() == "" or ecath.get() == "E_cathode":
            res = float(ecell.get()) + float(eano.get())
            ecath.delete(0, tk.END); ecath.insert(0, str(round(res, 4)))
    except: messagebox.showerror("Error", "Check Potential inputs")

tk.Button(tab_chem, text="Solve Potential", command=solve_potential).pack(pady=5)

tk.Label(tab_chem, text="--- Gibbs Free Energy (G = -nFE) ---").pack(pady=10)
g_ent = tk.Entry(tab_chem); g_ent.insert(0, "Delta G"); g_ent.pack()
n_ent = tk.Entry(tab_chem); n_ent.insert(0, "moles of e- (n)"); n_ent.pack()
e_gibbs = tk.Entry(tab_chem); e_gibbs.insert(0, "E_cell"); e_gibbs.pack()

F_CONST = 96485

def solve_gibbs():
    try:
        if g_ent.get() == "" or g_ent.get() == "Delta G":
            res = -float(n_ent.get()) * F_CONST * float(e_gibbs.get())
            g_ent.delete(0, tk.END); g_ent.insert(0, str(round(res, 2)))
    except: messagebox.showerror("Error", "Check Gibbs inputs")

tk.Button(tab_chem, text="Solve Gibbs", command=solve_gibbs).pack(pady=5)

tk.Label(tab_unit, text="Lab Unit Converter", font=("Arial", 12, "bold")).pack(pady=10)
conv_input = tk.Entry(tab_unit); conv_input.pack()

unit_choice = tk.StringVar(value="Lbs to Kg")
drop = ttk.Combobox(tab_unit, textvariable=unit_choice)
drop['values'] = ("Lbs to Kg", "Kg to Lbs", "Celsius to Kelvin", "Inches to mm")
drop.pack(pady=10)

def do_convert():
    try:
        val = float(conv_input.get())
        mode = unit_choice.get()
        if mode == "Lbs to Kg": res = val * 0.4536
        elif mode == "Kg to Lbs": res = val / 0.4536
        elif mode == "Celsius to Kelvin": res = val + 273.15
        elif mode == "Inches to mm": res = val * 25.4
        label_res.config(text=f"Result: {round(res, 4)}")
    except: messagebox.showerror("Error", "Enter a number")

tk.Button(tab_unit, text="Convert Now", command=do_convert).pack()
label_res = tk.Label(tab_unit, text="Result: --", font=("Arial", 12))
label_res.pack(pady=20)

root.mainloop()
