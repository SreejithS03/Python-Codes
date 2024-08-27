def count_num(li):
    count_of_even=0
    count_of_odd=0
    for num in li:
        if num!=0:
            if num%2==0:
                count_of_even+=1
            else:
                count_of_odd+=1
    return count_of_odd,count_of_even
list = [1,2,3,4,5,6,7,8,9,0]
a,b=count_num(list)
print(f"No of odd numbers {a}")
print(f"No of even numbers {b}")