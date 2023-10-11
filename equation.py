import math 
a = float(input("enter the first number : "))
b = float(input("enter the second number : "))
c = float(input("enter the third number : "))
delta = pow( b , 2 ) - 4 * a * c
if delta < 0 :
    print ("The equation has no roots")
elif delta == 0 :
    print("The equation has one root : " , -b / ( 2 * a ))
elif delta > 0 :
    x1=(-b + math.sqrt(delta))/(2*a)
    x2=(-b - math.sqrt(delta))/(2*a)
    print("The first root : " , x1 , "The second root : " , x2)