#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
eventn="$1"
eventt="$2"

nohup python3 build_voice_script.py "$eventn" "$even
tt" runserver &
killer_python=$!
python3 ngrok_n_call.py ;
kill $killer_python

exit