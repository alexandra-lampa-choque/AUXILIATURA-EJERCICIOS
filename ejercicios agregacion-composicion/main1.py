from modelo import Libro, Biblioteca

def main():

    b1 = Biblioteca("Central")
    b2 = Biblioteca("Zona Sur")

    b1.agregarLibro(Libro("Python Basico", "Juan Perez", 2020))
    b1.agregarLibro(Libro("Estructuras", "Ana Lopez", 2018))

    b2.agregarLibro(Libro("Algoritmos", "Carlos Ruiz", 2019))
    b2.agregarLibro(Libro("Bases de Datos", "Maria Gomez", 2021))

    b1.mostrar()
    b2.mostrar()

    print("\n--- Buscando libro ---")
    nombre = "Algoritmos"

    encontrado = False

    if b1.buscarLibro(nombre):
        encontrado = True
    if b2.buscarLibro(nombre):
        encontrado = True

    if not encontrado:
        print("Libro no encontrado")

    print("\n--- Biblioteca con más libros ---")

    if b1.cantLibros > b2.cantLibros:
        print(f"Mayor: {b1.nombre}")
    elif b2.cantLibros > b1.cantLibros:
        print(f"Mayor: {b2.nombre}")
    else:
        print("Empate:")
        print(b1.nombre)
        print(b2.nombre)

main()