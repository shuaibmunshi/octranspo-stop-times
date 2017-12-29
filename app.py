from flask import Flask
from flask import render_template
import json
import settings
from apicall import getstoptimes
from gpstime import getgpstime
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def main():
    current_time = datetime.now().strftime('%H:%M:%S')
    stoptimes6032 = getstoptimes(stop_number=6032) #Parameter is the stop number
    stoptimes6031 = getstoptimes(stop_number=6031) #Parameter is the stop number
    #Fetches the GPS time using the scheduled time and the time delta from the GPS position of the bus
    real_gps_time_6032_0 = getgpstime(stop_time=stoptimes6032['scheduled_stop_time_0'],adjustment_time=stoptimes6032['schedule_adjustment_time_0'])
    real_gps_time_6032_1 = getgpstime(stop_time=stoptimes6032['scheduled_stop_time_1'],adjustment_time=stoptimes6032['schedule_adjustment_time_1'])
    #render_template is a Flask function that returns renders what is in app/templates

    real_gps_time_6031_0 = getgpstime(stop_time=stoptimes6031['scheduled_stop_time_0'],adjustment_time=stoptimes6032['schedule_adjustment_time_0'])
    real_gps_time_6031_1 = getgpstime(stop_time=stoptimes6031['scheduled_stop_time_1'],adjustment_time=stoptimes6032['schedule_adjustment_time_1'])

    return render_template(
    'index.html',
    stop_label_6032=stoptimes6032['stop_label'],
    route_number=stoptimes6032['route_number'],
    trip_destination_6032_0=stoptimes6032['trip_destination_0'],
    scheduled_stop_time_6032_0=stoptimes6032['scheduled_stop_time_0'],
    schedule_adjustment_time_6032_0=stoptimes6032['schedule_adjustment_time_0'],
    real_gps_time_6032_0=real_gps_time_6032_0,
    trip_destination_6032_1=stoptimes6032['trip_destination_1'],
    scheduled_stop_time_6032_1=stoptimes6032['scheduled_stop_time_1'],
    schedule_adjustment_time_6032_1=stoptimes6032['schedule_adjustment_time_1'],
    real_gps_time_6032_1=real_gps_time_6032_1,
    current_time=current_time,
    stop_label_6031=stoptimes6031['stop_label'],
    trip_destination_6031_0=stoptimes6031['trip_destination_0'],
    scheduled_stop_time_6031_0=stoptimes6031['scheduled_stop_time_0'],
    schedule_adjustment_time__0=stoptimes6031['schedule_adjustment_time_0'],
    real_gps_time_6031_0=real_gps_time_6031_0,
    trip_destination_6031_1=stoptimes6031['trip_destination_1'],
    scheduled_stop_time_6031_1=stoptimes6031['scheduled_stop_time_1'],
    schedule_adjustment_time_6031_1=stoptimes6031['schedule_adjustment_time_1'],
    real_gps_time_6031_1=real_gps_time_6031_1
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
