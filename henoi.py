def TowerofHanoi(n,source,destination,intermediate):
    if n==1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    TowerofHanoi(n-1,source,intermediate,destination)
    print(f"Move disk {n} from {source} to {destination}")
    TowerofHanoi(n-1,intermediate,destination,source)

num=int(input("Enter a number"))
TowerofHanoi(num,'A','B','C')