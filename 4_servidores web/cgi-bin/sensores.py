from datetime import datetime
import csv


class Sensor():

    def __init__(self, num):
        self.num = num

    def readfile(self, path):
        with open(path, 'r') as fp:
            linea = fp.readline()
            valSens = float(linea)
        return valSens

    def get_value(self):
        return 0

    @staticmethod
    def log_sensores(listaSensores):
        timestamp = datetime.now()
        path = './log_sensores.txt'
        l = len(listaSensores)

        with open(path, mode = 'a') as fp:
            fp_writer = csv.writer(fp, delimiter= ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            fila = [timestamp]
            for i in range(l):
                fila.append(listaSensores[i].get_value())
            
            fp_writer.writerow(fila)


    @staticmethod
    def leer_log_sensores(path):
        
        with open(path, mode = 'r') as fp:
            fp_reader = csv.reader(fp, delimiter = ',')

            for row in fp_reader:
                break

            return row

class SensorTemperatura(Sensor):

    def get_value(self):
        path = './temp{0}.data'.format(self.num)
        val = self.readfile(path)
        if val < 0:
            val = 0
        return val


class SensorHumedad (Sensor):

    def get_value(self):
        path = './hum{0}.data'.format(self.num)
        val = self.readfile(path)
        return val/10


