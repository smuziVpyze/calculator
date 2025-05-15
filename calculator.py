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