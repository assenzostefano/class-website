import openpyxl as xl

#using read_excel() method to read our excel file and storing the same in the variable named "df "
workbook = xl.load_workbook(filename="test.xlsx")

ws = workbook.active

# row 4
for row in range (1, 100):
    # column B ~ column F
    for column in range (1, 100):
        cell = ws.cell(row, column)
        if cell.value == "2elci":
            print(ws.cell(row=cell.row, column=column).value)
            print(cell.row, column)
            #Search school time table
            for i in range(4,50):
                print(ws.cell(row=i, column=column).value)
            for i in range(4, 55):
                print(print(ws.cell(row=i, column=column+1).value))
                column = column