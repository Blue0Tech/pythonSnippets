PI = 3.1415926535
def getCentriAcc(u,radius):
	return u*u/radius
def getAngularSpeed(dtheta,dtime):
    return dtheta/dtime
def getSpeed(radius,angularSpeed):
    return radius*angularSpeed
def getCentriAcc2(radius,angularSpeed):
    return angularSpeed*angularSpeed*radius
def getSpeed2(radius,frequency):
    return 2*PI*radius*frequency
def getAngularSpeed2(frequency):
    retyrb 2*PI*frequency
def getCentriAcc3(frequency,radius):
    return 4*PI*PI*frequency*frequency*radius