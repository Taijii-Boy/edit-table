# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
import os
from tkinter import filedialog


class Application(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.set_ui()
        self.set_widgets()

    def set_ui(self):
        self.title("Расчет массы Компас 3D v.0.1")
        # self.geometry(f"{root_width}x{root_height}+1200+200")
        self.resizable(False, False) # Возможность изменения размера по ширине и по высоте

    def set_widgets(self):

        document_types = ("*.cdw", "*.spw", "Служебка")
        self.need_to_delete_value = tk.IntVar()
        lib_path = "C:\\LYT\\GRAPHICIL.LYT"

        def change_entry_state(event):
            if  self.combo_document_type.get() == "*.cdw" or self.combo_document_type.get() == "Служебка":
                self.entry_library_path.configure(state = "disable")
                btn_get_library_path.configure(state = "disable")
            elif self.combo_document_type.get() == "*.spw":
                self.entry_library_path.configure(state = "normal")
                btn_get_library_path.configure(state = "normal")


        def open_lib_file():
                file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Открыть файл библиотеки",
                                                    filetypes=[("Библиотека оформлений", "*.lyt")])
                if file_path:
                    file_path = file_path.replace("/", "\\")
                    self.entry_library_path.delete(0, tk.END)
                    self.entry_library_path.insert(0, file_path)

        
        self.label_mass = tk.Label(self, text = "Общая масса равна: ")
        self.label_mass.grid(row = 0, column = 0, pady = 5, stick = "w")

        tk.Label(self, text = "Путь к библиотеке стилей: ").grid(row = 3, column = 0)
        self.label_mass_result = tk.Label(self, text = "")
        self.label_mass_result.grid(row = 0, column = 1, pady = 5, stick = "w")
        
        tk.Label(self, text = "Компас документ:").grid(row = 1, column = 0, stick = "w")
        self.label_status = tk.Label(self, text = "Закрыт", fg = "red")
        self.label_status.grid(row = 1, column = 1, stick = "w")

        tk.Label(self, text = "Тип документа: ").grid(row = 2, column = 0, stick = "w")
        self.combo_document_type = ttk.Combobox(self, values = document_types)
        self.combo_document_type.grid(row = 2, column = 1, columnspan = 2, stick = "we")
        self.combo_document_type.current(1)
        self.combo_document_type.bind("<<ComboboxSelected>>", change_entry_state)

        self.entry_library_path = tk.Entry(self)
        self.entry_library_path.grid(row = 3, column = 1, stick = "we")
        self.entry_library_path.insert(0, lib_path)

        btn_get_library_path = ttk.Button(self, text = "...", width = 3, command = open_lib_file)
        btn_get_library_path.grid(row = 3, column = 2)

        self.btn_get_mass = ttk.Button(self, text = "Рассчитать массу")
        self.btn_get_mass.grid(row = 4, column = 0, stick = "w", padx = 5, pady = 10)
        self.cbtn_need_to_delete = tk.Checkbutton(self, text = "Удалять лишние строки",
                            variable = self.need_to_delete_value,
                            offvalue = 0, 
                            onvalue = 1)
        self.cbtn_need_to_delete.grid(row = 4, column = 1)


if __name__ == '__main__':
    root = Application()
    root.mainloop()
