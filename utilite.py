import tkinter as tk
from tkinter import ttk
import sys
from process import CpuBar
from widget_update import ConfigWidget

class Application(tk.Tk, ConfigWidget):
    pass


if __name__=='__main__':
    root = Application()
    root.mainloop()
