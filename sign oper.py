x = float(input("enter the first number : "))
y = float(input("enter a second number : "))
if ( x >= 0 and y >= 0 ) or ( x <= 0 and y <= 0) :
    z = x
    x = y
    y = z
    print("the first number is : " , x)
    print("the second number is : " , y)
else :
    print ("the sum is : " , x + y,"and the multiplication is : ", x * y)