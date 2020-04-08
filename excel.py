from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active  # get current active sheet
print(ws)
ws = wb.create_sheet('Mysheet')  # create a new sheet with title Mysheet
ws.title = 'first title'  # changes the title to first title
ws.sheet_properties.tabColor = "1072BA"



ws['A1'] = 42
ws['A2'] = 40
cell1 = ws['A1']
print(cell1.value)

d = ws.cell(row=4, column=2, value=10)
print(d.value)

ws.append([1, 2, 3]) # appends this list to fifth row because of cursor state
cell_range = ws['A1':'C2']

print(cell_range)
print([j.value for i in cell_range for j in i])

col = ws['C']
col_range = ws['C:D']
row10 = ws[10]
row_range = ws[5:10]

ws['A3'] = '=SUM(A1, A2)'

wb.save('balances.xlsx')


workbook = load_workbook(filename='test.xlsx')
print(workbook.sheetnames)
print(workbook.worksheets)
ws = workbook['فاتحیC1']
print(ws['b7'].value)

for i in range(4,27):
    print(ws['B'+str(i)],'    ',ws['B'+str(i)].value)