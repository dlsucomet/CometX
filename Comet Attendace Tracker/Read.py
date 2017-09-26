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

continue_reading = True
########################################################################################
#fonts and styles
boldtext = xlwt.Font()
boldtext.colour_index = 0
boldtext.bold = True
label = xlwt.XFStyle()
label.font = boldtext

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
##########################################################################################
#Read list from excel file
database = xlrd.open_workbook('DB.xlsx')
data_sheet = database.sheet_by_name('Master List')
id_num = 0

def check_List(uid): #Checks if the uid is part of the database
    column = data_sheet.col_values(colx=1, start_rowx=1)

    if (str(uid)[1:-1]) in list(column):
        return True
    else:
        return False

def create_attendace_sheet(uid): #Use only ONCE per day
    attendance = xlwt.Workbook()
    date_now = datetime.today()
    day = str(calendar.day_name[date_now.weekday()])

    ws = attendance.add_sheet(day)

    row = 2
    col = 1

    #Resize Columns
    col_2 = ws.col(1)
    col_2.width = 256*30
    col_3 = ws.col(2)
    col_3.width = 256*30
    col_4 = ws.col(3)
    col_4.width = 256*30
    col_5 = ws.col(4)
    col_5.width = 256*30

    #Add Column Labels
    ws.write(0,0,'DATE', label)
    ws.write(0,1, datetime.today(), style)
    ws.write(row,1,'ID', label
    ws.write(row,2,'NAME', label)
    ws.write(row,3,'TIME-IN', label)
    ws.write(row,4,'TIME-OUT', label)

    attendance.save(day+' '+'Attendance.xlsx')

def get_Id(uid): #Gets the ID number of the comet member
    uid_column = data_sheet.col_values(colx=1, start_rowx=1)
    id_column = data_sheet.col_values(colx=3, start_rowx=1)

    if (str(uid)[1:-1]) in list(uid_column):
        uid_temp = list(uid_column).index(str(uid)[1:-1])
        return int(list(id_column)[uid_temp])
    else:
        return False

def user_log(uid, row): #Writes the time in and time out of the uid
    print('False')

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

        # Print UID
        print "Card read UID: "+str(uid)
        check_List(uid)
        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]

        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)

        # Authenticate
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

        # Check if authenticated
        if status == MIFAREReader.MI_OK:
            MIFAREReader.MFRC522_Read(8)
            MIFAREReader.MFRC522_StopCrypto1()
       # else:
            #print "Authentication error"


        #delay
        time.sleep(2)
