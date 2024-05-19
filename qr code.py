import pyqrcode
n=str(input("Enter your name "))
g=str(input("Enter your email id "))
mo=str(input("Enter your mobile number"))
z=n+"\n"+g+"\n"+mo

q=n+".svg"
url=pyqrcode.create(z)
url.svg(q, scale =8)