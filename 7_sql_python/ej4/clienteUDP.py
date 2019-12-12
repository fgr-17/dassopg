import requests
import json
import os
import time
from datetime import datetime

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

      




print("Cliente UDP Lamparas")


    
    
l = Lamparas("http://localhost:5000")    
l.MostrarLamparas()
    

while True:
    
    time.sleep(1.5)

    l.ActualizarLamparasDB()
    l.MostrarLamparas()    
