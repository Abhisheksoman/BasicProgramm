a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
print("Select an option")
print("1.Addition 2.Subtraction 3.Multiplication 4.Division")
c=int(input())
def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
def div():
    print(a/b)
if c==1:
    add()
elif c==2:
    sub()
elif c==3:
    mul()
elif c==4:
    div()
else:
    print("Invalid choice")



