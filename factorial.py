def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter the number"))
Ans = fact(n)
print(f"The factorial of {n} is {Ans}")