from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from .models import Member
from .models import Log 
from .models import ResidencyLog 

from datetime import datetime
from datetime import timedelta 
from pytz import timezone
from playsound import playsound


import django
import _thread
import serial
import os

status = {}
timestamp = {}
phil_tz = timezone('Asia/Manila')

def playbeep():
    playsound('beep.mp3')

# Function that handles RFID scanner
def scanner_thread():
    ser = serial.Serial('/dev/ttyACM0', 9600)
    print(ser.name)

    # try:
    #     f = open('contacts.csv')
    # except FileNotFoundError:
    #     with open('contacts.csv', 'w') as f:
    #         writer = csv.writer(f)
    #         writer.writerow(['UID', 'Name', 'ID Number'])
    # finally:
    #     f.close()

    # try:
    #     f = open('log.csv')
    # except FileNotFoundError:
    #     with open('log.csv', 'w') as f:
    #         writer = csv.writer(f)
    #         writer.writerow(['UID', 'Time'])
    # finally:
        # f.close()

    while(True):
        uid = ser.readline().decode('utf-8').strip().replace(' ','')
        # print("UID:", uid)
        curTime = datetime.now(phil_tz)
        stringHour = str(curTime.hour)
        if(curTime.hour < 10):
            stringHour = '0' + stringHour
        stringMinute = str(curTime.minute)
        if(curTime.minute < 10):
            stringMinute = '0' + stringMinute
        readableTime = stringHour + ":" + stringMinute
        mem = Member.objects.filter(uid=uid)
        if(not mem.exists()):
            print("Member does not exist. Create one.")
            firstname = input("Input firstname: ")
            lastname = input("Input lastname: ")
            nickname = input("Input nickname: ")
            idnum = input("Input idnum: ")
            mem = Member(
                uid=uid,
                nickname=nickname,
                firstname=firstname,
                lastname=lastname,
                idnum=idnum
            )
            mem.save()

        mem = Member.objects.get(uid=uid)
        
        log = Log(
            member=mem,
            timestamp=curTime
        )
        log.save()

        if(uid in status):
            if(status[uid]):
                status[uid] = False
                seconds = (curTime - timestamp[uid]).total_seconds()
                print("###")
                print("See you later",mem.firstname,mem.lastname+"!")
                print("Time:",readableTime)
                print("Minutes stayed:",format(seconds / 60, '.2f'))
                playbeep()
                residencyLog = ResidencyLog(
                    member=mem,
                    seconds=seconds,
                    timestamp=curTime
                )
                residencyLog.save()
            else:
                print("###")
                print("Welcome",mem.firstname,mem.lastname+"!")
                print("Time:",readableTime)
                timestamp[uid] = curTime
                status[uid] = True
                playbeep()
        else:
            print("###")
            print("Welcome",mem.firstname,mem.lastname+"!")
            print("Time:",readableTime)
            timestamp[uid] = curTime
            status[uid] = True
            playbeep()
        # with open('log.csv', 'a') as f:
        #     writer = csv.writer(f)
        #     timeVal = time.time()
            # writer.writerow([uid,timeVal])

# Create two threads as follows
try:
   _thread.start_new_thread(scanner_thread, ())
except Exception as e:
    print(e)

# Create your views here.
def index(request):
    return redirect("/logs")

def viewMembers(request):
    memberList = Member.objects.all()
    data = {}
    data['memberList'] = [i for i in memberList.iterator()]
    
    return render(request, "viewMembers.html", data)

def viewLogs(request):
    logList = Log.objects.all()
    data = {}
    rawLogList = [i for i in logList.iterator()]
    finalLogList = []

    for i in rawLogList:
        log = {}
        log['uid'] = i.member.uid
        log['nickname'] = i.member.nickname
        log['idnum'] = i.member.idnum
        i.timestamp = i.timestamp.astimezone(phil_tz)
        log['timestamp'] = i.timestamp
        finalLogList.append(log)

    data['logList'] = finalLogList
    
    return render(request, "viewLogs.html", data)

def viewResidencyLogs(request):
    logList = ResidencyLog.objects.all()
    data = {}
    rawLogList = [i for i in logList.iterator()]
    finalLogList = []

    for i in rawLogList:
        log = {}
        log['uid'] = i.member.uid
        log['nickname'] = i.member.nickname
        log['idnum'] = i.member.idnum
        log['minutes'] = format(i.seconds / 60, '.2f')
        i.timestamp = i.timestamp.astimezone(phil_tz)
        log['timestamp'] = i.timestamp
        finalLogList.append(log)

    data['logList'] = finalLogList
    
    return render(request, "viewResidencyLogs.html", data)
# @csrf_exempt
# def addMember(uid, nickname, firstname, lastname, idnum):
#     mem = Member(
#         uid=uid,
#         nickname=nickname,
#         firstname=firstname,
#         lastname=lastname,
#         idnum=idnum
#     )
#     mem.save()
#     print(mem)