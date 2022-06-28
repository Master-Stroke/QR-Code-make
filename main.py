import qrcode

qr = qrcode.QRCode()
data = input('Введите что будет храниться в qrcode: ')
qr.add_data(data)
save = input('Введите названия файла: ')
img = qr.make_image()
img.save(save)