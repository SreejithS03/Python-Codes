n = int(input("Enter the no of elements in the array"))
arr = []
arr = list(map(int,input("Enter the elements").split()))[:n]
large = arr[0]
for i in range(1,n):
    if arr[i]>large:
        large = arr[i]
print(large)
