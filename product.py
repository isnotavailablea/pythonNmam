import main as ma
import xlsxwriter

dictcopy=ma.maindict.copy()
totalpeople=0#This is the number of all the people
agewt={}
others={}
for key in dictcopy["ageGroups"]:
    totalpeople+=dictcopy["ageGroups"][key]["value"]

for key in dictcopy["ageGroups"]:
    agewt[key]=round(dictcopy["ageGroups"][key]["value"]/totalpeople,3)

for keys in dictcopy["ageGroups"]:
    for otherkeys in dictcopy["ageGroups"][keys]["others"]:
        if otherkeys in others:
            others[otherkeys]+=dictcopy["ageGroups"][keys]["others"][otherkeys]
        else:
            others[otherkeys]=dictcopy["ageGroups"][keys]["others"][otherkeys]

for keys in others:
    others[keys]=round(others[keys]/totalpeople,3)

for keys in others:
    print(keys,"=",others[keys])

#list of columns name
l=["agebucket","agewt","ECG-1","ECG-0","CKMB-0","CKMB-1","Chest_Pain-0","Chest_Pain-1","Chest_Pain-2","Diabetic-0","Diabetic-1","PHF /family history-0","PHF /family history-1","Cholesterol-0","Cholesterol-1"]

#UPLOADING INTO THE XL-SHEET
workbook=xlsxwriter.Workbook('finalprod.xlsx')
worksheet=workbook.add_worksheet()
totalrows=0
for index,i in enumerate(l):
    if i=="agebucket":
        worksheet.write(0,0,i)
        row=1
        for keys in agewt:
            worksheet.write(row,0,keys)
            row+=1
        totalrows=row
    elif i=="agewt":
        worksheet.write(0,1,i)
        row=1
        for value in agewt:
            worksheet.write(row,1,agewt[value])
            row+=1
    else:
        worksheet.write(0,index,i)
        for j in range(1,totalrows):
            worksheet.write(j,index,others[i])


workbook.close()

