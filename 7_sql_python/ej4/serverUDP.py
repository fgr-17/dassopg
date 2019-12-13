import signal
import socket

class Main:

    def __init__(self):
        pass

    def main(self):

        port = 4096

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(("localhost", port))
        print("Escuchando en localhost:"+str(port)+"...")

        while True:
            (data, addr) = s.recvfrom(10)
            print(data)
#            s.sendto(bytearray("OK","utf-8"),addr)


m = Main()
m.main()
