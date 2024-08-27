a = int(input("Enter the first limit"))
b= int(input("Enter the second limit"))
sum = 0
for i in range(a,b+1):
    sum+=i
print(sum)

def twolimits(s,n1,n2):
    if n1>n2:
        return s
    return n1+twolimits(s,n1+1,n2)
num1=2;num2=8
sum =0
sum = twolimits(sum,num1,num2)
print(sum)