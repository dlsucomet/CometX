#!/usr/bin/env python
# -*- coding: utf8 -*-
import os
import xlwt, xlrd
import time, calendar
from datetime import datetime
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
	pass
	

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
	pass

def get_Id(uid): #Gets the ID number of the comet member
################################################################
#Get the id of the member in DB.xlsx
################################################################
	database = xlrd.open_workbook('DB.xlsx')
	data_sheet = database.sheet_by_name('Master List')

	uid_column = data_sheet.col_values(colx=1, start_rowx=1)
	id_column = data_sheet.col_values(colx=3, start_rowx=1)

	if (str(uid)[1:-1]) in list(uid_column):
		uid_temp = list(uid_column).index(str(uid)[1:-1])
		return int(list(id_column)[uid_temp])
	else:
		return False

def get_row(uid):
################################################################
#Returns the row to be updated by the user_log() function
#This will tell the program which cell should it write on
################################################################
	database = xlrd.open_workbook('DB.xlsx')
	data_sheet = database.sheet_by_name('Master List')

	uid_column = data_sheet.col_values(colx=1, start_rowx=1)
	id_column = data_sheet.col_values(colx=3, start_rowx=1)

	if (str(uid)[1:-1]) in list(uid_column):
		uid_temp = list(uid_column).index(str(uid)[1:-1])
		return int(uid_temp)
	else:
		return False

		
def user_log(uid):  	
################################################################
#Writes the time in and time out of the uid
#Taps are considered as in or out
#If tap in is greater then tap out, then the type of tap is out.
#If tap out is greater than than tap in, then the type of tap is in.
#Total is tap out - tap in, only in tapo outs
#Use military time to compare tap ins and tap outs
################################################################
	pass

	
#########################################################################################
# This loop keeps checking for chips. If one is near it will get the UID and authenticate

def main():
	
if __name__ == "__main__":
	main()
	
