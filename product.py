import main
import xlsxwriter
newdict={}
for keys in main.maindict["ageGroups"]:
    for mainkeys in main.maindict["ageGroups"][keys]["others"]:
        newdict[mainkeys]=1
for keys in newdict:
    print(keys)
print(main.maindict["ageGroups"]["26-30"]["others"]["ECG-1"]/main.maindict["ageGroups"]["26-30"]["value"])