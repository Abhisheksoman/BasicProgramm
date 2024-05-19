import pyqrcode
a=('https://youtu.be/i5WYp4wMXfc?si=Ag7szLllt60kaj2N')
ss=("abdul kalam.svg")
url=pyqrcode.create(a)
url.svg(ss, scale = 8)