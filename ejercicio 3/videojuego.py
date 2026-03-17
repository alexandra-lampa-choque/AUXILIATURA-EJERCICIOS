class Videojuego:
    def __init__(self, nombre="", plataforma="", jugadores=0):
        self.nombre = nombre
        self.plataforma = plataforma
        self.jugadores = jugadores
    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Plataforma:", self.plataforma)
        print("Cantidad de jugadores:", self.jugadores)
        print("-----------------------------")
    def agregarJugadores(self, cantidad=None):
        if cantidad is None:
            self.jugadores += 1
        else:
            #v4rios jugadores
            self.jugadores += cantidad