#!/usr/bin/env python

import sys
import requests
import json
import re

args = sys.argv
if len(args) != 4:
    print
    'Not enough command line arguments!'
    sys.exit(1)
else:
    msg_receiver = args[1]
    msg_subject = args[2]
    msg_body = args[3]
    msg = msg_body.split("||")
    msg_content = msg[1].split(":")
    if msg[0].find("OK") == -1:
        msg_color = '#FF0000'
        msg_content[0] = 'NOT AVAILABLE'
    else:
        msg_color = '#00FF00'
        msg_content[0] = 'AVAILABLE'

    msg_text = msg_content[0] + msg_content[1]
    msg_attach = "[" + '{ ' + 'text: ' + msg_text + ', ' + 'color: ' + msg_color + ' } ' + "]"
    msg_value = re.escape(msg_attach)
    print(msg_attach)
    print(msg_value)

    token = 'xxxxxxx'
    channel = '#' + msg_receiver

    send_url = 'https://slack.com/hooks/'
    payload = json.dumps({
                          'channel': channel,
                          'attachments': [{
                              'text': msg_text,
                              'color': msg_color
                          }
                          ],
                          })

    r = requests.post(send_url + token, data=payload)
    if r.status_code == 200:
        sys.exit(0)
    else:
        print
        'The message has not been sent!'
        print
        r.status_code
        sys.exit(1)
