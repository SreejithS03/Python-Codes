n = int(input("Enter the value of n"))
if n%100==0:
    if n%4==0:
        print(f"The given year {n} is leap year")
    else:
        print(f"The given year {n} is not a leap year")
elif n%4==0:
    print(f"The given year {n} is leap year")
else:
    print(f"The given year {n} is not leap year")
    