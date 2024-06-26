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

        self.meal_label = tk.Label(self, text="Питание:")  # Метка для выбора питания
        self.breakfast_var = tk.BooleanVar(self, False)  # Переменная для хранения выбранного завтрака
        self.breakfast_cb = tk.Checkbutton(self, text="Завтрак", variable=self.breakfast_var)  # Флажок для выбора завтрака
        self.lunch_var = tk.BooleanVar(self, False)  # Переменная для хранения выбранного обеда
        self.lunch_cb = tk.Checkbutton(self, text="Обед", variable=self.lunch_var)  # Флажок для выбора обеда
        self.dinner_var = tk.BooleanVar(self, False)  # Переменная для хранения выбранного ужина
        self.dinner_cb = tk.Checkbutton(self, text="Ужин", variable=self.dinner_var)  # Флажок для выбора ужина

        self.smoking_label = tk.Label(self, text="Номер для курящих:")
        self.smoking_var = tk.StringVar(self, "Нет")
        self.smoking_menu = tk.OptionMenu(self, self.smoking_var, "Нет", "Да")

        self.calculate_button = tk.Button(self, text="Подсчитать", command=self.calculate_total)  # Кнопка для подсчета стоимости
        self.total_label = tk.Label(self, text="Итоговая стоимость: 0 рублей")  # Метка для вывода итоговой стоимости
        self.reserve_button = tk.Button(self, text="Забронировать номер", command=self.reserve_room)  # Кнопка для бронирования номера

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

        self.meal_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.breakfast_cb.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        self.lunch_cb.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        self.dinner_cb.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        self.smoking_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.smoking_menu.grid(row=7, column=1, padx=10, pady=5, sticky="w")

        self.calculate_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
        self.total_label.grid(row=9, column=0, columnspan=2, padx=10, pady=5)
        self.reserve_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

    # Метод для вычисления итоговой стоимости
    def calculate_total(self):
        # Получение значений параметров бронирования
        days_cost = int(self.days_var.get()) * 1000
        guests_cost = int(self.guests_var.get()) * 1000
        beds_cost = int(self.beds_var.get()) * 500
        cleaning_cost = {"Нет": 0, "Утро": 500, "Вечер": 500, "Оба": 1000}[self.cleaning_var.get()]

        # Вычисление стоимости питания
        meal_cost = 0
        if self.breakfast_var.get():
            meal_cost += 450
        if self.lunch_var.get():
            meal_cost += 450
        if self.dinner_var.get():
            meal_cost += 450
        meal_cost =  meal_cost * int(self.days_var.get()) * int(self.guests_var.get())

        smoking_cost = {"Нет": 0, "Да": 199}[self.smoking_var.get()]

        # Вычисление итоговой стоимости
        total_cost = days_cost + guests_cost + beds_cost + cleaning_cost  + meal_cost + smoking_cost
        self.total_label.config(text=f"Итоговая стоимость: {total_cost} рублей")

    # Метод для бронирования номера
    def reserve_room(self):
        total_cost = int(self.total_label.cget("text").split(":")[1].strip().split()[0])
        if total_cost != 0:
            # Проверка подтверждения бронирования
            if messagebox.askyesno("Забронировать номер", "Хотите забронировать номер?"):
                name = "";
                while name == "":
                    name = simpledialog.askstring("Фамилия и Имя клиента:", "Введите имя и фамилию клиента, на которого будет забронирован номер")

             # Запрос номера телефона
                phone_number = "";
                while phone_number == "":
                 phone_number = simpledialog.askstring("Оставьте номер телефона", "Пожалуйста, оставьте ваш номер телефона")
                # Вывод информации о бронировании
                messagebox.showinfo("Бронирование номера", f"Спасибо за бронирование, {name}. Ваш номер телефона: {phone_number}")
            else:
                messagebox.showinfo("Гостиница", "Будем рады видеть вас в нашей гостинице!")
        else:
            messagebox.showinfo("Ошибка", "Сначала заполните данные о номере.")

# Запуск приложения
if __name__ == "__main__":
    app = HotelReservationApp()
    app.mainloop()