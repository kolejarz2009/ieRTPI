#!/usr/bin/python3
'''
To run:
$python3 -c 'import ieRTPI; ieRTPI.LocateTrainByHeadCode("a310")'

AIMS:
-To retrive a train by headcode
-To show trains arriving at specified location
-
'''
#Imports
from datetime import datetime

###FUNCTIONS!!! YAY!!!!!!
def TodaysDate_func(): #<- Don't touch!!! Works!
#TodaysDate=datetime.today().strftime("%d %m %Y")
    Today_Day=datetime.today().strftime("%d")
    Today_Month_Numerical=datetime.today().strftime("%m")
    if Today_Month_Numerical == "01":
        Today_Month="jan"
    elif Today_Month_Numerical == "02":
        Today_Month="feb"
    elif Today_Month_Numerical == "03":
        Today_Month="mar"
    elif Today_Month_Numerical=='04':
        Today_Month="apr"
    elif Today_Month_Numerical=='05':
        Today_Month="may"
    elif Today_Month_Numerical=='06':
        Today_Month="jun"
    elif Today_Month_Numerical=='07':
        Today_Month="jul"
    elif Today_Month_Numerical=='08':
        Today_Month="aug"
    elif Today_Month_Numerical=='09':
        Today_Month="sep"
    elif Today_Month_Numerical=='10':
        Today_Month="oct"
    elif Today_Month_Numerical=='11':
        Today_Month="nov"
    elif Today_Month_Numerical=='12':
        Today_Month="dec"
    else:
        print("Problem establishing current month - Required to continue")
    Today_Year=datetime.today().strftime("%Y")
    TodaysDate=Today_Day + " " + Today_Month + " " + Today_Year
    #print('Today\'s date is:', TodaysDate)
    return TodaysDate

def LocateTrainByHeadCode(HeadCode, Date=TodaysDate_func()): #<- Don't touch!!! Works!
    WebAdress="http://api.irishrail.ie/realtime/realtime.asmx/getTrainMovementsXML?TrainId=%s&TrainDate=%s" %(HeadCode, Date)
    #print(WebAdress)
    return WebAdress

def LocateTrainByStationCode(StationCode, Minutes="89"):
    WebAdress="http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML_WithNumMins?StationCode=%s&NumMins=%s" % (StationCode, Minutes)
    #print(WebAdress)
    return WebAdress
    
def LocateTrainByStationName(StationName, Minutes="89"):
    WebAdress="http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByNameXML?StationDesc=%s&NumMins=%s" %(StationName, Minutes)
    #print(WebAddress)
    return WebAdress
    

