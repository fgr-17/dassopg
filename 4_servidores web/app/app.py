import requests
import time

#https://www.mocky.io/

URL = "http://localhost:8002/cgi-bin/servicioSensores.py"

while(1):
    time.sleep(5)
    r = requests.get(url = URL) 

    if r.status_code==200:
        print(r.text)
    else:
        print("error code:"+str(r.status_code))
