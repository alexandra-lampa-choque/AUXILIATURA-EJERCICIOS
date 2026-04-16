from estudiante import Estudiante
from docente import Docente
est1 = Estudiante("Ana", 123, 20, 1001, "Sistemas")
est2 = Estudiante("Luis", 456, 25, 1002, "Industrial")

doc = Docente("Carlos", 789, 25, 10, 5000.0)

print("\nEstudiante 1")
est1.mostrar()
print("\nEstudiante 2")
est2.mostrar()
print("\nDocente")
doc.mostrar()
if est1.edad == doc.edad or est2.edad == doc.edad:
    print("\nAlgún estudiante tiene la misma edad que el docente")
else:
    print("\nNingún estudiante tiene la misma edad que el docente")
if est1.misma_carrera(est2):
    print("\nLos estudiantes están en la misma carrera")
else:
    print("\nLos estudiantes NO están en la misma carrera")