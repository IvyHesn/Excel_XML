from pyexcelerate import Workbook

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # data is a 2D array

wb = Workbook("output.xlsx")
wb.new_sheet("sheet111 name", data=data)
wb.save("output.xlsx")