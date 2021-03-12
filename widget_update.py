


# этот класс будет родителем класса utilite.py, поэтому некоторые обьекты, методи и переменные здесь будут из класса-наследника
class ConfigWidget:
    def config_cpu_bar(self): # конфигурация стандартного окна
        r = self.cpu.cpu_percent_return()  # получаем процент загрузки процессора
        for i in range(self.cpu.cpu_count_logical): # получаем количиство потоков и перебираем их в цикле
            self.list_label[i].configure(text=f'core{i+1} usage {r[i]}%') # в список с лейблами заносим значения загрузки каждого потока в процентах
            self.list_pbar[i].configure(value=r[i]) # в список прогресс-баров заносим значение загрузки в процентах

        r2 = self.cpu.ram_usage()
        self.ram_lab.configure(text=f'RAM usage: {r2[2]}%, used: {round(r2[3]/1048576)}Mb, available: {round(r2[1]/1048576)} Mb') # заносим значения параметров памяти
        self.ram_bar.configure(value=r2[2]) # значение для прогресс-бара

        self.wheel = self.after(1000, self.config_cpu_bar) # создаем переменную wheel, в которой функция afret() для обновления данных раз в 1 секунду

    def configure_win(self): # функция для конфигурации окна - чтоб убирать или добавлять системную рамку
        if self.wm_overrideredirect():
            self.overrideredirect(False) # что то эта функция в tkinter не срабатывает
        else:
            self.overrideredirect(True)
        self.update() # обновление окна


    def config_minwin(self): # конфигурация мини-окна
        self.bar_one.configure(value=self.cpu.cpu_one_return()) # установка актуальных значений для cpu
        self.ram_bar.configure(value=self.cpu.ram_usage([2])) # установка актуальных значений для ram
        self.wheel = self.after(1000, self.config_minwin) # создаем переменную wheel, в которой функция afret() для обновления данных раз в 1 секунду

    def clear_win(self):                #метод очистки виджетов
        for i in self.winfo_children(): #перебираем виджеты (children) и отключаем их (destroy)
            i.destroy()