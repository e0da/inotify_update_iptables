inotify_update_tables
=====================

Watch a directory for newly created files. If a file is created, use its name as
an IP address and insert a -j ACCEPT for that IP into the firewall at position
10.

This is obviously a very useful program for one very specific purpose. :)
