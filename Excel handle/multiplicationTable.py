import openpyxl , sys
from openpyxl.styles import Font
from pathlib import Path
if len(sys.argv) == 2:
    
    try:
        number = int(sys.argv[1])
        
    except Exception as e:
        print(e)   
         
    excelFile = openpyxl.Workbook()
    sheet = excelFile.active 
    
    for y in range(number +1):
        for x in range(number + 1 ):
            isHeader = False 
            if x ==0 and y == 0:
                isHeader = True
                n = ''
            elif x == 0:
                isHeader = True
                n = y
            elif y == 0 :
                isHeader = True
                n = x
            else: 
                n = x*y
            cell = sheet.cell(row=y+1, column=x + 1)
            
            if isHeader:
                cell.font = Font(bold=True)
            cell.value = n
    savedFile = str(Path("D:\\Code\\Husoub Academy\\Python\\PythonLearning\\Excel handle") / 'multiplication_table_') + str(number) + '.xlsx'
    excelFile.save(savedFile)
    print('Saved as ' + savedFile)

else:
    print('Please enter only two arguments')


