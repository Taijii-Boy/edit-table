# -*- coding: utf-8 -*-
#|1

import pythoncom, pyperclip
from win32com.client import Dispatch, gencache

#  Подключим константы API Компас
const = gencache.EnsureModule("{75C9F5D0-B5B8-4526-8681-9903C567D2ED}", 0, 1, 0).constants
const_3d = gencache.EnsureModule("{2CAF168C-7961-4B90-9DA2-701419BEEFE3}", 0, 1, 0).constants

#  Подключим описание интерфейсов API5
KAPI = gencache.EnsureModule("{0422828C-F174-495E-AC5D-D31014DBBE87}", 0, 1, 0)
iKompasObject = KAPI.KompasObject(Dispatch("Kompas.Application.5")._oleobj_.QueryInterface(KAPI.KompasObject.CLSID, pythoncom.IID_IDispatch))

#  Подключим описание интерфейсов API7
KAPI7 = gencache.EnsureModule("{69AC2981-37C0-4379-84FD-5DD2F3C0A520}", 0, 1, 0)
application = KAPI7.IApplication(Dispatch("Kompas.Application.7")._oleobj_.QueryInterface(KAPI7.IApplication.CLSID, pythoncom.IID_IDispatch))

#  Получим активный документ
iDocument = application.ActiveDocument
iKompasDocument2D = KAPI7.IKompasDocument2D(iDocument)
iDocument2D = iKompasObject.ActiveDocument2D()
iKompasDocument2D1 = KAPI7.IKompasDocument2D1(iKompasDocument2D)


# Функция считывает таблицу построчно, возвращает списки строк в rows_in_table
def get_rows_from_table():
    rows_in_table = []
    current_row = []
    for row in range(2, iTable.RowsCount):
        for column in range(3, 8):
            iTableCell = iTable.Cell(row, column)
            iTextObject = iTableCell.Text
            iText = iTextObject._oleobj_.QueryInterface(KAPI7.IText.CLSID, pythoncom.IID_IDispatch)
            iText = KAPI7.IText(iText)
            current_row.append(iText.Str)
        rows_in_table.append(current_row)
        current_row = []
    return rows_in_table


# Функция удаляет пустые строки
def del_empty_rows(table_list):
    emty_template = ["", "", "", "", ""]
    for row in table_list:
        if row == emty_template:
            table_list.remove(row)
    return table_list


# Функция, меняющая запятую в значениях на точку
def point(text):
    text = text.replace(',','.')
    return text


# Функция, меняющая точку в значениях на запятую
def comma(text):
    text = text.replace('.',',')
    return text


# Функция подсчета массы 
# 0 - Обозначение, 1 - Наименование, 2 - Кол на сборке, 3 - Количество на изд, 4 - Масса
def get_mass(table_list):
    mass = 0.000
    mass_increase = True # Флаг, показывающий, суммировать массу или вычитать
    for row in table_list:
        if row[1] == "Изменение массы":
            continue
        elif row[1] == "Снять" or row[1] == "снять":
            mass_increase = False # Массу будем вычитать
        elif row[1] == "Добавить" or row[1] == "добавить":
            mass_increase = True # Массу будем складывать
        elif row[4] != "" and row[3] != "":
            if mass_increase:
                mass = mass + float(point(row[4]))*float(row[3])
            else:
                mass = mass - float(point(row[4]))*float(row[3])
        elif row[4] != "" and row[3] == "":
            if mass_increase:
                mass = mass + float(point(row[4]))
            else:
                mass = mass - float(point(row[4]))
    return mass


# Функция вывода результата на экран и в буфер обмена
def get_result(mass):
    if mass > 0:
        mass = comma(str(mass)) # Меняем точку на запятую для вывода
        iKompasObject.ksMessage("Изменение массы: +" + mass + " кг") # Выдаем сообщение в компасе
        pyperclip.copy(f"+{mass}") # Копируем в буфер обмена
    else:
        mass = comma(str(mass)) # Меняем точку на запятую для вывода
        iKompasObject.ksMessage("Изменение массы: " + mass + " кг") # Выдаем сообщение в компасе
        pyperclip.copy(mass) # Копируем в буфер обмена


# Удаляем из таблицы лишние строки
def clear_table():
    rows_to_delete = []
    iDrawingObject = KAPI7.IDrawingObject(iTable)
    for row in range(2, iTable.RowsCount): # Проходим по всем строкам, не включая шапку
        for column in (4, 6, 8):
            if column == 6:
                iTableCell = iTable.Cell(row, column) # 6 - Номер колонки с количеством на изделии
                iTextObject = iTableCell.Text
                iText = iTextObject._oleobj_.QueryInterface(KAPI7.IText.CLSID, pythoncom.IID_IDispatch)
                iText = KAPI7.IText(iText)
                iText = iText.Str
                if iText in ("111", "222", "1111", "2222"):
                    rows_to_delete.append(iTableCell.Row) # Создаем список строк, которые необходимо удалить
    first_iter = True
    j = 1
    for r in rows_to_delete:
        if first_iter:
            iTable.DeleteRow(r) # Удаляем строки
            first_iter = False
        else:
            iTable.DeleteRow(r - j) # Учитываем удаленные строки в списке rows_to_delete 
            j += 1
    iDrawingObject.Update() # Обновляем графический объект


# MAIN

# Получаем выделенную таблицу
total_mass = 0.000

iSelectionManager = iKompasDocument2D1.SelectionManager 
selected_object = iSelectionManager.SelectedObjects

if type(selected_object) != tuple and (selected_object == None or selected_object.Type != 13062): # Если ничего не выделили или выделена не таблица
    iKompasObject.ksMessage("Выделите таблицу и перезапустите программу")
    exit()
elif type(selected_object) == tuple:
    for sel_object in selected_object:
        if sel_object.Type == 13062: # Если в выделенных элементах присутствует Таблица
            iTable = KAPI7.ITable(sel_object)
            rows_in_table = get_rows_from_table() # Получаем списком данные из таблицы
            clear_table() # Удаляем лишние строки
            rows_in_table = get_rows_from_table() # Повторно запрашиваем данные очищенной таблицы
            rows_in_table = del_empty_rows(rows_in_table) # Удаляем лишние строки
            mass = round(get_mass(rows_in_table), 3) # Считаем массу и округляем до 3 знаков после запятой
            total_mass = total_mass + mass
        else:
            continue # Пропускаем все выделенные объекты кроме таблиц
    total_mass = round(total_mass, 3) # Округляем до 3 знаков после запятой
    get_result(total_mass)  # Выводим результат
    exit()

# Если выделена одна таблица
iTable = KAPI7.ITable(selected_object)
rows_in_table = get_rows_from_table() # Получаем списком данные из таблицы
clear_table() # Удаляем лишние строки
rows_in_table = get_rows_from_table() # Повторно запрашиваем данные очищенной таблицы
rows_in_table = del_empty_rows(rows_in_table) # Удаляем лишние строки
mass = round(get_mass(rows_in_table), 3) # Считаем массу и округляем до 3 знаков после запятой
get_result(mass) # Выводим результат
