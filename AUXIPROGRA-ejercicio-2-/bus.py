class Bus:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = 0
        self.precio_pasaje = 1.50
    def subir_pasajeros(self, cantidad):
        if self.pasajeros + cantidad <= self.capacidad:
            self.pasajeros += cantidad
            print("Pasajeros actuales:", self.pasajeros)
        else:
            print("No hay suficientes asientos")
    def cobrar_pasaje(self):
        total = self.pasajeros * self.precio_pasaje
        print("Total recaudado:", total, "Bs")
    def asientos_disponibles(self):
        disponibles = self.capacidad - self.pasajeros
        print("Asientos disponibles:", disponibles)