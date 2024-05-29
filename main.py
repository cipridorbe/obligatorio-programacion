from backend import consulta_medica
from backend import especialidad
from backend import medico
from backend import persona
from backend import policlinica
from backend import socio
from backend import util

menu_mensaje = \
"1. Dar de alta una especialidad\n\
2. Dar de alta un socio\n\
3. Dar de alta un médico\n\
4. Dar de alta una consulta médica\n\
5. Emitir un ticket de consulta\n\
6. Realizar consultas\n\
7. Salir del programa"


policlinica_main = policlinica.Policlinica()

# Entry point
def main():
    while True:
        opcion = menu()
        if opcion == 7:
            print("Saliendo del programa")
            break

       

def menu() -> int:
    print("Seleccione una opción del menú:")
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