import tkinter as tk
from tkinter import ttk
import sys
from process import CpuBar
from widget_update import ConfigWidget

class Application(tk.Tk, ConfigWidget):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)      # запрет на измененин размеров окна
        self.title('Utilite monitor bar') # название утилиты в верху окна
        self.geometry('+10+30')           # отступ от угла экрана
        self.update_idletasks()           # обновление окна
        self.attributes('-topmost', True) # окно всегда поверх друких окон
        self.attributes('-alpha', 0.85)    # прозначность онка
        self.update_idletasks()           # обновление окна
        self.overrideredirect(True)      # убрать системное окно с '_ <> X'
        self.iconphoto(True, tk.PhotoImage(file='icon_11.png')) # фото на иконку

        self.cpu = CpuBar()
        self.run_set_utilite()

    def run_set_utilite(self): # создание всего содержимого окна и запуск работы
        self.set_utilite()
        self.make_bar_cpu()
        # self.config_cpu_bar()

    def set_utilite(self):
        pass

    def make_bar_cpu(self):
        pass

    def make_minwin(self):
        pass

    def enter_mouse(self):
        pass

    def leave_mouse(self):
        pass

    def choise_combo(self):
        pass

    def make_full_win(self):
        pass

    def app_exit(self):
        pass
if __name__=='__main__':
    root = Application()
    root.mainloop()
