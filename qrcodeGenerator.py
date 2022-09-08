import qrcode
import os

screen_name = f"qrcode{0}.png"
dirCurrent = os.getcwd()
print("put your website to create qrCode: ", end='')
user_data = input()

qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(user_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save(screen_name)
print("created!")