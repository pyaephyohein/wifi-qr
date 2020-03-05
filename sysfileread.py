import os
import re
def regfile():
    os.system("ls -l /etc/NetworkManager/system-connections/")
    catt = input("Enter wifiName:")
    os.system(f" sudo cat /etc/NetworkManager/system-connections/{catt} > /tmp/wifi.txt",)
    f = open("/tmp/wifi.txt",'r')
    with f as open_file:
        data = open_file.read()
        reg = []
        reg = re.findall(r'psk=.*',data)
        for i in reg:
            return i
        return regfile
        
    
