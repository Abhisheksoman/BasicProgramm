a=int(input("Enter a number"))
if a>1:
    for i in range(2,int(a/2)+1):
        if a%i==0:
            print("not prime")
            break
        else:
            print(" prime")
            break

else: 
    print("The number is not a prime")