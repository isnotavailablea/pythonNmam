import openpyxl

path="Male-MI-0_Cluster.xlsx"
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active
cell_obj = sheet_obj.cell(row=1, column=1)
maxrow=sheet_obj.max_row
maxcolumn=sheet_obj.max_column

class Headnode:
    def __init__(self, name,childrennum=maxrow-1):
        self.name = name
        self.next = []
        for i in range(childrennum):
            self.next.append(None)
head=Headnode("agecat")
class Node:
    def __init__(self,name,value,children=2):
        self.name=name
        self.value=value
        self.next=[]
        for i in range(children):
            self.next.append(None)


def addfirstlayer():
    for i in range(maxrow):
        if head.next[i]==None:
            head.next[i]=Node(sheet_obj.cell(row=i+1,column=1).value,sheet_obj.cell(row=i+1,column=2))
    return



