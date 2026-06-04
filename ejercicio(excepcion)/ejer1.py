class SueldoInvalidoException(Exception):
    def __init__(self):
        super().__init__("El sueldo no puede ser menor a 2500 Bs")

class CargoInvalidoException(Exception):
    def __init__(self):
        super().__init__("El cargo solo debe contener letras")

class Empleado:
    def __init__(self, nom, car, sue):
        self.__nombre = nom
        self.__cargo = car
        self.__sueldo = sue
    def __str__(self):
        return f"Nombre: {self.__nombre}, Cargo: {self.__cargo}, Sueldo: {self.__sueldo} Bs"

class Empresa:
    def __init__(self, nom):
        self.__nombre = nom
        self.__empleados = []
    def agregarEmpleado(self, emp):
        self.__empleados.append(emp)
    def mostrarEmpleados(self):
        print("\nEmpresa:", self.__nombre)
        for i in range(len(self.__empleados)):
            print(self.__empleados[i])

nomEmp = input("Nombre de la empresa: ")
empresa = Empresa(nomEmp)
n = int(input("Cantidad de empleados: "))

for i in range(n):
    print(f"\nEmpleado {i+1}")
    nombre = input("Nombre: ")
    while True:
        try:
            cargo = input("Cargo: ")
            for c in cargo:
                if c.isdigit():
                    raise CargoInvalidoException()
            break

        except CargoInvalidoException as e:
            print(e)
    try:
        sueldo = float(input("Sueldo: "))
        if sueldo < 2500:
            raise SueldoInvalidoException()
    except SueldoInvalidoException as e:
        print(e)
        print("Se asignará automáticamente 2500 Bs")
        sueldo = 2500
    emp = Empleado(nombre, cargo, sueldo)
    empresa.agregarEmpleado(emp)
empresa.mostrarEmpleados()