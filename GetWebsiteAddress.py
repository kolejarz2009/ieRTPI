from ieCurrentDate import Date
Headcode=input("Headcode: ")
Website="http://api.irishrail.ie/realtime/realtime.asmx/getTrainMovementsXML?TrainId=" + Headcode + "&TrainDate=" + Date
print(Website)
