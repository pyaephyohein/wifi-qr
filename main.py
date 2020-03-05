#author = Pyae Phyo Hein
#idea from https://github.com/kokoye2007/wifi-qr
#31.12.2019
import sys
import os
import gen_qr
import sysfileread
def main():
    # os.remove("key.png")
    xdgop = "xdg-open '/tmp/key.png'"
    print('1) Generate QR Code')
    print('2) Scan QR Code')
    chmanu = input('Select Option ')
    if chmanu == "1":
        print('Input information : ')
        keyraw = sysfileread.regfile()
        key = str(keyraw)
        gen_qr.qrgen(key[4:])
        os.system(xdgop)
    elif chmanu == "2":
        print('hello')
    else:
        print('hello')
if __name__ == "__main__":
    main()