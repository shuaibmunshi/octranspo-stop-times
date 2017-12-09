from flask import Flask
import os
import socket
import requests
import json
import settings
from stop_6032 import getstoptimes


app = Flask(__name__)

@app.route("/")
def main():
    #apiparameters = {'appID': settings.OCTRASPOAPPID,'apiKey': settings.OCTRANSPOAPIKEY,'routeNo': '86','stopNo': '6032','format': 'json'}
    #r = requests.post('https://api.octranspo1.com/v1.2/GetNextTripsForStop', data = apiparameters)
    #parsed_json = json.loads(r.text) #loads is load string r.text is the text format
    #jsonstoptime = parsed_json['GetNextTripsForStopResult']['StopNo']
    stoptimes = getstoptimes()
    html = "<h3>Stop 6032, Northbound:</h3>" \
           "<b>Stoptime:</b> {functionstoptime}<br/>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(hostname=socket.gethostname(), functionstoptime=stoptimes)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
