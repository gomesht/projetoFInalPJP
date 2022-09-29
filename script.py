import datetime, time

aniversárioDateTime = datetime.date(2006,1,7)
aniversárioTuple = datetime.date.timetuple(aniversárioDateTime)
aniversárioSTR = time.strftime("%Y %m %d",aniversárioTuple)

print(aniversárioDateTime,aniversárioTuple,aniversárioSTR)

print(datetime.date(time.strptime(aniversárioSTR, "%Y %m %d")[0],time.strptime(aniversárioSTR, "%Y %m %d")[1],time.strptime(aniversárioSTR, "%Y %m %d")[2]))