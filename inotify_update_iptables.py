#!/usr/bin/env python
#
# Usage:
#   ./inotify_update_iptables.py
#
# Watches the ./inotify_update_ipables directory for created files, then adds an
# exception to the firewall for the IP address specified by the file name.

import subprocess
import sys
import pyinotify

class OnCreateHandler(pyinotify.ProcessEvent):

    def process_IN_CREATE(self, event):
        ip_address = event.name
        command = 'iptables -I INPUT 10 -s {0} -j ACCEPT'.format(ip_address)
        try:
            print('Exempting {0}'.format(ip_address))
            subprocess.call(command.split())
        except Exception as e:
            print(e)

if __name__ == '__main__':
    wm = pyinotify.WatchManager()
    notifier = pyinotify.Notifier(wm, default_proc_fun=OnCreateHandler())
    wm.add_watch('ips', pyinotify.ALL_EVENTS)
    notifier.loop()
