#!/usr/bin/python3

import os
import time
import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib

def message_callback(bus, message):
    if message.get_interface() == "org.mate.ScreenSaver":
        if message.get_member() == "ActiveChanged":
            screensaver_enabled = bool(message.get_args_list()[0])
            print('screensaver = ', screensaver_enabled)
            if screensaver_enabled:
                os.system('xset +dpms dpms 1 1 1')
            else:
                os.system('xset dpms dpms 0 0 0')

dbus_loop = DBusGMainLoop(set_as_default=True)
session = dbus.SessionBus(mainloop=dbus_loop)
session.add_match_string_non_blocking("interface='org.mate.ScreenSaver'")
session.add_message_filter(message_callback)
loop = GLib.MainLoop()
loop.run()
