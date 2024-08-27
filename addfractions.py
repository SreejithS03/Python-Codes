def lcm(n1,n2):
    for i in range(max(n1,n2),n1*n2+1,max(n1,n2)):
        if i%min(n1,n2)==0:
            return i
def hcf(n1,n2):
    while n1!=n2:
        if n1>n2:
            n1-=n2
        else:
            n2-=n1
    return n1

n1 = int(input("Enter the numerator"))
d1 = int(input("Enter the denominator"))
n2 = int(input("Enter the numerator"))
d2 = int(input("Enter the denominator"))
ans = lcm(d1,d2)
rem = ans//d1
n1*=rem
d1 = ans
rem = ans//d2
n2*=rem
d2 = ans
ansnum = n1+n2
ansden = d1
h = hcf(ansnum,ansden)
ansnum = int(ansnum/h)
ansden = int(ansden/h)
print(f"The answer is {ansnum}/{ansden}")