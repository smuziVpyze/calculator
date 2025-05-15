import tkinter as tk
from tkinter import ttk

def convert():
    try:
        value = float(entry.get())
        from_unit = from_unit_combobox.get()
        to_unit = to_unit_combobox.get()

        if from_unit == "Метры" and to_unit == "Километры":
            result = value / 1000
        elif from_unit == "Километры" and to_unit == "Метры":
            result = value * 1000
        elif from_unit == "Граммы" and to_unit == "Килограммы":
            result = value / 1000
        elif from_unit == "Килограммы" and to_unit == "Граммы":
            result = value * 1000
        elif from_unit == "Цельсий" and to_unit == "Фаренгейт":
            result = (value * 9/5) + 32
        elif from_unit == "Фаренгейт" and to_unit == "Цельсий":
            result = (value - 32) * 5/9
        else:
            result = value  # Если выбран один и тот же тип единиц

        result_label.config(text=f"Результат: {result:.2f}")
    except ValueError:
        result_label.config(text="Пожалуйста, введите корректное число")

# Создание главного окна
root = tk.Tk()
root.title("Калькулятор перевода единиц измерения")

# Создание интерфейса
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0)

entry_label = ttk.Label(frame, text="Введите значение:")
entry_label.grid(row=0, column=0)

entry = ttk.Entry(frame, width=15)
entry.grid(row=0, column=1)

from_unit_label = ttk.Label(frame, text="Единица измерения (от):")
from_unit_label.grid(row=1, column=0)

from_unit_combobox = ttk.Combobox(frame, values=["Метры", "Километры", "Граммы", "Килограммы", "Цельсий", "Фаренгейт"])
from_unit_combobox.grid(row=1, column=1)
from_unit_combobox.set("Метры")

to_unit_label = ttk.Label(frame, text="Единица измерения (в):")
to_unit_label.grid(row=2, column=0)

to_unit_combobox = ttk.Combobox(frame, values=["Метры", "Километры", "Граммы", "Килограммы", "Цельсий", "Фаренгейт"])
to_unit_combobox.grid(row=2, column=1)
to_unit_combobox.set("Километры")

convert_button = ttk.Button(frame, text="Перевести", command=convert)
convert_button.grid(row=3, column=0, columnspan=2)

result_label = ttk.Label(frame, text="Результат: ")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()