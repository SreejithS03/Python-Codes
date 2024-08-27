n = int(input("Enter the value of n"))
prime = 0
if n<2:
    prime=1
elif n==2:
    prime = 0
elif n%2==0:
    prime = 1
else:
    for i in range(3,int(pow(n,0.5)+1),2):
        if n%i==0:
            prime = 1
            break
if prime==0:
    print("The given number is prime")
else:
    print("The given number is not prime")