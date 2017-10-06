#!/usr/bin/env python
# -*- coding: utf8 -*-
import os
import RPi.GPIO as GPIO
import MFRC522
import signal
import xlwt, xlrd
import time
from datetime import datetime
from xlutils.copy import copy

continue_reading = True
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

#Header of DB.xlsx
database = xlrd.open_workbook('DB.xlsx')
file = copy(database)
sheet = file.get_sheet(0)


file.save('DB.xlsx')

##########################################################################################
#Read list from excel file

id_num = 0
def check_List(uid): #Checks if the uid is part of the database
    database = xlrd.open_workbook('DB.xlsx')
    data_sheet = database.sheet_by_name('Master List')
    column = data_sheet.col_values(colx=1, start_rowx=1)
    
    if (str(uid)[1:-1]) in list(column):
        print "You are already registered! Wag ka na!"
        time.sleep(1)
        os.system("clear")
        print "Scan your ID to register!"
        return True
    else:
        print "New ID detected!"
        file = copy(database)
        sheet = file.get_sheet(0)
        ####Column Width
        col_2 = sheet.col(1)
        col_2.width = 256*30
        col_2 = sheet.col(2)
        col_2.width = 256*30
        col_2 = sheet.col(3)
        col_2.width = 256*30
        ####Text format
        sheet.write(0,0,'#',label)
        sheet.write(0,1,'UID',label)
        sheet.write(0,2,'Name',label)
        sheet.write(0,3,'ID Number',label)
        #######################################
        name = str(raw_input("NAME (ex. Brandon Teh): "))
        ID_num = str(raw_input("Enter ID number: "))
        if(not(name=="" or ID_num=="")):
            sheet.write(len(column)+1,0,str(len(column)+1))
            sheet.write(len(column)+1,1,str(uid)[1:-1])
            sheet.write(len(column)+1,2,name)
            sheet.write(len(column)+1,3,ID_num)
        file.save('DB.xlsx')
        print "Register Successful!"
        time.sleep(1)
        os.system("clear")
        print "Scan your ID!"
        return False 
  


# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()



#Header of DB.xlsx
database = xlrd.open_workbook('DB.xlsx')
file = copy(database)
sheet = file.get_sheet(0)
sheet.write(0,0,'#',label)
sheet.write(0,1,'UID',label)
sheet.write(0,2,'Name',label)
sheet.write(0,3,'ID Number',label)

col_2 = sheet.col(1)
col_2.width = 256*30

col_3 = sheet.col(2)
col_3.width = 256*30

col_4 = sheet.col(3)
col_4.width = 256*30
file.save('DB.xlsx')

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

        check_List(uid)
        time.sleep(2)
        