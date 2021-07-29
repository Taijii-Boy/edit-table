# -*- coding: utf-8 -*-
#|1

import pythoncom, pyperclip
from win32com.client import Dispatch, gencache
import tkinterWind as tw
from tkinter import messagebox
import os

class Main_logic():

	def __init__(self):
		self.app = tw.Application() # Подключаем UI
		self.status_open_document = self.get_Kompas() # Пробуем подключиться к компасу
		self.change_status_in_app() # Отображаем статус компаса в приложении
		self.app.btn_get_mass.configure(command = self.get_mass)

	
	def get_Kompas(self):
		#  Подключим константы API Компас
		self.const = gencache.EnsureModule("{75C9F5D0-B5B8-4526-8681-9903C567D2ED}", 0, 1, 0).constants
		self.const_3d = gencache.EnsureModule("{2CAF168C-7961-4B90-9DA2-701419BEEFE3}", 0, 1, 0).constants

		#  Подключим описание интерфейсов API5
		self.KAPI = gencache.EnsureModule("{0422828C-F174-495E-AC5D-D31014DBBE87}", 0, 1, 0)
		self.iKompasObject = self.KAPI.KompasObject(Dispatch("Kompas.Application.5")._oleobj_.QueryInterface(self.KAPI.KompasObject.CLSID, pythoncom.IID_IDispatch))

		#  Подключим описание интерфейсов API7
		self.KAPI7 = gencache.EnsureModule("{69AC2981-37C0-4379-84FD-5DD2F3C0A520}", 0, 1, 0)
		self.application = self.KAPI7.IApplication(Dispatch("Kompas.Application.7")._oleobj_.QueryInterface(self.KAPI7.IApplication.CLSID, pythoncom.IID_IDispatch))

		#  Получим активный документ
		self.iDocument = self.application.ActiveDocument

		if self.iDocument:
			return True # Компас запущен
		else:
			close_Kompas_process()
			return False # Компас не запущен
	

	def close_Kompas_process(self, program = "KOMPAS.exe"): # Принудительно убиваем процесс после закрытия
		os.system("TASKKILL /F /IM " + program) 


	def change_status_in_app(self):
		if self.status_open_document:
			self.app.label_status.configure(text = "Открыт", fg = "green")
		else: 
			self.app.label_status.configure(text = "Закрыт", fg = "red")
	

	def get_mass(self):
		if self.app.combo_document_type.get() == "*.cdw":
			self.get_mass_from_cdw()
		elif self.app.combo_document_type.get() == "*.spw":
			self.get_mass_from_spw()
		elif self.app.combo_document_type.get() == "Служебка":
			self.get_mass_from_table()


	# Функция, меняющая запятую в значениях на точку
	def point(self, text):
		text = text.replace(',','.')
		return text


	# Функция, меняющая запятую в значениях на точку
	def comma(self, text):
		text = text.replace('.',',')
		return text


	def get_mass_from_cdw(self):

		specification_date = ()

		# Функция получения данных из колонок спецификации
		def get_data_for_cdw():
			sp_obozn = []
			sp_naim = []
			sp_col = []
			sp_mass = []
			sp_date = ()

			count = iLayoutSheets.Count + 1 # Количество листов + 1 для цикла 
			
			for sheet_num in range(1, count): # Перебираем листы 
				iLayoutSheet = iLayoutSheets.ItemByNumber(sheet_num)
				iStamp = iLayoutSheet.Stamp

				for i in range(1014, 1225, 10): # Обозначение
					iObozn = iStamp.Text(i)
					sp_obozn.append(iObozn.Str)

				for i in range(1015, 1226, 10): # Наименование
					iNaim = iStamp.Text(i)
					sp_naim.append(iNaim.Str)

				for i in range(3011, 3222, 10): # Количество
					iCol = iStamp.Text(i)
					sp_col.append(iCol.Str)

				for i in range(1019, 1230, 10): # Масса
					iMass = iStamp.Text(i)
					sp_mass.append(iMass.Str)

			sp_date = (sp_obozn, sp_naim, sp_col, sp_mass)
			return sp_date

		# Функция подсчета массы 
		def get_mass_cdw(sp_date):
			mass = 0.000
			sp_obozn, sp_naim, sp_col, sp_mass = sp_date 

			for i in range (0, len(sp_naim)):
				if sp_naim[i] == "Сборочный чертеж":
					pass
				elif sp_obozn[i] == '' and sp_naim[i] == '': # пропускаем пустые строки
					continue
				elif sp_mass[i] != '' and sp_col[i] != '':
					mass = mass + float(self.point(sp_mass[i]))*float(sp_col[i])
				elif sp_mass[i] != '' and sp_col[i] == '':
					mass = mass + float(self.point(sp_mass[i]))
			return mass
		
		iLayoutSheets = self.iDocument.LayoutSheets
		specification_date = get_data_for_cdw() # Считываем данные спецификации
		mass = round(get_mass_cdw(specification_date), 3) # Считаем массу и округляем до 4 знаков после запятой
		mass = self.comma(str(mass)) # Меняем точку на запятую для вывода
		self.app.label_mass_result.configure(text = f"{mass} кг", font = ("Arial", 10, "bold")) # Выводим в приложение
		pyperclip.copy(mass) # Копируем в буфер обмена


	def get_mass_from_spw(self):
		pass


	def get_mass_from_table(self):
		pass

a = Main_logic()
