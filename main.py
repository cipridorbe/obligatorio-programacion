import jsonpickle

import backend
from backend import consulta_medica
from backend.especialidad import Especialidad
from backend.medico import Medico
from backend import persona
from backend import policlinica
import backend.medico
from backend.socio import Socio
from backend import util

menu_mensaje = \
"\033[1m1. Dar de alta una especialidad\n\
2. Dar de alta un socio\n\
3. Dar de alta un médico\n\
4. Dar de alta una consulta médica\n\
5. Emitir un ticket de consulta\n\
6. Realizar consultas\n\
7. Salir del programa\033[0m"


policlinica_main = policlinica.Policlinica()

# Entry point
def main():
    load()
    while True:
        opcion = menu()
        if opcion == 7:
            save()
            print("Saliendo del programa")
            break
        match opcion: 
            case 1:
                dar_alta_especialidad()
            case 2:
                dar_alta_socio()
            case 3:
                dar_alta_medico()

# opcion 1
def dar_alta_especialidad():
    esp = Especialidad.dar_de_alta_especialidad(policlinica_main.especialidades)
    if esp != None:
        policlinica_main.especialidades.append(esp)
        print(f"La especialidad {esp.nombre} se ha creado con éxito.")

# opcion 2
def dar_alta_socio():
    soc = Socio.dar_de_alta_socio(policlinica_main.socios)
    if soc != None:
        policlinica_main.socios.append(soc)
        print(f"El socio con cédula {soc.cedula} se ha registrado con éxito.")

# opcion 3
def dar_alta_medico():
    medico = Medico.dar_de_alta_medico(policlinica_main.medicos, policlinica_main.especialidades)
    if medico != None:
        policlinica_main.medicos.append(medico)
        if not policlinica_main.especialidades.contains(medico.especialidad):
            policlinica_main.especialidades.append(medico.especialidad)
            print(f"La especialidad {medico.especialidad.nombre} se ha creado con éxito.")
        print(f"El medico con cédula {medico.cedula} se ha registrado con éxito.")

# opcion 7
def save():
    json = jsonpickle.encode(policlinica_main)
    with open("data.txt", "w") as data:
        data.write(json)

def load():
    global policlinica_main
    with open("data.txt") as data:
        json = data.read()
        policlinica_main = jsonpickle.decode(json)
    policlinica_main.medicos = backend.medico.ListaMedico()

def menu() -> int:
    print("\nSeleccione una opción del menú:")
    print(menu_mensaje)
    opcion = input().strip()
    match opcion:
        case "1": return 1
        case "2": return 2
        case "3": return 3
        case "4": return 4
        case "5": return 5
        case "6": return 6
        case "7": return 7
        case _: 
            print("La opción seleccionada no es correcta, vuelva a intentar con otra opción.\n")
            return menu()

# Execute code
if __name__ == '__main__':
    main()
