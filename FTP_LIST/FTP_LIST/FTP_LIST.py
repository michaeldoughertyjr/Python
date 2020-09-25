import paramiko
import sys
import os
import datetime
import time

ts = time.time()
current_date = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d %H:%M:%S')

#BATCH_1
sftp1URL   =  '172.21.25.248'
sftp1User  =  'dsupport'
sftp1Pass  =  'd3vUsrpwd'

#BATCH_2
sftp2URL   =  '172.21.25.250'
sftp2User  =  'dsupport'
sftp2Pass  =  'd3vUsrpwd'

ssh1 = paramiko.SSHClient()
ssh2 = paramiko.SSHClient()
ssh1.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
ssh2.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
ssh1.connect(sftp1URL, username=sftp1User, password=sftp1Pass)
ssh2.connect(sftp2URL, username=sftp2User, password=sftp2Pass)
ftp1 = ssh1.open_sftp()
ftp2 = ssh2.open_sftp()
ftp1.chdir('/data/HCS/x12Stage')
ftp2.chdir('/data/HCS/x12Stage')

with open('C:/Users/mdougherty/Desktop/Analyst Resources/Python/FTP_LIST/FILE_LIST/FILE_LIST.txt', 'a') as write_to:
    
    for i in ftp1.listdir():
        lstatout=str(ftp1.lstat(i)).split()[0]
        if 'd' not in lstatout: write_to.write(current_date+', '+i+'\n')
    
    for i in ftp2.listdir():
        lstatout=str(ftp2.lstat(i)).split()[0]
        if 'd' not in lstatout: write_to.write(current_date+', '+i+'\n')

write_to.close()