from persona import Persona
class Estudiante(Persona):
    def __init__(self, nombre, carnet, edad, matricula, carrera):
        super().__init__(nombre, carnet, edad)
        self.matricula = matricula
        self.carrera = carrera
    def mostrar(self):
        super().mostrar()
        print("Matrícula:", self.matricula)
        print("Carrera:", self.carrera)
    def misma_carrera(self, otro):
        return self.carrera == otro.carrera