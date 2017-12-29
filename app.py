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
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    stoptimes = getstoptimes(stop_number=6032) #Parameter is the stop number
    #Fetches the GPS time using the scheduled time and the time delta from the GPS position of the bus
    real_gps_time = getgpstime(stop_time=stoptimes['scheduled_stop_time_0'],
                    adjustment_time=stoptimes['schedule_adjustment_time_0'])
    #render_template is a Flask function that returns renders what is in app/templates
    return render_template('index.html',
                        stop_label=stoptimes['stop_label'],
                        route_number=stoptimes['route_number'],
                        trip_destination_0=stoptimes['trip_destination_0'],
                        scheduled_stop_time_0=stoptimes['scheduled_stop_time_0'],
                        schedule_adjustment_time_0=stoptimes['schedule_adjustment_time_0'],
                        real_gps_time=real_gps_time,
                        current_time=current_time
                        )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
