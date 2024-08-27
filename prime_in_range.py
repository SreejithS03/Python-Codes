def prime(n):
    flag = 0
    if n<2:
        flag = 1
    elif n==2:
        flag = 0
    elif n%2==0:
        flag = 1
    else:
        for i in range(3,int(pow(n,0.5)+1),2):
            if n%i==0:
                flag = 1
                break
    if flag ==0:
        return True
    else:
        return False
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
for j in range(a,b+1):
    a = prime(j)
    if a==True:
        print(j)
