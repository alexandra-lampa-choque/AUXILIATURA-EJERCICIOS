from clases import Perro, Gato, CentroVeterinario

def main():

    cv1 = CentroVeterinario("Centro 1")

    # Perros
    cv1.agregarPerro(Perro("Firulais", 5, "Ana", True, True))
    cv1.agregarPerro(Perro("Rex", 3, "Luis", False, True))

    # Gatos
    cv1.agregarGato(Gato("Michi", 2, "Ana", True, True))
    cv1.agregarGato(Gato("Pelusa", 4, "Carlos", False, False))

    print("Perros ordenados:")
    cv1.ordenarPerros()
    for p in cv1.perros:
        print(p.nombre, p.edad, p.nombreDueno)

    print("\nGatos ordenados:")
    cv1.ordenarGatos()
    for g in cv1.gatos:
        print(g.nombre, g.edad, g.nombreDueno)

    print("\nDueños repetidos:")
    cv1.verificarDueno()


main()