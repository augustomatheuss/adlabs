# Copyright (c) 2015, Augusto Damasceno.
# All rights reserved.
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#   1. Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
# OF SUCH DAMAGE.

import pygame
import time
import socket

UDP_IP = "192.168.0.64" # Your Ip
UDP_PORT = 1234		# Port

print 'Init joystick module with pygame...\n'
# Initialize the joystick module.
pygame.joystick.init()

# Get the number of joysticks.
num = pygame.joystick.get_count()
if num <> 0:
    c = 1
    if num <> 1:
        print 'There is %d joysticks, choose one.' % num
        c = input(">> ")
        while (c < 1) or (c > num):
            print 'Wrong joystick number, choose again.'
            c = input(">> ")

    print 'Try to initialize joystick %d.' % c
    myJoystick = pygame.joystick.Joystick(0)
    myJoystick.init()
    if myJoystick.get_init():
        # Initialize all imported pygame modules
        pygame.init()
        print 'Joystick %d successful initialized.' % c
        print 'Id: %s' % myJoystick.get_id()
        print 'Name: %s' % myJoystick.get_name()
        axes = myJoystick.get_numaxes()
        print 'Axes: %s' % axes
        balls = myJoystick.get_numballs()
        print 'Balls: %s' % balls
        buttons = myJoystick.get_numbuttons()
        print 'Buttons: %s' % buttons
        hats = myJoystick.get_numhats()
        print 'Hats: %s' % hats
        quit = False
        # Main loop.
        while quit == False:
            # Write here your code using the joystick!!

            # Internally process pygame event handlers.
            pygame.event.pump()

            # Get events from the queue.
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    print 'Axis %d: %f' % (event.axis,event.value)
		    MESSAGE = 'Axis %d: %f' % (event.axis,event.value)
	    	    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	    	    sock.sendto(MESSAGE,(UDP_IP, UDP_PORT))
                if event.type == pygame.JOYBALLMOTION:
                    print 'Ball %d: <%d , %d>' % (event.ball,event.rel)
		    MESSAGE = 'Ball %d: <%d , %d>' % (event.ball,event.rel)
	    	    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	    	    sock.sendto(MESSAGE,(UDP_IP, UDP_PORT))
                if event.type == pygame.JOYBUTTONDOWN:
                    print 'Button %d pressed.' % event.button
		    MESSAGE = 'Button %d pressed.' % event.button
	    	    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	    	    sock.sendto(MESSAGE,(UDP_IP, UDP_PORT))
                if event.type == pygame.JOYBUTTONUP:
                    print 'Button %d released.' % event.button
		    MESSAGE = 'Button %d released.' % event.button
	    	    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	    	    sock.sendto(MESSAGE,(UDP_IP, UDP_PORT))
                if event.type == pygame.JOYHATMOTION:
                    print 'Hat %d: ' % event.hat
                    print event.value
		    MESSAGE = 'Hat %d: <%d , %d>' % (event.hat,event.value[0],event.value[1])
	    	    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	    	    sock.sendto(MESSAGE,(UDP_IP, UDP_PORT))

            # Stopping criterion.
            #if 'remove this comment and write your condition here':
            #    quit = True
    else:
        print 'Joystick %d not initialized, end of program.' % c
else:
    print 'Insert a joystick before run this program.'
# Uninitialize the joystick module.
pygame.joystick.quit()
# Uninitialize all pygame modules.
pygame.quit()
