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


p0 = Persona("juan", 13)
p0.print_persona()
print(p0.es_mayor_de_edad())


p1 = Persona("Pepe", 81)
p1.print_persona()
print(p1.es_mayor_de_edad())
