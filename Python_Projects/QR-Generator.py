# import qrcode as qr

# img = qr.make("https://google.com")
# img.save("Google.png")

import qrcode as qr
from PIL import Image

qr = qr.QRCode(version=1,
               error_correction=qr.constants.ERROR_CORRECT_H,
               box_size=10 , border=4)

qr.add_data("https://www.google.com")    #add URL and make QR Code instantally
qr.make(fit=True)
img = qr.make_image(fill_color="orange",back_color="white")   #set color
img.save("image.png")
