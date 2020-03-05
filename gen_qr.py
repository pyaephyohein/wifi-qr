import qrcode
def qrgen(key):
    img = qrcode.make(key)
    img.save('/tmp/key.png')
    
