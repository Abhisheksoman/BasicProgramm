a=int(input("Enter the measurement of first side -"))
b=int(input("Enter the measurement of second side -"))
c=int(input("Enter the measurement of third side -"))
if a==b==c:
    print("the triangle is equilateral")
elif a!=b and b!=c and a!=c:
    print("the triangle is scalene")
else:
    print("the triangle is isoceles")

