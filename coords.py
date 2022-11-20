from sin import sin
from cos import cos
import math
pi = 3.14159265
r = 6371000
def coords(x1,y1,x2,y2):
		x1r = x1 * pi/180
		x2r = x2 * pi/180
		dx = (x2-x1) * pi/180
		dy = (y2-y1) * pi/180
		a = sin(dx/2,5,False)**2 + cos(x1r,5,False) * cos(x2r,5,False) * (sin(dy/2,5,False)**2)
		c = 2 * math.atan2((a)**0.5,(1-a)**0.5)
		d = r * c
		return d