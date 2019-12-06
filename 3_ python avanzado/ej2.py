import sensores as sn
import time

a = sn.SensorHumedad(0)
print('get value de sensor de humedad:{0}'.format(a.get_value()))

b = sn.SensorTemperatura(1)
print('get value de sensor de temperatura:{0}'.format(b.get_value()))

listaSensores = [a, b]


while(1):
    time.sleep(5)
    sn.Sensor.log_sensores(listaSensores)
    




