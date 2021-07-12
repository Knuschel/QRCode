#Generate
import pyqrcode
url = pyqrcode.create("https://computerbase.de", error = 'H')
print(url.png(r"C:\Users\joshu\PycharmProjects\Baby\Data\qrcode.png", scale=(8)))

#Decode
from PIL import Image
from pyzbar.pyzbar import decode
data = decode(Image.open(r"C:\Users\joshu\PycharmProjects\Baby\Data\qrcode.png"))
print(data)
