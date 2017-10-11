#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import xlwt, xlrd
import time
from datetime import datetime
import calendar
from xlutils.copy import copy

####################### STYLES #################################
########################################################################################
#BOLD Font
boldtext = xlwt.Font()
boldtext.colour_index = 0
boldtext.bold = True
label = xlwt.XFStyle()
label.font = boldtext

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
style.num_format_str = 'D-MMMM-YYYY'
style.font = font
#Time format
style1 = xlwt.XFStyle()
style1.num_format_str = 'h:mm:ss AM/PM'
style1.font = font1


def check_List(uid): 
################################################################
#Checks if the uid is part of the database
################################################################
	database = xlrd.open_workbook('DB.xlsx')
	data_sheet = database.sheet_by_name('Master List')
	column = data_sheet.col_values(colx=1, start_rowx=1)

	if (str(uid)[1:-1]) in list(column):
		return True
	else:
		return False
	

def register_member(uid):	
################################################################
#Register a new member by entering the name, and id number
################################################################
	pass
	
def create_attendace_sheet(uid):
################################################################
#Create the Initial Sheet to be updated during the day. This is
#used once per day 	
#This function saves the file as the '<weekday> Attendance.xlsx'
################################################################
	attendance = xlwt.Workbook()
	date_now = datetime.today()
	day = str(calendar.day_name[date_now.weekday()])

	ws = attendance.add_sheet(day)

	row = 2
	col = 1

	#Resize Columns
	col_2 = ws.col(1)
	col_2.width = 256*30
	col_2 = ws.col(2)
	col_2.width = 256*30
	col_2 = ws.col(3)
	col_2.width = 256*30
	col_2 = ws.col(4)
	col_2.width = 256*30

	#Add Column Labels
	ws.write(0,0,'DATE', label)
	ws.write(0,1, datetime.today(), style)
	ws.write(row,1,'ID', label)
	ws.write(row,2,'NAME', label)
	ws.write(row,3,'TIME-IN', label)
	ws.write(row,4,'TIME-OUT', label)
	ws.write(row,5,'DURATION', label)
	
	#Copy all names to attendance sheet
	database = xlrd.open_workbook('DB.xlsx')
	data_sheet = database.sheet_by_name('Master List')
	id_column = list(data_sheet.col_values(colx=3, start_rowx=1))
	name_column = list(data_sheet.col_values(colx=2, start_rowx=1))
	
	#Move all to attendance sheet
	for row in range(3, len(id_column)):
		ws.write(row, 1, id_column[row-2])
		ws.write(row, 2, name_column[row-2])
		
	attendance.save(day+' '+'Attendance.xls')

def get_Id(uid): #Gets the ID number of the comet member
################################################################
#Get the id of the member in DB.xlsx
################################################################
	pass

def get_row(uid):
################################################################
#Returns the row to be updated by the user_log() function
#This will tell the program which cell should it write on
################################################################
	pass

		
def user_log(uid):  	
################################################################
#Writes the time in and time out of the uid
#Taps are considered as in or out
#If tap in is greater then tap out, then the type of tap is out.
#If tap out is greater than than tap in, then the type of tap is in.
#Total is tap out - tap in, only in tapo outs
#Use military time to compare tap ins and tap outs
################################################################
	#Date
	date_now = datetime.today()
	day = str(calendar.day_name[date_now.weekday()])
	
	attendance = xlrd.open_workbook(day+' '+'Attendance.xls')

	if check_List(uid) == True:
		file = copy(attendance)
		attend_sheet = file.get_sheet(0)
		####Column Width
		col_2 = attend_sheet.col(1)
		col_2.width = 256*30
		col_2 = attend_sheet.col(2)
		col_2.width = 256*30
		col_2 = attend_sheet.col(3)
		col_2.width = 256*30
		col_2 = attend_sheet.col(4)
		col_2.width = 256*30
		col_2 = attend_sheet.col(5)
		col_2.width = 256*30
		####Text format
		attend_sheet.write(0,0,'DATE', label)
		attend_sheet.write(0,1, datetime.today(), style)
		attend_sheet.write(2,1,'ID', label)
		attend_sheet.write(2,2,'NAME', label)
		attend_sheet.write(2,3,'TIME-IN', label)
		attend_sheet.write(2,4,'TIME-OUT', label)
		attend_sheet.write(2,5,'DURATION', label)
		################################################
		row = 2 + get_row(uid)
		
		attend_sheet.write(row, 3, datetime.now(), style1)
		#Save
		file.save(day+' '+'Attendance.xls')
	else: 
		print ('Warning! Not a member')

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:

    # Scan for cards
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"

    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        pass

        #delay
        time.sleep(2)
