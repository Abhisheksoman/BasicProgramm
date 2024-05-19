import calculator1 as cl

a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
print("Select an option")
print("1.Addition 2.Subtraction 3.Multiplication 4.Division")
c=int(input())
if c==1:
    cl.add(a,b)
elif c==2:
    cl.sub(a,b)
elif c==3:
    cl.mul(a,b)
elif c==4:
    cl.div(a,b)
else:
    print("Invalid choice")

