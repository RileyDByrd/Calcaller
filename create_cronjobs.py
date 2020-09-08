#!/usr/bin/env python3

import subprocess, datetime, ast;

cal_events = subprocess.check_output(['python3', 'quickstart.py']).decode('ascii').splitlines()

for i in range(0, len(cal_events)):
	cal_events[i] = ast.literal_eval(cal_events[i])

for c in cal_events:
	if c[0][-3:-2] == ":":
		c[0] = c[0][:-3] + c[0][-2:];
print(cal_events);

currentt = datetime.datetime.astimezone(datetime.datetime.now(datetime.timezone.utc)).isoformat()
currentt = currentt[:-3] + currentt[-2:]

for e in cal_events:
	try:
		en = '\ '.join(e[1].split())
		et = datetime.datetime.strptime(e[0], "%Y-%m-%dT%H:%M:%S%z")
		notifyt = et - datetime.timedelta(minutes=5)
		cmd = ['crontab -l | { cat; echo \'' + datetime.datetime.strftime(notifyt, '%M %H %d %m *') + ' sh launch.sh ' + en + datetime.datetime.strftime(et, ' at\ %I\:%M\ %p\'; } ') + "| crontab -"]
		print(cmd)
		subprocess.check_output(cmd, shell=True)
	except:
		en = '\ '.join(e[1].split())
		et = datetime.datetime.strptime(e[0], "%Y-%m-%d")
		notifyt = et - datetime.timedelta(hours=11)
		cmd = ['crontab -l | { cat; echo \'' + datetime.datetime.strftime(notifyt, '%M %H %d %m *') + ' sh launch.sh ' + en + datetime.datetime.strftime(et, ' on\ %m\,\ %d\'; } ') + "| crontab -"]
		print(cmd)
		subprocess.check_output(cmd, shell=True)
