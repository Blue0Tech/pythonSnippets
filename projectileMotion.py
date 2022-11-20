from cos import cos
from sin import sin
from tan import tan
G = 9.8107
def getXPos(u,theta,time):
	return u*cos(theta,5,True)*time
def getYPos(u,theta,time):
    part1 =  u*sin(theta,5,True)*time
    part2 = G*time*time/2
    return part1-part2
def getXVel(u,theta):
    return u*cos(theta,5,True)
def getYVel(u,theta,time):
    part1 = u*sin(theta,5,True)
    part2 = G*time
    return part1-part2
def getYPos2(u,theta,x):
    part1 = tan(theta,5,True)*x
    part2 = (G/(2*u*cos(theta,5,True)*u*cos(theta,5,True)))*x*x
    return part1-part2
def timeForMaxHeight(u,theta):
    return u*sin(theta,5,True)/G
def timeInFlight(u,theta):
    return 2*timeForMaxHeight(u,theta)
def getMaxHeight(u,theta):
    return u*sin(theta,5,True)*u*sin(theta,5,True)/(2*G)
def getHorizontalRange(u,theta):
    return u*u*sin(theta*2,5,True)/G
def getMaxRange(u):
    return u*u/G