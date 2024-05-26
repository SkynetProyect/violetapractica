from arbolheap import Paciente
from arbolheap import Heap

def registrarPaciente(sala):
    idpaciente = input("Ingrese el id del paciente: ")
    genero = input("Ingrese el genero del paciente: ")
    nombre = input("Ingrese el nombre del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))  # Convertir a entero
    triaje = int(input("Ingrese el triaje del paciente: "))  # Convertir a entero
    paciente = Paciente(idpaciente, genero, nombre, edad, triaje)
    sala.Registrar(paciente)
    print("Paciente registrado correctamente.")

def mostrarPacientes(sala):
    print("\nPacientes en la sala de urgencias:")
    if len(sala.heap) == 0:
        print("No hay pacientes registrados.")
    else:
        print(sala)
        sala.impresion()

sala = Heap()

while True:
    print("\nMenú:")
    print("1. Registrar paciente")
    print("2. Mostrar lista de pacientes")
    print("3. Salir")

    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        registrarPaciente(sala)
    elif opcion == "2":
        mostrarPacientes(sala)
    elif opcion == "3":
        break
    else:
        print("Ingrese una opción válida.")
