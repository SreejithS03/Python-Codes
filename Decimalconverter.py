n = int(input("Enter the number"))
numsys = int(input("Enter the number system"))
ans = []
while n>0:
    ans.append(n%numsys)
    n=n//numsys
for i in ans:
    print(i,end="")
    