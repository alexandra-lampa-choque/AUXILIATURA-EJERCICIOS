class Persona:
    def __init__(self, nombre, carnet, edad):
        self.nombre = nombre
        self.carnet = carnet
        self.edad = edad
    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Carnet:", self.carnet)
        print("Edad:", self.edad)