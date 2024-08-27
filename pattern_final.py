n=4
for i in range(n):
    print(" "*(n-i-1) +"*"*n)

for i in range(n):
    print(" "*i + "*"*n)
    
n=5
for i in range(n):
    print(" "*(n-i) + "*"*(2*i+1))
n=5
for i in range(1,n):
    print(" "*(i+1) + "*"*((n-i)*2-1))

n=5
for i in range(n):
    print("*"*(i+1))
for i in range(n):
    print("*"*(n-i-1))