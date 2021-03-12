import psutil as pt  # импортируем библиотеку psutil для работы с параметрами процессора и памяти

class CpuBar:
    def __init__(self):
        self.cpu_count = pt.cpu_count(logical=True) # получаем количество ядер процессора
        self.cpu_count_logical = pt.cpu_count()     # получаем количество потоков (без logical=True)

    def cpu_percent_return(self):
        return pt.cpu_percent(percpu=True)          # получаем значение загрузки процессора по потокам

    def cpu_one_return(self):
        return pt.cpu_percent()                     # получаем значение суммарной загрузки процессора

    def ram_usage(self):
        return pt.virtual_memory()                  # получаем параметры памяти

