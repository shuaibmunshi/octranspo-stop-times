from datetime import datetime, timedelta
#example_time='15:10'
#example_adjustment_time='6'

def getgpstime(stop_time,adjustment_time):
    string_hour,string_minutes=stop_time.split(":") #Splits the time stamp into two variables

    int_hour=int(string_hour)
    int_minutes=int(string_minutes)
    int_adjustment_time=int(adjustment_time)
    #print("schedule hours:", int_hour)
    #print("schedule minutes:", int_minutes)
    #print("adjustment age:", example_adjustment_time)

    timeobject = datetime.strptime(stop_time, "%H:%M") #Makes object using stop time with the format Hours:Minutes
    calculated_time = timeobject + timedelta(minutes = int_adjustment_time) #Adds the timedelta (adjustment time)
    twelve_hour = calculated_time.strftime("%I:%M %p") #Converts to 12hour time
    #print(timeobject)
    #print(calculated_time)
    #print(twelve_hour)
    return twelve_hour
