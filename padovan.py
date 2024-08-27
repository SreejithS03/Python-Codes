def pad(n):
    if n<0:
        return 0
    elif n>=0 and n<3:
        return 1
    else: 
        return pad(n-2)+pad(n-3)
num=int(input("Enter a number"))
for i in range(num):
    print(pad(i))