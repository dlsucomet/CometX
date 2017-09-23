import xlwt
from datetime import datetime
import time

#blank spreadsheet file
wb = xlwt.Workbook()


#Create sheet
ws = wb.add_sheet('COMET Attendance tracker')
col_2 = ws.col(1)
col_2.width = 256*30

col_3 = ws.col(2)
col_3.width = 256*30

col_4 = ws.col(3)
col_4.width = 256*30

#write on sheet
boldtext = xlwt.Font()
boldtext.colour_index = 0
boldtext.bold = True
label = xlwt.XFStyle()
label.font = boldtext


ws.write(0,0,'DATE', label)
ws.write(2,1,'NAME', label)
ws.write(2,2,'TIME-IN', label)
ws.write(2,3,'TIME-OUT', label)

#fonts and styles
font = xlwt.Font()
font.name = 'Times New Roman'
font.colour_index = 2
font.bold = True

font1 = xlwt.Font()
font1.name = 'Times New Roman'
font1.colour_index = 0
font1.bold = False

#Date format
style = xlwt.XFStyle()
style.num_format_str = 'D-MMMM-YY'
style.font = font

#Time format
style1 = xlwt.XFStyle()
style1.num_format_str = 'h:mm:ss AM/PM'
style1.font = font1

ws.write(0,1, datetime.today(), style)
ws.write(3,2, datetime.time(datetime.now()), style1)
ws.write(3,3, datetime.time(datetime.now()), style1)

#save
wb.save('writing.xls')
