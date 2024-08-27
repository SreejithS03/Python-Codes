def hcf(n1,n2):
    while n1!=n2:
        if n1>n2:
            n1-=n2
        else:
            n2-=n1
    return n1
def lcm(n1,n2):
    for i in range(max(n1,n2),n1*n2+1,max(n1,n2)):
        if i%min(n1,n2)==0:
            return i

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
result1 = hcf(num1,num2)
result2 = lcm(num1,num2)
print(f"HCF : {result1}\nLCM : {result2}")