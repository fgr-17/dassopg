class Gpio:

    salida = 0
    path0 = './gpio_'
    path1 = '.data'

    def __init__(self, salida):
        self.salida = salida        

    def set_state(self, estadoBool):
        path = Gpio.path0 + str(self.salida) + Gpio.path1
        fp = open(path, 'w')

        if(estadoBool == True):
            fp.write('1')
        else:
            fp.write('0')


    def get_state(self):
        path = Gpio.path0 + str(self.salida) + Gpio.path1
        fp = open(path, 'r')
        valorGuardado = fp.read(1)    

        print(valorGuardado)

        if(valorGuardado == "1"):
            return True
        elif(valorGuardado == "0"):
            return False
