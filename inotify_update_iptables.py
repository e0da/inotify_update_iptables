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
        try:
            print 'Exempting {0}'.format(event.name)
            subprocess.call([
                'iptables',
                '-I INPUT 10',
                '-s {0}',
                '-j ACCEPT'.format(event.name),
                ])
        except Exception as e:
            print e

if __name__ == '__main__':
    wm = pyinotify.WatchManager()
    notifier = pyinotify.Notifier(wm, default_proc_fun=OnCreateHandler())
    wm.add_watch('inotify_update_iptables', pyinotify.ALL_EVENTS)
    notifier.loop()
