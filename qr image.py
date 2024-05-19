import pyqrcode
from pyqrcode import QRCode
ss=("image.svg")
a=('https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2F4k%2520wallpaper%2F&psig=AOvVaw1G0dX4fDJ3zi5yElLi4HxW&ust=1699510312436000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCNjPlrzfs4IDFQAAAAAdAAAAABAE')
url=pyqrcode.create(a)
url.svg(ss,scale=8)
