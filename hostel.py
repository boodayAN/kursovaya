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

        self.guests_label = tk.Label(self, text="Сколько гостей:")
        self.guests_var = tk.StringVar(self, "1")
        self.guests_menu = tk.OptionMenu(self, self.guests_var, *range(1, 5))

        self.beds_label = tk.Label(self, text="Количество двуспальных кроватей:")
        self.beds_var = tk.StringVar(self, "0")
        self.beds_menu = tk.OptionMenu(self, self.beds_var, *range(1, 3))

        self.cleaning_label = tk.Label(self, text="Уборка в номере:")
        self.cleaning_var = tk.StringVar(self, "Нет")
        self.cleaning_menu = tk.OptionMenu(self, self.cleaning_var, "Нет", "Утро", "Вечер", "Оба")

        self.calculate_button = tk.Button(self, text="Подсчитать", command=self.calculate_total)  # Кнопка для подсчета стоимости
        self.total_label = tk.Label(self, text="Итоговая стоимость: 0 рублей")  # Метка для вывода итоговой стоимости

        # Создание интерфейса
        self.create_layout()

    # Создание расположения элементов на интерфейсе
    def create_layout(self):
        self.days_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.days_menu.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.guests_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.guests_menu.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.beds_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.beds_menu.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.cleaning_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.cleaning_menu.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        self.calculate_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
        self.total_label.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

    # Метод для вычисления итоговой стоимости
    def calculate_total(self):
        # Получение значений параметров бронирования
        days_cost = int(self.days_var.get()) * 1000
        guests_cost = int(self.guests_var.get()) * 1000
        beds_cost = int(self.beds_var.get()) * 500
        cleaning_cost = {"Нет": 0, "Утро": 500, "Вечер": 500, "Оба": 1000}[self.cleaning_var.get()]

        # Вычисление итоговой стоимости
        total_cost = days_cost + guests_cost + beds_cost + cleaning_cost
        self.total_label.config(text=f"Итоговая стоимость: {total_cost} рублей")

# Запуск приложения
if __name__ == "__main__":
    app = HotelReservationApp()
    app.mainloop()