# calculadora-sam
import tkinter as tk

def on_click(btn_text):
    current = entry.get()
    if btn_text == "=":
        try:
            result = eval(current)  # Avalia a expressão matemática
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Erro")
    elif btn_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, btn_text)

# Criação da janela principal
window = tk.Tk()
window.title("Calculadora")

# Caixa de entrada para exibir os números e resultados
entry = tk.Entry(window, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Definindo os botões
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Adicionando botões à interface
row, col = 1, 0
for btn in buttons:
    tk.Button(window, text=btn, width=5, height=2, font=("Arial", 18), command=lambda btn=btn: on_click(btn)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Iniciando a interface gráfica
window.mainloop()
