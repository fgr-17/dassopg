import csv

class Persona:

    nombre = ""
    edad = 0

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad        

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def print_persona(self):
        print(self.nombre + " edad: " + str(self.edad))

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    def es_mayor_que(self, otro):
        if self.edad > otro.edad:
            return True
        else:
            return False

    @staticmethod
    def get_mayor(pa, pb):
        if pa.edad > pb.edad:
            return pa
        else:
            return pb
    
    @staticmethod
    def dump_csv(nombreArchivo, personas):
        with open(nombreArchivo, mode = 'w') as fp:
            fp_writer = csv.writer(fp, delimiter= ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for i in range(len(personas)):
                fp_writer.writerow([personas[i].nombre, personas[i].edad])

    @staticmethod
    def load_csv(nombreArchivo):
        listaPersonas = []

        with open(nombreArchivo) as fp:

            fp_reader = csv.reader(fp, delimiter=',')

            for row in fp_reader:
                paux = Persona(row[0], row[1])
                listaPersonas.append(paux)
            
        return listaPersonas

lista = Persona.load_csv("./datos")

for i in range(len(lista)):
    lista[i].print_persona()







