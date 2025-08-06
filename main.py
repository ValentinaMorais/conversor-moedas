import requests
import tkinter as tk
from tkinter import ttk, messagebox

def get_conversion_rate(from_currency, to_currency):
    url = f"https://api.frankfurter.app/latest?from={from_currency}&to={to_currency}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        print("Resposta da API:", data)
        rate = data['rates'][to_currency]
        return rate
    except Exception as e:
        print("Erro ao buscar taxa:", e)
        return None

def convert():
    try:
        amount = float(entry_amount.get())
        from_curr = combo_from.get()
        to_curr = combo_to.get()
        rate = get_conversion_rate(from_curr, to_curr)

        if rate is None:
            messagebox.showerror("Erro", "Não foi possível buscar a taxa de câmbio.")
            return

        result = amount * rate
        label_result.config(text=f"{amount:.2f} {from_curr} = {result:.2f} {to_curr}")
    except ValueError:
        messagebox.showerror("Erro", "Insira um valor numérico válido.")

currencies = ['USD', 'EUR', 'BRL', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF']

root = tk.Tk()
root.title("Conversor de Moedas")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Valor:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=10)
entry_amount = tk.Entry(root, font=("Arial", 12), justify="center")
entry_amount.pack()

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

combo_from = ttk.Combobox(frame, values=currencies, width=10, state="readonly")
combo_from.set("USD")
combo_from.grid(row=0, column=0, padx=10)

tk.Label(frame, text="→", bg="#f0f0f0", font=("Arial", 12)).grid(row=0, column=1)

combo_to = ttk.Combobox(frame, values=currencies, width=10, state="readonly")
combo_to.set("BRL")
combo_to.grid(row=0, column=2, padx=10)

btn_convert = tk.Button(root, text="Converter", command=convert, bg="#4CAF50", fg="white", font=("Arial", 12), width=15)
btn_convert.pack(pady=15)

label_result = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 14, "bold"))
label_result.pack()

root.mainloop()
