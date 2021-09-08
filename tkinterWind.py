 # -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
import os
from tkinter import filedialog
from configparser import ConfigParser
from PIL import Image as PilImage
from PIL import ImageTk
import configuration_window as cw


class Application(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.config = ConfigParser()
        self.create_config_file()
        self.set_ui()
        self.set_widgets()


    # def create_configuration_window(self):
    #     cw.configuration_window(self)


    def set_ui(self):
        self.title("Расчет массы v.1.2")
        self.resizable(False, False) # Возможность изменения размера по ширине и по высоте


    def create_config_file(self):
        if not os.path.exists('config.ini'):
            self.config['DEFAULT'] = {'path':'C:\\LYT\\GRAPHICIL.LYT', 'rows_to_del':'1111, 2222'}
            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)


    def save_configuration(self):
        self.config.read('config.ini')
        self.config.set('DEFAULT', 'path', self.entry_library_path.get())
        with open("config.ini", "w") as configfile:
            self.config.write(configfile)
       

    def load_configuration(self):
        self.config.read('config.ini')
        path = self.config.get('DEFAULT', 'path')
        rows_to_del = (self.config.get('DEFAULT', 'rows_to_del')).split(", ")
        return path, rows_to_del


    def change_configuration(self):
        cw.configuration_window(self)


    def set_widgets(self):
        document_types = ("*.cdw", "*.spw", "Служебка")
        self.need_to_delete_value = tk.IntVar()
        self.lib_path, self.rows_to_del = self.load_configuration()


        def change_entry_state(event):
            if  self.combo_document_type.get() == "*.cdw":
                self.entry_library_path.configure(state = "disable")
                btn_get_library_path.configure(state = "disable")
                self.cbtn_need_to_delete.configure(state = "disable")
            elif self.combo_document_type.get() == "*.spw":
                self.entry_library_path.configure(state = "normal")
                btn_get_library_path.configure(state = "normal")
            elif self.combo_document_type.get() == "Служебка":
                self.entry_library_path.configure(state = "disable")
                btn_get_library_path.configure(state = "disable")
                self.cbtn_need_to_delete.configure(state = "normal")


        def open_lib_file():
                file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Открыть файл библиотеки",
                                                    filetypes=[("Библиотека оформлений", "*.lyt")])
                if file_path:
                    file_path = file_path.replace("/", "\\")
                    self.entry_library_path.delete(0, tk.END)
                    self.entry_library_path.insert(0, file_path)


        self.label_mass = tk.Label(self, text = "Общая масса равна: ")
        self.label_mass.grid(row = 0, column = 0, pady = 6, stick = "w")

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
        self.entry_library_path.insert(0, self.lib_path)

        btn_get_library_path = ttk.Button(self, text = "...", width = 3, command = open_lib_file)
        btn_get_library_path.grid(row = 3, column = 2)

        configuration_icon = PilImage.open(r"images/settings.png")
        configuration_icon = configuration_icon.resize((18, 18), PilImage.ANTIALIAS)
        self.conf_icon = ImageTk.PhotoImage(configuration_icon)
        btn_change_configuration = ttk.Button(self, width = 3, image = self.conf_icon,
                                             command = self.change_configuration)
        btn_change_configuration.grid(row = 4, column = 2)

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
