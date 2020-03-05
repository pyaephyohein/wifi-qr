import sys, qrcode
d = qrcode.decode()
if d.decode('out.png'):
    print ('result: '+ d.result)
else:
    print ('error: '+ d.error)