def power_num(b,p):
    if p==0:
        return 1
    else:
        return b*power_num(b,p-1)

base,power = map(int,input("Enter the base and power").split())
print(f"The answer is: {power_num(base,power)}")
