num1 = int(input("Enter first number"))
num2 =  int(input("Enter second number"))
for i in range(num1,num2+1):
    l=len(str(i))
    temp = i
    ang = 0
    while i>0:
        rem = i%10
        ang=ang+rem**l
        i = i//10
    if ang == temp:
        print(temp)
