import datetime
now=datetime.datetime.now()

CurrentYear=print(now.year)
CurrentMonth=print(now.month)
CurrentDay=print(now.day)
CurrentHour=print(now.hour)
CurrentMinute=print(now.minute)

if True==True:
#def GetCurrentDate("Yes")
    Year=CurrentYear
    if CurrentMonth=="12":
        Month="dec"
    if CurrentMonth=="11":
        Month="nov"
    if CurrentMonth=="10":
	Month="oct"
    if CurrentMonth=="9":
	Month="sep"
    if CurrentMonth=="8":
	Month="aug"
    if CurrentMonth=="7":
	Month="jul"
    if CurrentMonth=="6":
	Month="jun"
    if CurrentMonth=="5":
	Month="may"
    if CurrentMonth=="4":
	Month="apr"
    if CurrentMonth=="3":
	Month="mar"
    if CurrentMonth=="2":
	Month="feb"
    if CurrentMonth=="1":
	Month="jan"
    else:
	print("Error in retriving current date!")
    Day=CurrentDay

IEDateFormat=Day+"%20 "+Month+"%20 "+Year
print(IEDateFormat)

#http://api.irishrail.ie/realtime/realtime.asmx/getTrainMovementsXML?TrainId=e109&TrainDate=21%20dec%202011

