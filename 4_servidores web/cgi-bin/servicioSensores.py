#!/usr/bin/env python3
import time
import sensores as sn

print("Content-Type: application/json\n")

datosLeidos = sn.Sensor.leer_log_sensores('./sensores/log_sensores.txt')

temp = datosLeidos[1]
hum = datosLeidos[2]

#print(temp, hum)

#print('{\"temp\":\"{0}\", \"hum\":\"{1}\"}'.format(temp, hum))


print('{\"temp\":\"' + temp + '\", \"hum\":\"' + hum + '\"}')
