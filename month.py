month = input("enter a month : ")
if month==("january","march","may","july","august","october","december"):
     print("31")
elif month==("april","june","september","november"):
    print("30")
elif month=="february":    
    print("29")
else:
    print("invalid month")