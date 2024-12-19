# pip install qrcode & pillow in a virtual environment
#Generate a QR code for my GitHub profile

import qrcode

text = input('Enter a text or URL to generate a QR code: ').strip()
file_name = input('Enter the file name to save the QR code: ').strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(text)

image = qr.make_image(fill_color='black', back_color='white')
image.save(file_name)

print(f'QR code is saved as {file_name}')