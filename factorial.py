f=int(input("Enter a number:"))
def fact(f):
    if f==0:
        return 1
    else:
        return f*fact(f-1)
print("The factorial of the given number is",fact(f))

