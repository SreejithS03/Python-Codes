n = input("Enter a number")
l = len(n)
num = int(n)
temp = num
ang = 0
rev = 0
sum = 0
while num>0:
    rem = num%10
    ang=ang+rem**l
    sum+=rem
    rev = rev*10+rem
    num = num//10
print(f"Sum: {sum}")
if rev == temp:
    print("The given number is a palindrome")
else:
    print(f"The given number is not a palindrome and the reverse is {rev}")
if ang == temp:
    print("The given number is angstrom")
else:
    print(f"The given number is not angstrom")

