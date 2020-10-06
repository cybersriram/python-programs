import math
def catAndMouse(x,y,z):
    a =(int) (math.fabs(z-x))
    b =(int) (math.fabs(z-y))
    if(a == b):
        return ("Mouse C")
    elif(a>b):
        return("Cat B")
    else:
        return("Cat A")

x,y,z = map(int,input().split())
RES = catAndMouse(x,y,z)
print(RES)