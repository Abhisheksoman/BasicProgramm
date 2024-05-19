import random
num=random.randint(1,10)
n=int(input("Guess a number"))
print("Number guessed by machine is ",num)
if n>10:
   print("Too high")
elif n<1:
    print("Too low")
elif n==num:
    print("Your guess is right")
else:
    print("wrong guess!")