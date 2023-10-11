n = int(input("enter a non-zero positive number : "))
if n <= 0:
    print("please enter a non-zero positive number.")
else:
    f = 1
    for i in range(1, n + 1):
        f *= i
    print("the factorielle of" , n ,"is", f)