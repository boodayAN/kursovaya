import tkinter as tk
from tkinter import messagebox, simpledialog

class HotelReservationApp(tk.Tk):
    # Инициализация приложения
    def __init__(self):
        super().__init__()
        self.title("Гостиничное бронирование")  # Установка заголовка окна

        # Создание и инициализация элементов интерфейса
        self.days_label = tk.Label(self, text="На сколько дней:")  # Метка для выбора дней
        self.days_var = tk.StringVar(self, "1")  # Переменная для хранения выбранного количества дней
        self.days_menu = tk.OptionMenu(self, self.days_var, *range(1, 15))  # Выпадающее меню для выбора дней

        # Создание интерфейса
        self.create_layout()
        # Создание расположения элементов на интерфейсе
    def create_layout(self):
        self.days_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.days_menu.grid(row=0, column=1, padx=10, pady=5, sticky="w")

if __name__ == "__main__":
    app = HotelReservationApp()
    app.mainloop()