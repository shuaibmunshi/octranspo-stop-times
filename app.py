from flask import Flask
import os
import socket
import requests
import json
import settings
from apicall import getstoptimes


app = Flask(__name__)

@app.route("/")
def main():
    stoptimes = getstoptimes(stop_number=6032) #Parameter is the stop number
    html = "<h3>Bus Stop 6032: {stop_label}</h3>" \
           "<b>Bus Number:</b> {route_number}</br>" \
           "<b>Trip Destination:</b> {trip_destination_0}</br>" \
           "<b>Scheduled Stop:</b> {scheduled_stop_time_0}<br/>"
    return html.format(stop_label=stoptimes['stop_label'],
                       route_number=stoptimes['route_number'],
                       trip_destination_0=stoptimes['trip_destination_0'],
                       scheduled_stop_time_0=stoptimes['scheduled_stop_time_0']
                       )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
