import requests
import json
import os
import settings

def getstoptimes():
    api_parameters = [
      ('appID', settings.OCTRASPOAPPID),
      ('apiKey', settings.OCTRANSPOAPIKEY),
      ('routeNo', '86'),
      ('stopNo', '6032'),
      ('format', 'json'),
      ]
    #r = requests.get('https://api.octranspo1.com/v1.2/GetNextTripsForStop', data=data)
    requeststop = requests.post('https://api.octranspo1.com/v1.2/GetNextTripsForStop', data=api_parameters)
    #print(requeststop.text) #this is for debugging, it prints the json as a string into the shell

    #use example json below if you're staying up too late and there are no more trips to fetch from OCtranspo
    example_json = '{"GetNextTripsForStopResult":{"StopNo":"6032","StopLabel":"FISHER DYNES","Error":"","Route":{"RouteDirection":{"RouteNo":86,"RouteLabel":"Elmvale","Direction":"Eastbound","Error":"","RequestProcessingTime":"20171208115954","Trips":{"Trip":[{"TripDestination":"Hurdman","TripStartTime":"11:50","AdjustedScheduleTime":"9","AdjustmentAge":"0.85","LastTripOfSchedule":false,"BusType":"4E DEH","Latitude":"45.342767","Longitude":"-75.728672","GPSSpeed":"0.5"},{"TripDestination":"Elmvale","TripStartTime":"12:02","AdjustedScheduleTime":"19","AdjustmentAge":"0.72","LastTripOfSchedule":false,"BusType":"4LA - DEH","Latitude":"45.348399","Longitude":"-75.762452","GPSSpeed":"0.5"},{"TripDestination":"Hurdman","TripStartTime":"12:18","AdjustedScheduleTime":"34","AdjustmentAge":"-1","LastTripOfSchedule":false,"BusType":"4E - DEH","Latitude":"","Longitude":"","GPSSpeed":""}]}}}}}'

    #parsed_json = json.loads(requeststop.text) #loads is load string r.text is the text format
    parsed_json = json.loads(example_json) #Uses the example json object

    #print(parsed_json['GetNextTripsForStopResult']['StopLabel'])
    #print(parsed_json['GetRouteSummaryForStopResult']['StopDescription'])
    #description = (parsed_json['GetNextTripsForStopResult']['StopDescription'])
    trip_start_time_0 = parsed_json['GetNextTripsForStopResult']['Route']['RouteDirection']['Trips']['Trip'][0]['TripStartTime']
    return trip_start_time_0
    #print(parsed_json['StopLabel'])


#    data = [('appID', '6679054e'),('apiKey', '298d65c70e16cdbd892cab3aec6849a5'),('stopNo', '6032'),('format', 'json')]
