import tkinter as tk
import math


class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")

        self.entry = tk.Entry(root, font=('Helvetica', 20))
        self.entry.grid(row=0, column=0, columnspan=5)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sin', 'cos', 'tan', '^2',
            'sqrt', '(', ')', 'C'
        ]

        row_val = 1
        col_val = 0

        for button_text in buttons:
            tk.Button(
                root,
                text=button_text,
                font=('Helvetica', 15),
                command=lambda text=button_text: self.button_click(text)
            ).grid(row=row_val, column=col_val, padx=10, pady=10)

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def button_click(self, text):
        if text == '=':
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, 'Error')
        elif text == 'C':
            self.entry.delete(0, tk.END)
        elif text == 'sqrt':
            self.entry.insert(tk.END, 'sqrt(')
        elif text == '^2':
            self.entry.insert(tk.END, '**2')
        elif text in ('sin', 'cos', 'tan'):
            self.entry.insert(tk.END, f"{text}(")
        else:
            self.entry.insert(tk.END, text)


if __name__ == "__main__":
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()
