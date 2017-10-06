#!/usr/bin/env python
# -*- coding: utf8 -*-


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
################################################################
#Get the id of the member in DB.xlsx
################################################################
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
	pass

		
def user_log(uid, row):  	
################################################################
#Writes the time in and time out of the uid
#Taps are considered as in or out
#If tap in is greater then tap out, then the type of tap is out.
#If tap out is greater than than tap in, then the type of tap is in.
#Total is tap out - tap in, only in tapo outs
#Use military time to compare tap ins and tap outs
################################################################
 
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

#########################################################################################
# This loop keeps checking for chips. If one is near it will get the UID and authenticate
if __name__ == "__main__":
	main()
	
def main():
	while continue_reading:
		# Scan for cards    
		(status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
		
		# Get the UID of the card
		(status,uid) = MIFAREReader.MFRC522_Anticoll()
		
		# If we have the UID, do the following functions
		if status == MIFAREReader.MI_OK:
			################################################################
			#insert functions to be used#
			################################################################
			time.sleep(2)
