# This file is part of myjoy_example

# Print all states of the joystick 'j'.
def all(j,axes,balls,buttons,hats):
	print ''
	# Print axes information.
	if axes > 1:
		for i in range(axes):
			print 'Axis %d: %f' % (i,j.get_axis(i))
	elif axes == 1:
		print 'Axis: %f' % j.get_axis(0)
	# Print balls information.
	if balls > 1:
		for i in range(balls):
			print 'Ball %d: <%d , %d>' % (i,j.get_ball(i))
	elif balls == 1:
		print 'Ball: <%d , %d>' % j.get_ball(0)
    	# Print buttons information.
	if buttons > 1:
		for i in range(buttons):
			print 'Button %d: %d' % (i,j.get_button(i))
	elif buttons == 1:
		print 'Button: %d' % j.get_button(0)
	# Print hats information.
	if hats > 1:
		for i in range(hats):
			print 'Hat %d: <%d , %d>' % (i,j.get_hat(i))
	elif hats == 1:
		print 'Hat: <%d , %d>' % j.get_hat(0)
