import csv
import json

import socket
import os
import sys

import time
import signal
import traceback

class Moneda:

    def __init__(self, nombre):
        self.nombre = nombre
        self.compra = compra
        self.venta = venta

class Parser:

    @staticmethod
    def LeerArchivo(path):
        
        with open(path) as fp:
            fp_reader = csv.DictReader(fp, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            monedas = []
            cuenta = 0
            
            for row in fp_reader:
                monedas.append(row)
        
            monedas_json = json.dumps(monedas)
        
            return (monedas_json)
            
    @staticmethod            
    def ObtenerPathCSV():
        with open("./config.txt") as fp:
            path = fp.read()
            path = path[0:-1]   # saco el \n del final que mete el read()
            fp.close()
            return path
                

class Main:
    
    def __init__(self):
        pass

    def handler_SIGINT(self, sig, frame):  # define the handler  
        #print("Signal Number:", sig, " Frame: ", frame)  
        #traceback.print_stack(frame)
        print("\nSaliendo del servicio Parser\n")
        self.s.close()
        exit()

    def main(self):

        
        signal.signal(signal.SIGINT, self.handler_SIGINT)
        
        port = 10000
        
        try:
            port = int(sys.argv[1])
        except:
            print("Puerto incorrecto")
            exit(1)


        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.connect(("localhost", port))
        print("Escribiendo puerto "+str(port)+"...")
        
        while True:

            pathCSV = Parser.ObtenerPathCSV()
            divisas = Parser.LeerArchivo(pathCSV)
            
            bytesEnviados = self.s.send(bytearray(divisas, 'utf-8'))
            (data, addr) = self.s.recvfrom(len("OK"))
                    
            time.sleep(10)

m = Main()
m.main()

