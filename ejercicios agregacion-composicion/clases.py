class Animal:
    def __init__(self, nombre, edad, nombreDueno):
        self.nombre = nombre
        self.edad = edad
        self.nombreDueno = nombreDueno


class Perro(Animal):
    def __init__(self, nombre, edad, nombreDueno, requiereBosal, ladraFuerte):
        Animal.__init__(self, nombre, edad, nombreDueno)
        self.requiereBosal = requiereBosal
        self.ladraFuerte = ladraFuerte


class Gato(Animal):
    def __init__(self, nombre, edad, nombreDueno, cazaRatones, tomaLeche):
        Animal.__init__(self, nombre, edad, nombreDueno)
        self.cazaRatones = cazaRatones
        self.tomaLeche = tomaLeche


class CentroVeterinario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.perros = []
        self.gatos = []

    def agregarPerro(self, perro):
        self.perros.append(perro)

    def agregarGato(self, gato):
        self.gatos.append(gato)

    def ordenarPerros(self):
        n = len(self.perros)
        for i in range(n):
            for j in range(n - 1):
                p1 = self.perros[j]
                p2 = self.perros[j + 1]

                if (p1.edad > p2.edad) or \
                   (p1.edad == p2.edad and p1.nombreDueno > p2.nombreDueno) or \
                   (p1.edad == p2.edad and p1.nombreDueno == p2.nombreDueno and p1.nombre > p2.nombre):

                    aux = self.perros[j]
                    self.perros[j] = self.perros[j + 1]
                    self.perros[j + 1] = aux

    def ordenarGatos(self):
        n = len(self.gatos)
        for i in range(n):
            for j in range(n - 1):
                g1 = self.gatos[j]
                g2 = self.gatos[j + 1]

                if (g1.tomaLeche == False and g2.tomaLeche == True) or \
                   (g1.tomaLeche == g2.tomaLeche and g1.edad < g2.edad) or \
                   (g1.tomaLeche == g2.tomaLeche and g1.edad == g2.edad and g1.nombre > g2.nombre):

                    aux = self.gatos[j]
                    self.gatos[j] = self.gatos[j + 1]
                    self.gatos[j + 1] = aux

    def verificarDueno(self):
        mostrados = []

        for i in range(len(self.perros)):
            dueno = self.perros[i].nombreDueno

            if dueno not in mostrados:
                contador = 0

                for p in self.perros:
                    if p.nombreDueno == dueno:
                        contador += 1

                for g in self.gatos:
                    if g.nombreDueno == dueno:
                        contador += 1

                if contador >= 2:
                    print(dueno, "tiene", contador, "animales")
                    mostrados.append(dueno)

        for i in range(len(self.gatos)):
            dueno = self.gatos[i].nombreDueno

            if dueno not in mostrados:
                contador = 0

                for p in self.perros:
                    if p.nombreDueno == dueno:
                        contador += 1

                for g in self.gatos:
                    if g.nombreDueno == dueno:
                        contador += 1

                if contador >= 2:
                    print(dueno, "tiene", contador, "animales")
                    mostrados.append(dueno)