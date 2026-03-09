class Jugador:

    def __init__(self, nombre, diamantes):
        self.nombre = nombre
        self.diamantes = diamantes
class Servidor:
    def __init__(self):
        self.jugadores = []
        self.max_jugadores = 10
    def agregar_jugador(self, nombre, diamantes):
        if len(self.jugadores) < self.max_jugadores:
            jugador = Jugador(nombre, diamantes)
            self.jugadores.append(jugador)
            print("Jugador agregado:", nombre)
        else:
            print("Servidor lleno")
    def verificar_stacks(self):
        for jugador in self.jugadores:
            stacks = jugador.diamantes // 64
            print(jugador.nombre, "tiene", stacks, "stack(s)")
    def jugador_mas_diamantes(self):
        mayor = self.jugadores[0]
        for jugador in self.jugadores:
            if jugador.diamantes > mayor.diamantes:
                mayor = jugador
        print("Jugador con más diamantes:", mayor.nombre)
    def total_diamantes(self):
        total = 0
        for jugador in self.jugadores:
            total += jugador.diamantes
        print("Total diamantes:", total)