class Aula:

    def __init__(self, nombre, piso, estudiantes):
        self.nombre = nombre
        self.piso = piso
        self.estudiantes = estudiantes
    def mostrar(self, tipo=None):

        print("Nombre del aula:", self.nombre)
        print("Piso:", self.piso)

        if tipo is None:
            print("\nLista de estudiantes y notas:")
            for nombre, nota in self.estudiantes:
                print("Estudiante:", nombre, "| Nota:", nota)
        else:
            print("\nEstado de estudiantes:")
            for nombre, nota in self.estudiantes:
                if nota >= 51:
                    estado = "APROBADO"
                else:
                    estado = "REPROBADO"
                print("Estudiante:", nombre, "| Nota:", nota, "|", estado)

        print("--------------------------------")