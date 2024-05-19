x=100
print(x)
d=int(input("enter the divisor"))
try:
    a=x/d
    print(a)
except ZeroDivisionError:
    print("Division by 0 is not possible")
finally:
    print("Task completed")
 