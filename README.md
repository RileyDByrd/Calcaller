# Calcaller
## Description
Calcaller is a simple application to remind one by phone of upcoming events. It's intended to be run as a daemon on something like a raspberry pi that you keep running all the time. Before deploying the application, make sure to replace the filler text with your Google Calendar and Twilio A.P.I. keys, to add your own message, and to replace the relative paths that are sent to Cron with absolute paths for your system.

## Dependencies
* Python3
  * Flask, Twilio, oauth2client, httplib2, and apiclient Python packages
* BASH, Ngrok, and Cron
