#!/usr/bin/env python3

### Check Ngrok. Kill if running. Start new instance.
import socket, subprocess, time, json;
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socktest = sock.connect_ex(('127.0.0.1', 4040))

if socktest == 0:
    subprocess.check_output("killall ngrok".split());
    time.sleep(2);
    subprocess.Popen(["ngrok http 5000 > ngrok.log &"], shell=True);
else:
    subprocess.Popen(["ngrok http 5000 > ngrok.log &"], shell=True);

time.sleep(3);
subprocess.check_output(["curl http://localhost:4040/api/tunnels > tunnels.json"], shell=True);
with open('/home/pi/NC_Pi_Scholarship/tunnels.json') as data_file:
     datajson = json.load(data_file)
for i in datajson['tunnels']:
    ngrokurl = i['public_url']
print(ngrokurl)

### Make call.
from twilio.rest import Client

account_sid = 'your account sid'
auth_token = 'your auth token'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url = ngrokurl + "/",
                        to = '+ your to number',
                        from_ = '+ your from number'
                        )

time.sleep(180);
subprocess.check_output("killall ngrok".split());
exit()