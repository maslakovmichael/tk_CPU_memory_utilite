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
        # self.update_idletasks()           # обновление окна
        self.attributes('-topmost', True) # окно всегда поверх друких окон
        # self.attributes('-alpha', 0.9)    # прозначность онка
        # self.update_idletasks()           # обновление окна
        self.overrideredirect(True)      # убрать системное окно с '_ <> X'
        self.iconphoto(True, tk.PhotoImage(file='icon_11.png')) # фото на иконку

        self.cpu = CpuBar() # создаем обьект в котором получаем параметры CPU и RAM
        self.run_set_utilite() # запускаем создание элементов окна и роботу приложения

    def run_set_utilite(self): # создание всего содержимого окна и запуск работы
        self.set_utilite()
        self.make_bar_cpu()
        self.config_cpu_bar()

    def set_utilite(self): # функция создания и размещения элементов окна приложения
        self.exit_button = ttk.Button(self, text='Exit', command=self.app_exit ) # создаем кнопку выхода из программы
        self.exit_button.pack(fill=tk.X) # розмещаем ее растянув по оси Х

        self.bar_1 = ttk.LabelFrame(self, text='Manual') # создаем область для комбобокса
        self.bar_1.pack(fill=tk.X)

        self.combo_win = ttk.Combobox(self.bar_1, values=['hide', 'don\'t hide', 'min'],
                                      width=9, state='readonly') # создаем комбобокс с выбором режима отображения окна во фрейме, со статусом только для чтения
        self.combo_win.current(1) # обозначаем какой режим будет отображаться - по номеру из списка
        self.combo_win.pack(side=tk.LEFT) # размещаем комбобокс по левую сторону

        ttk.Button(self.bar_1, text='change', command=self.configure_win).pack(side=tk.LEFT) # создаем кнопку чтоб убрать/установить рамку вокруг окна
        ttk.Button(self.bar_1, text='>>>').pack(side=tk.LEFT) # соэдаем кнопки, чтоб занять ими пространства Label_frame
        ttk.Button(self.bar_1, text='<<<').pack(side=tk.LEFT)

        self.bar_2 = ttk.LabelFrame(self, text='Power')
        self.bar_2.pack(fill=tk.BOTH) # создаем второй LaberFrame

        self.bind_class('Tk', '<Enter>', self.enter_mouse) # обработка наведения мыши на окно
        self.bind_class('Tk', '<Leave>', self.leave_mouse) # обработка убирания мыши с окна
        self.combo_win.bind('<<ComboboxSelected>>', self.choise_combo) # обработка выбора на комбобоксе


    def make_bar_cpu(self): # создание бара для CPU в bar_2
        ttk.Label(self.bar_2, text=f'phisical cores: {self.cpu.cpu_count}, logical cores: {self.cpu.cpu_count_logical}',
                  anchor=tk.CENTER).pack(fill=tk.X) # создаем лейбл для вывлда количества ядер и количество потоков процессора,
        self.list_label = [] # список лейблов по количеству потоков
        self.list_pbar = [] # список прогрессбаров по количеству потоков

        for i in range(self.cpu.cpu_count_logical): # добавляем в списки лейблы и прогрессбары
            self.list_label.append(ttk.Label(self.bar_2, anchor=tk.CENTER))
            self.list_pbar.append(ttk.Progressbar(self.bar_2, length=100))
        for i in range(self.cpu.cpu_count_logical): # размещаем из списков лейблы и прогрессбары в self.bar_2
            self.list_label[i].pack(fill=tk.X)
            self.list_pbar[i].pack(fill=tk.X)

        self.ram_lab = ttk.Label(self.bar_2, text='', anchor=tk.CENTER)
        self.ram_lab.pack(fill=tk.X)
        self.ram_bar = ttk.Progressbar(self.bar_2, length=100)
        self.ram_bar.pack(fill=tk.X)

    def make_minwin(self): # формируем окно минимального режима
        ttk.Label(self, text='CPU: ').pack(side=tk.LEFT) # лейбл для CPU для мини-окна
        self.bar_one = ttk.Progressbar(self, length=100) # прогрессбар
        self.bar_one.pack(side=tk.LEFT)

        ttk.Label(self, text='RAM: ').pack(side=tk.LEFT) # лейбл для RAM для мини-окна
        self.ram_bar = ttk.Progressbar(self, length=100) # прогрессбар
        self.ram_bar.pack(side=tk.LEFT)

        ttk.Button(self, text='full', command=self.make_full_win, width=5).pack(side=tk.RIGHT) # кнопка возвращения в полный режим
        ttk.Button(self, text='change', command=self.configure_win, width=5).pack(side=tk.RIGHT) # кнопка изменения рамки

        self.update() # обновляем окно
        self.config_minwin() # создаем прогрессбары для CPU и RAM

    def enter_mouse(self, event):
        if self.combo_win.current() == 0 or 1: # если текущее значение комбобокса по списку 0 или 1, то...
            self.geometry('') # оставляем такую геометрию окна, какая есть

    def leave_mouse(self, event):
        if self.combo_win.current() == 0: # если значение - нулевое из списка значений комбобокса
            self.geometry(f'{self.winfo_width()}x2') # значит что ширина - текущая, а висоту выставить 1px

    def choise_combo(self, event):
        if self.combo_win.current()==2:
            self.enter_mouse('') # раскрываем окно
            self.unbind_class('Tk', '<Enter>') # отвязывоем реакцию на наведение мыши
            self.unbind_class('Tk', '<Leave>') # отвязываем реакцию на убирание мыши
            self.combo_win.unbind('<<ComboboxSelected>>') # отвязываем реакцию на комбобоксе
            self.after_cancel(self.wheel) # отвязываем обновление окна
            self.clear_win() # удаляем виджеты
            self.update()
            self.make_minwin() # запускаем виджет режима минимального окна

    def make_full_win(self):
            self.after_cancel(self.wheel) # обрываем цикличность
            self.clear_win() # очищаем окно от виджетов
            self.update()
            self.run_set_utilite() # создаем окно для полной версии
            self.enter_mouse('')
            self.combo_win.current(1)

    def app_exit(self):
        self.destroy() # метод завершения работы окна (уничтожение екземпляра self)
        sys.exit() # завершение процесса


if __name__=='__main__':
    root = Application()
    root.mainloop()
