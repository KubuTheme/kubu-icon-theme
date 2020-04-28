#!/bin/python3

import os

icons = dict()
icons = {
    "system-reboot.svg":[
        "system-restart.svg"
    ],
    "system-switch-user.svg":[
        "xfsm-switch.svg",
        "org.kde.plasma.userswitch.svg",
        "org.kde.plasma.userswitcher.svg",
        "org.kde.plasma.uswitcher.svg"
    ]
}

for key in icons:
    for link in icons[key]:
        cmd = 'ln -s ./../scalable/'+key+' ./links/'+link
        os.system(cmd)

print('done ...')
