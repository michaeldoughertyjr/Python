import telnetlib
import os
import pyautogui
import pywinauto
import clipboard
import time

RSA_Path = 'C:/Program Files/RSA SecurID Software Token/'
RSA_Client = 'SecurID.exe'
app = pywinauto.Application().start('C:/Program Files/RSA SecurID Software Token/SecurID.exe')
app.windows()
str(pyautogui.hotkey('ctrl', 'c'))
RSAKey = clipboard.paste()
clipboard.copy('')


HOST = '172.21.2.76'
user = 'michael.dougherty@medecision.com'
password = b'392781' + RSAKey.encode('ascii')


tn = telnetlib.Telnet(HOST)
print(tn.read_eager())
tn.read_until(b'Username: ', 2)
tn.write(user.encode('ascii'))
tn.write(b'\n\r')
time.sleep(1)
print(tn.read_eager())
tn.read_until(b'Password: ', 2)
tn.write(b'392781' + RSAKey)
tn.write(b'\n\r')
time.sleep(1)
print(tn.read_all())


##tn.write(b'ls\n')
##tn.write(b'exit\n')

#print(tn.read_all())
