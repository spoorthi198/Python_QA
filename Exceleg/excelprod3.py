import openpyxl as xl

wb = xl.Workbook()
sheet1 = wb.active
sheet1.title="sdate"
sheet1['A3'].value="Rajendra"
sheet = wb.create_sheet('Reports')
sheet['A1'].value = "spoorthi"
wb.save('python.xlsx')
