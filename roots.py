a= int(input("Enter the value of a"))
b = int(input("Enter the value of b"))
c = int(input("Enter the value of c"))
d = pow(b,2)-4*a*c
if d==0:
    print("The roots are equal")
    root1 = -b/2*a
    print(root1)
elif d<0:
    print("The roots are imaginary")
    root1 = -b/2*a
    root2 = round(pow(-d,0.5)/(2*a),3)
    print(f"The roots are {root1}+i{root2} and {root1}-i{root2}")
else:
    print("The roots are real")
    root1 = (-b+pow(d,0.5))/(2*a)
    root2 = (-b-pow(d,0.5))/(2*a)
    print(f"The roots are {int(root1)} and {int(root2)}")