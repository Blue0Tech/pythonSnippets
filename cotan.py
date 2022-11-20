from factorial import fact
from sin import sin
from cos import cos
def cotan(x,accuracy,deg):
    sinVal = sin(x,accuracy,deg)
    cosVal = cos(x,accuracy,deg)
    result = cosVal/sinVal
    return result
# x is the angle in degrees or radians
# accuracy is how many times to continue the sequence of (x^n)/n!
# if deg is true then it is converted into radians for the formula to work
