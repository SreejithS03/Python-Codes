n=4
for i in range(0,n):
    for j in range(0,n-i):
        print(" ",end='')
    for j in range(0,n):
        print("*", end='')
    print("")

n=4
for i in range(0,n):
    for j in range(0,n):
        print("*", end='')
    print()
    for j in range(0,i+1):
        print(" ",end='')

