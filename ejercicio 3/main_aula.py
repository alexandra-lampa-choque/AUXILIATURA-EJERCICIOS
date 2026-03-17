from aula import Aula

estudiantes = [
    ("Luis", 98),
    ("Aracely", 88)
]
aula1 = Aula("Aula 101", 2, estudiantes)
print("=== DATOS DEL AULA ===")
aula1.mostrar()
print("\n=== ESTADO DE ESTUDIANTES ===")
aula1.mostrar("estado")