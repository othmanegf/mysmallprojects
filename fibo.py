n = int(input("Enter a number n greater than 2: "))
U0 = 0
U1 = 1
print(U0)
print(U1)
Un = U0 + U1
while Un <= n:
    print(Un)
    U0 = U1
    U1 = Un
    Un = U0 + U1