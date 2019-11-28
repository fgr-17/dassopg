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
    


p0 = Persona("juan", 13)
p0.print_persona()
print(p0.es_mayor_de_edad())


p1 = Persona("Pepe", 81)
p1.print_persona()
print(p1.es_mayor_de_edad())

print(p1.nombre + " es mayor que " + p0.nombre + "??")
print(p1.es_mayor_que(p0))

px = Persona.get_mayor(p0, p1)
print("el mayor de los dos es: ")
px.print_persona()




