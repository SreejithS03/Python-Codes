numsys=int(input("Enter the base"))
n = int(input("Enter the number"))
temp = n
dec = 0
base=1
while n>0:
    rem = n%10
    dec = dec+base*rem
    n=n//10
    base*=numsys
print(dec)

