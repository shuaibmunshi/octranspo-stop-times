# octranspo-stop-times
Flask app to show local OCtranspo Bus Times

Fetches Octranspo stop data for a given stop using OCtranspo's appID.
Displays the next two stops for the given bus stop as well as uses the GPS data to predict when the bus will actually arrive at the bus stop.

Note:
1) Requires an OCtransp API key from: http://www.octranspo.com/developers
The API key and your APPID go in a file called settings.py in the app directory.
2) This code is written specifically for the two stops that the people in my house use, it does not support other stops without changing stop numbers everywhere in the code.

![alt text][1]

  [1]: https://i.imgur.com/fBWpnUL.png
