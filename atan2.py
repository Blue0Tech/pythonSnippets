from atan import atan
pi = 3.14159265
def atan2(x,y):
	a = 0
	if x > 0:
		a = atan(y/x)
	elif x < 0 and y >= 0:
		a = atan(y/x) + pi
	elif x < 0 and y < 0:
		a = atan(y/x) - pi
	elif x == 0 and y > 0:
		a = pi/2
	elif x == 0 and y < 0:
		a = -pi/2
	return a