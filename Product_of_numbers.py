def prod(list):
    result = 1
    for num in list:
        result*=num
    return result
l=[1,2,3,4,5,6,7,8,9]
Ans = prod(l)
print(f"The result is {Ans}")