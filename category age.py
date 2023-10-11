n = int(input("Write your age : "))
while n <= 0 :
    n = int(input("Write corectly your age : "))
if n == 6 or n == 7 :
    print("Chick")
elif n == 8 or n == 9 :
    print("Pupil")
elif n == 10 or n == 11 :
    print("small")
elif n > 12 :
    print("Youngest")