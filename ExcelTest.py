import xlwt
from xlwt import Workbook
ans='y'
i=0
j=0
while ans=='y':
  i=i+1
  j=j+1
  name=input("Enter name")
  age=input("Enter age")
  wb = Workbook()
  sheet1 = wb.add_sheet('Sheet 1')
  sheet1.write(i, 0, name)
  sheet1.write(j, 1, age)
  wb.save('example.xls')
# Workbook is created
  print("y/n")
  ans=input()

