n=str(input("Enter your name "))
g=str(input("Enter your email id "))
mo=str(input("Enter your mobile number"))
f=open(n,"w")
z=n+"\n"+g+"\n"+mo
f.write(z)
f.close()
f=open(n,"r")
print("select an option")
c=int(input("1.Read\n2.Write\n"))
if c==1:
    print(f.read())
elif c==2:
    f.write("")
