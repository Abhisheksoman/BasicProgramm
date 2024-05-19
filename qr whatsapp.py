import pyqrcode
a=('https://wa.me/qr/4YDILPIPJLUAC1')
ss=("my whatsapp.svg")
url=pyqrcode.create(a)
url.svg(ss, scale = 8)
