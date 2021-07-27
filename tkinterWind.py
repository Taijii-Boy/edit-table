# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
import pythoncom
import pyperclip
import os
from win32com.client import Dispatch, gencache
from tkinter import filedialog


class Application(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.set_ui()


    def set_ui(self):
        self.title("Расчет массы Компас 3D v.0.1")
        # self.geometry(f"{root_width}x{root_height}+1200+200")
        self.resizable(False, False) # Возможность изменения размера по ширине и по высоте
        self.set_widgets()


    def set_widgets(self):

        document_types = ("*.cdw", "*.spw", "Служебка")
        need_to_delete_value = tk.IntVar()
        lib_path = "C:\\LYT\\GRAPHICIL.LYT"


        def change_entry_state(event):
            if  combo_document_type.get() == "*.cdw" or combo_document_type.get() == "Служебка":
                entry_library_path.configure(state = "disable")
                btn_get_library_path.configure(state = "disable")
            elif combo_document_type.get() == "*.spw":
                entry_library_path.configure(state = "normal")
                btn_get_library_path.configure(state = "normal")


        def open_lib_file(event):
            file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Открыть файл библиотеки",
                                           filetypes=[("Библиотека оформлений", "*.lyt")])
            file_path = file_path.replace("/", "\\")
            entry_library_path.delete(0, tk.END)
            entry_library_path.insert(0, file_path)



        tk.Label(self, text = "Общая масса равна: ").grid(row = 0, column = 0, pady = 5, stick = "w")
        tk.Label(self, text = "Путь к библиотеке стилей: ").grid(row = 2, column = 0)
        
        entry_library_path = ttk.Entry(self)
        entry_library_path.grid(row = 2, column = 1, stick = "we")
        entry_library_path.insert(0, lib_path)

        btn_get_library_path = ttk.Button(self, text = "...", width = 3)
        btn_get_library_path.grid(row = 2, column = 2)
        btn_get_library_path.bind("<Button-1>", open_lib_file)

        tk.Label(self, text = "Тип документа: ").grid(row = 1, column = 0, stick = "w")
        combo_document_type = ttk.Combobox(self, values = document_types)
        combo_document_type.grid(row = 1, column = 1, columnspan = 2, stick = "we")
        combo_document_type.current(1)
        combo_document_type.bind("<<ComboboxSelected>>", change_entry_state)

        btn_get_mass = ttk.Button(self, text = "Рассчитать массу").grid(row = 3, column = 0, stick = "w", padx = 5, pady = 10)
        cbtn_need_to_delete = tk.Checkbutton(self, text = "Удалять лишние строки",
                            variable = need_to_delete_value,
                            offvalue = 0, 
                            onvalue = 1).grid(row = 3, column = 1)



if __name__ == '__main__':
    root = Application()
    root.mainloop()
