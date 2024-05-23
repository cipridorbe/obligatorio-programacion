import backend.consulta_medica
import backend.especialidad
import backend.medico
import backend.persona
import backend.policlinica
import backend.socio
import backend.util

# Entry point
def main():
    menu = \
"1. Dar de alta una especialidad\n\
2. Dar de alta un socio\n\
3. Dar de alta un médico\n\
4. Dar de alta una consulta médica\n\
5. Emitir un ticket de consulta\n\
6. Realizar consultas\n\
7. Salir del programa"
    while True:
        print("Seleccione una opción del menú:")
        print(menu)
        opcion = input().strip()
        match opcion:
            case "1": pass
            case "2": pass
            case "3": pass
            case "4": pass
            case "5": pass
            case "6": pass
            case "7": 
                print("Saliendo del programa")
                break
            case _: print("La opción seleccionada no es correcta, vuelva a intentar con otra opción.\n")
            

# Execute code
if __name__ == '__main__':
    main()