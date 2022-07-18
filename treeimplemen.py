import openpyxl

path="finalprod.xlsx"
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active
cell_obj = sheet_obj.cell(row=1, column=1)
maxrow=sheet_obj.max_row
maxcolumn=sheet_obj.max_column

class Head:
    def __init__(self,next):
        self.next=[]