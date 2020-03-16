# -*- coding: utf-8 -*-
#!/usr/bin/python

##
#  CoffeeTime
#  Copyright (C) 2016, Augusto Damasceno
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import myserial
import time
import datetime
import serialPython

ports = serialPython.serialDiscover()
port = ports[int(input("Choose the port (number, the first is 0): "))]

hour = input('Hour to alarm: ');
minute = input('Minute to alarm: ')

alarmWait = True
while alarmWait:
    d = datetime.datetime.now()
    if(d.hour == hour):
        if(d.minute == minute):
            serialPython.serialSend(port,9600,'O',1,serial.PARITY_NONE,serial.EIGHTBITS,serial.STOPBITS_ONE)
            alarmWait = False
    time.sleep(3)

# Wait 10 minutes and turn off
time.sleep(600)
serialPython.serialSend(port,9600,'F',1,serial.PARITY_NONE,serial.EIGHTBITS,serial.STOPBITS_ONE)

