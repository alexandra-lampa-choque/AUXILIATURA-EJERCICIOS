from figuras import Cuadrado, Triangulo, Redondo

c1 = Cuadrado("rojo", 4)
c2 = Cuadrado("azul", 6)
t1 = Triangulo("verde", 3, 4, 5)
t2 = Triangulo("amarillo", 5, 5, 6)
r1 = Redondo("negro", 3)
r2 = Redondo("blanco", 5)

print("CUADRADOS")
print(c1)
print(c2)

print("\nTRIANGULOS")
print(t1)
print(t2)

print("\n REDONDOS")
print(r1)
print(r2)
print("\nCOMPARACION")
cuadrados = [c1, c2]
triangulos = [t1, t2]
for c in cuadrados:
    for t in triangulos:
        print(f"\nComparando {c.color} vs {t.color}")
        if c.obtenerArea() > t.obtenerArea():
            print("Mayor área: CUADRADO de color", c.color)
        elif c.obtenerArea() < t.obtenerArea():
            print("Mayor área: TRIANGULO de color", t.color)
        else:
            print("Ambos tienen la misma área")
