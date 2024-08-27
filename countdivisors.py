n = int(input("Enter a number"))
d = int(input("Enter the count of divisors"))
count = 0
for i in range(1,n+1):
    count_divisor = 0
    for j in range(1,i+1):
        if i%j==0:
            count_divisor+=1
    if count_divisor==d:
        count+=1
print(count)