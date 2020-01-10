from django.db import models
import pytz

# Create your models here.
class Member(models.Model):
    uid = models.CharField(max_length=9, primary_key=True)
    nickname = models.CharField(max_length=21)
    firstname = models.CharField(max_length=21)
    lastname = models.CharField(max_length=21)
    idnum = models.IntegerField(default=0)

class Log(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()

    # def checkDate(self, currentDate):
    #     utc = pytz.UTC
    #     print(self.date)
    #     currentDate = currentDate.replace(tzinfo=utc) 
    #     entryDate = self.date.replace(tzinfo=utc) 
    #     return entryDate.year == currentDate.year and entryDate.month == currentDate.month and entryDate.day == currentDate.day 
