from socket import *
import random
port = 12000
s_soc = socket(AF_INET, SOCK_STREAM)
s_soc.bind(('localhost', port))
while True:

        con, addr = s_soc.accept()
        data = con.recv(4096).decode()
        data = data.split(,)
        print("C Name: ",data[0])
        print("S Name: ",str(addr))
        rint = random.randint(1,100) + int(data[1])
        message = 'Server of Ankush Kamble,' + str(rint - int(data[1])) + "," + str(rint)
        con.send(resp.encode())
        print("Sent")
        con.close()
