import requests
import json
import os
import settings

def getstoptimes():
    data = [
      ('appID', settings.OCTRASPOAPPID),
      ('apiKey', settings.OCTRANSPOAPIKEY),
      ('routeNo', '86'),
      ('stopNo', '6032'),
      ('format', 'json'),
      ]
    #r = requests.get('https://api.octranspo1.com/v1.2/GetNextTripsForStop', data=data)
    requeststop = requests.post('https://api.octranspo1.com/v1.2/GetNextTripsForStop', data=data)

    #requeststop = requests.post('https://api.octranspo1.com/v1.2/GetNextTripsForStopAllRoutes', data=data)

    #print(requeststop.text) #this is for debugging, it prints the json as a string into the shell

    parsed_json = json.loads(requeststop.text) #loads is load string r.text is the text format

    #print(parsed_json['GetNextTripsForStopResult']['StopLabel'])
    #print(parsed_json['GetRouteSummaryForStopResult']['StopDescription'])
    #description = (parsed_json['GetNextTripsForStopResult']['StopDescription'])
    trip_start_time_0 = print(parsed_json['GetNextTripsForStopResult']['Route']['RouteDirection']['Trips']['Trip'][0]['TripStartTime'])
    return trip_start_time_0
    #print(parsed_json['StopLabel'])


#    data = [('appID', '6679054e'),('apiKey', '298d65c70e16cdbd892cab3aec6849a5'),('stopNo', '6032'),('format', 'json')]
