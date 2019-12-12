import requests
import os

BASE_URL = "http://localhost:5000"

print("Cliente HTTP para pruebas")

while True:
    os.system('clear')
    print("\n1) GET a /devices")
    print("2) PUT a /device")
    print("3) GET a /log")
    print("4) Salir")

    op = int(input("Ingrese una opcion:"))

    if op==1:
        r = requests.get(url = BASE_URL+"/devices") 
        if r.status_code==200:
            print(r.text)
        else:
            print("error code:"+str(r.status_code))

    elif op==2:
        id_lamp = input("Ingrese ID de lampara:")
        state_lamp = input("Ingrese estado de lampara [0,1]:")
        data = {"state":state_lamp}
        r = requests.put(url = BASE_URL+"/device/"+id_lamp, data=data) 
        if r.status_code==200:
            print(r.text)
        else:
            print("error code:"+str(r.status_code))

    elif op==3:
        page = input("Ingrese numero de pagina:")
        size = input("Ingrese size de pagina:")
        data = {"page":page,"size":size}
        r = requests.get(url = BASE_URL+"/log",params=data) 
        if r.status_code==200:
            print(r.text)
        else:
            print("error code:"+str(r.status_code))

    elif op==4:
        break
