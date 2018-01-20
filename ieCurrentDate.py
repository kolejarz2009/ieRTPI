# This script establishes the current date, in the format used by Irish Rail, in their public API
import datetime
CurrentMonth=datetime.datetime.now().month

Year=datetime.datetime.now().year
if (CurrentMonth)==12:
        Month="dec"
if CurrentMonth==11:
        Month="nov"
if CurrentMonth==10:
        Month="oct"
if CurrentMonth==9:
        Month="sep"
if CurrentMonth==8:
        Month="aug"
if CurrentMonth==7:
        Month="jul"
if CurrentMonth==6:
        Month="jun"
if CurrentMonth==5:
        Month="may"
if CurrentMonth==4:
        Month="apr"
if CurrentMonth==3:
        Month="mar"
if CurrentMonth==2:
        Month="feb"
if CurrentMonth==1:
        Month="Jan"
Day=datetime.datetime.now().day

IEDateFormat = "%s %s %s" % (Day, Month, Year)
global Date
Date = IEDateFormat


print(Date)
