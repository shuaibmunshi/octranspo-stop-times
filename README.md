# octranspo-stop-times
Flask app to show local OCtranspo Bus Times

Fetches Octranspo stop data for a given stop using OCtranspo's appID.
Displays the next two stops for the given bus stop as well as uses the GPS data to display more accurate next bus time.

Note that you need an OCtransp API key from: http://www.octranspo.com/developers
The API key and your APPID go in a file called settings.py in the app directory.
