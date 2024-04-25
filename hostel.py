import tkinter as tk
from tkinter import messagebox, simpledialog

class HotelReservationApp(tk.Tk):
    # Инициализация приложения
    def __init__(self):
        super().__init__()
        self.title("Гостиничное бронирование")  # Установка заголовка окна




        # Создание интерфейса
        self.create_layout()


if __name__ == "__main__":
    app = HotelReservationApp()
    app.mainloop()