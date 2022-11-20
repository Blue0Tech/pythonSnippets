from factorial import fact
PI = 3.1415926535
def sec(x,accuracy,deg):
    if(deg):
        x*=(PI/180)
    result = 0
    for i in range(0,accuracy):
        iterations = i*2
        numerator = x**iterations
        denominator = fact(iterations)
        if(i%2==0):
            result+=(numerator/denominator)
        else:
            result-=(numerator/denominator)
    result = 1/result
    return result
# x is the angle in degrees or radians
# accuracy is how many times to continue the sequence of (x^n)/n!
# if deg is true then it is converted into radians for the formula to work
