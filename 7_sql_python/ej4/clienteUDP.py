import requests
import json
import os
import time

from datetime import datetime

import signal
import socket

class Lampara:

    def __init__(self, idLampara, name, ip, status):
        self.id = idLampara
        self.name = name
        self.ip = ip
        self.status = status
        self.flagCambio = False

    @staticmethod
    def ParserJson(linea):  
        idLampara = linea[0]  
        name = linea[1]
        ip = linea[2]
        status = linea[3]
        return Lampara(idLampara, name, ip, status)

        
class Lamparas:
    
    def __init__(self, url):
        self.lamparas = []   
        self.url = url
        
        self.RequestDB()
        self.CargarJson()
        

    def AgregarLampara(self, lampara):
        self.lamparas.append(lampara)

    def MostrarLamparas(self):
        os.system('clear')
        print(datetime.now())    
        for lampara in self.lamparas:
            print("{0}\t{1}\t\t\t{2}\t{3}".format(lampara.id, lampara.name, lampara.ip, lampara.status))

        
    def CargarJson(self):
        devicesJsonParsed = json.loads(self.jsonTexto)
        
        for device in devicesJsonParsed:
            lampara = Lampara.ParserJson(device)
            self.AgregarLampara(lampara)


    def ActualizarJson(self):
        devicesJsonParsed = json.loads(self.jsonTexto)
        
        indice = 0
        
        for device in devicesJsonParsed:
            lampara = Lampara.ParserJson(device)
            if self.lamparas[indice].status != lampara.status:
                self.lamparas[indice].status = lampara.status
                self.lamparas[indice].flagCambio = True
            indice += 1  
        
        
    def RequestDB(self):

        r = requests.get(url = self.url + "/devices") 

        if r.status_code!=200:
            print("error code:"+str(r.status_code))
            exit()
            
        self.jsonTexto = r.text
        
    def ActualizarLamparasDB(self):
        self.RequestDB()
        self.ActualizarJson()    


class ServicioUDP:

    def handler_SIGINT(self, sig, frame):  # define the handler  
        #print("Signal Number:", sig, " Frame: ", frame)  
        #traceback.print_stack(frame)
        print("\nSaliendo cliente UDP Lamparas\n")
        self.s.close()
        exit()


    def __init__(self):
        self.puerto = 4096
        signal.signal(signal.SIGINT, self.handler_SIGINT)


    def Enviar(self, ip, trama):
    
        self.ip = ip
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.s.connect((self.ip, self.puerto))
            # print("Conectado a " + str(self.ip) + ":"+ str(self.puerto))
            self.s.send(bytearray(trama, 'utf-8'))
            self.s.close()
        except:
            print("No se pudo conectar a" + str(self.ip) + ":"+ str(self.puerto))
            return
            
    def EnviarVariaciones(self, lamparas):
        
        for lampara in lamparas:
            if (lampara.flagCambio == True):
                lampara.flagCambio = False
                if lampara.status == 0:
                    self.Enviar(lampara.ip, ">ST:OFF\n")
                else:
                    self.Enviar(lampara.ip, ">ST:ON\n")
            

print("Cliente UDP Lamparas")
l = Lamparas("http://localhost:5000")    
l.MostrarLamparas()
sudp = ServicioUDP()
    

while True:
    
    time.sleep(1.5)

    l.ActualizarLamparasDB()
    sudp.EnviarVariaciones(l.lamparas)
    l.MostrarLamparas()    
