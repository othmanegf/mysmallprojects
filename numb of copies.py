n = int(input("enter the number of copies : "))
if n <= 10 :
    print ("the price is : " , n * 0.30 , "DH" )
elif n > 10 and n <= 30 :
    print ( "the price is: " , 10 * 0.30 + (n - 10) * 0.25 , "DH" )
else :
    print ("the price is : " , 10 * 0.30 + 20 * 0.25 + (n-30) * 0.20 , "DH")