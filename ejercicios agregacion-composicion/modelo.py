class Libro:
    def __init__(self, nombre, autor, anio):
        self.nombre = nombre
        self.autor = autor
        self.anio = anio

    def __str__(self):
        return f"{self.nombre} | {self.autor} | {self.anio}"


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = [0]*100
        self.cantLibros = 0

    def agregarLibro(self, libro):
        if self.cantLibros < 100:
            self.libros[self.cantLibros] = libro
            self.cantLibros += 1

    def buscarLibro(self, nombreBuscado):
        for i in range(self.cantLibros):
            if self.libros[i].nombre == nombreBuscado:
                print(f"Encontrado en {self.nombre}: {self.libros[i]}")
                return True
        return False

    def mostrar(self):
        print(f"\nBiblioteca: {self.nombre}")
        for i in range(self.cantLibros):
            print(self.libros[i])