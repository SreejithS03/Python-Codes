n = int(input("Enter the number"))
arr = []
for i in range(2,n):
    flag = 0
    if i==2:
        flag = 0
    elif i%2==0:
        flag = 1
    else:
        for j in range(3,int(pow(i,0.5))+1,2):
            if i%j==0:
                flag = 1
    if flag == 0:
        arr.append(i)
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==n:
            print(f"{arr[i]}, {arr[j]}")

