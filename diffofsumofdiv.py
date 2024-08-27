n = int(input())
m = int(input())
sumdiv = 0
sumnotdiv = 0
for i in range(1,m+1):
    if i%n==0:
        sumdiv +=i
    else:
        sumnotdiv+=i
print(sumnotdiv-sumdiv)