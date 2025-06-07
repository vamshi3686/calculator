import tkinter as tk
from tkinter import ttk

def handle_button_click(clicked_button_text):
    current_text = result_var.get()

    if clicked_button_text == "=":
        try:
            expression = current_text.replace("÷", "/").replace("X", "*")
            result = eval(expression)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            result_var.set(result)
        except Exception:
            result_var.set("Error")
    elif clicked_button_text == "C":
        result_var.set("")
    elif clicked_button_text == "%":
        try:
            current_number = float(current_text)
            result_var.set(current_number / 100)
        except ValueError:
            result_var.set("Error")
    elif clicked_button_text == "±":
        try:
            current_number = float(current_text)
            result_var.set(-current_number)
        except ValueError:
            result_var.set("Error")
    else:
        result_var.set(current_text + clicked_button_text)

# Main window
root = tk.Tk()
root.title("Calculator")

# Result entry
result_var = tk.StringVar()
result_entry = ttk.Entry(root, textvariable=result_var, font=("Helvetica", 24), justify="right")
result_entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Button layout
buttons = [
    ("C", 1, 0), ("±", 1, 1), ("%", 1, 2), ("÷", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("X", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0, 2), (".", 5, 2), ("=", 5, 3)
]

# Style
style = ttk.Style()
style.theme_use('default')
style.configure("TButton", font=("Helvetica", 16))

# Buttons
for button_info in buttons:
    button_text, row, col = button_info[:3]
    colspan = button_info[3] if len(button_info) > 3 else 1
    button = ttk.Button(root, text=button_text, command=lambda text=button_text: handle_button_click(text), style="TButton")
    button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

# Grid config
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Set fixed size
root.geometry("500x700")
root.resizable(False, False)

# Key bindings
root.bind("<Return>", lambda event: handle_button_click("="))
root.bind("<BackSpace>", lambda event: handle_button_click("C"))

root.mainloop()
