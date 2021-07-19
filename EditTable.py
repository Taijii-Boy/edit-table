# -*- coding: utf-8 -*-
#|1

import pythoncom
from win32com.client import Dispatch, gencache

#  ��������� ��������� API ������
const = gencache.EnsureModule("{75C9F5D0-B5B8-4526-8681-9903C567D2ED}", 0, 1, 0).constants
const_3d = gencache.EnsureModule("{2CAF168C-7961-4B90-9DA2-701419BEEFE3}", 0, 1, 0).constants

#  ��������� �������� ����������� API5
KAPI = gencache.EnsureModule("{0422828C-F174-495E-AC5D-D31014DBBE87}", 0, 1, 0)
iKompasObject = KAPI.KompasObject(Dispatch("Kompas.Application.5")._oleobj_.QueryInterface(KAPI.KompasObject.CLSID, pythoncom.IID_IDispatch))

#  ��������� �������� ����������� API7
KAPI7 = gencache.EnsureModule("{69AC2981-37C0-4379-84FD-5DD2F3C0A520}", 0, 1, 0)
application = KAPI7.IApplication(Dispatch("Kompas.Application.7")._oleobj_.QueryInterface(KAPI7.IApplication.CLSID, pythoncom.IID_IDispatch))

#  ������� �������� ��������
iDocument = application.ActiveDocument
iKompasDocument2D = KAPI7.IKompasDocument2D(iDocument)
iDocument2D = iKompasObject.ActiveDocument2D()
iKompasDocument2D1 = KAPI7.IKompasDocument2D1(iKompasDocument2D)
iSelectionManager = iKompasDocument2D1.SelectionManager	
selected_object = iSelectionManager.SelectedObjects

iTable = KAPI7.ITable(selected_object)
print(iTable.ColumnsCount)
print(iTable.RowsCount)
iTable.AddColumn(1, True)
iTable.AddRow(1, True)






# iTableCell = iTable.Cell


# in_cell = iTable.CellById(2)

# columns = iTable.ColumnsCount
# rows = iTable.RowsCount
# print("columns: ", columns)
# print("rows: ", rows)


# iViewsAndLayersManager = iKompasDocument2D.ViewsAndLayersManager
# iViews = iViewsAndLayersManager.Views
# iView = iViews.ActiveView
# iSymbols2DContainer = KAPI7.ISymbols2DContainer(iView)
# iDrawingTables = iSymbols2DContainer.DrawingTables
# iDrawingTable = iDrawingTables.DrawingTable(1) # ����� �������� �������. �����������?
# print("iDrawing: ", iDrawingTable)
# print("Selected: ", selected_object)

