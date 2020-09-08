#!/usr/bin/env python3

from flask import Flask, request;
from twilio.twiml.voice_response import VoiceResponse;
import sys;

app = Flask(__name__)
@app.route("/", methods = ['GET', 'POST'])
def voice(event_name = sys.argv[1], event_time = sys.argv[2]):
        # Start TwiML response.
        resp = VoiceResponse()
        # Read message.
        resp.say("Sir, your scheduled event, {}, is {}. With that, I bid you adieu.".format(str(event_name), str(event_time)), voice='man');

        return str(resp);

print(sys.argv[1], sys.argv[2])
if __name__ == "__main__":
    app.run(debug=True)