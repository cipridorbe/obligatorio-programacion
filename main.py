from backend import policlinica
from excepciones.excepciones import ExitException

serialization_on = True
try:
    import jsonpickle
except Exception:
    serialization_on = False

menu_mensaje = \
"\033[1m    1. Dar de alta una especialidad\n\
    2. Dar de alta un socio\n\
    3. Dar de alta un médico\n\
    4. Dar de alta una consulta médica\n\
    5. Emitir un ticket de consulta\n\
    6. Realizar consultas\n\
    7. Salir del programa\033[0m"


policlinica_main = policlinica.Policlinica()

# Entry point
def main():
    if serialization_on:
        load()
    print("\033[1mIngrese EXIT en cualquier momento para volver al menu principial\033[0m")
    while True:
        try:
            if serialization_on:
                save()
            opcion = menu()
            if opcion == 7:
                print("Saliendo del programa")
                break
            match opcion: 
                case 1:
                    dar_alta_especialidad()
                case 2:
                    dar_alta_socio()
                case 3:
                    dar_alta_medico()
                case 4:
                    dar_alta_consulta_medica()
                case 5:
                    emitir_ticket_de_consulta()
                case 6:
                    realizar_consulta()
        except ExitException:
            print("Se ha vuelto al menú con éxito.")

# opcion 1
def dar_alta_especialidad():
    policlinica_main.dar_alta_especialidad()

# opcion 2
def dar_alta_socio():
    policlinica_main.dar_alta_socio()

# opcion 3
def dar_alta_medico():
    policlinica_main.dar_alta_medico()

# opcion 4
def dar_alta_consulta_medica():
    policlinica_main.dar_alta_consulta_medica()

# opcion 5
def emitir_ticket_de_consulta():
    policlinica_main.emitir_ticket()

# opcion 6
def realizar_consulta():
    policlinica_main.realizar_consulta()

# opcion 7
def save():
    jsonpickle.set_encoder_options('json', indent=4)
    json = jsonpickle.encode(policlinica_main)
    with open("data.txt", "w") as data:
        data.write(json)

def load():
    global policlinica_main
    try:
        with open("data.txt") as data:
            json = data.read()
            policlinica_main = jsonpickle.decode(json)
    except Exception:
        pass

def menu() -> int:
    print("\033[1m\nSeleccione una opción del menú:\033[0m")
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
        case "EXIT": return 7
        case _: 
            print("\033[31;1mLa opción seleccionada no es correcta, vuelva a intentar con otra opción.\033[0m")
            return menu()

# Execute code
if __name__ == '__main__':
    main()
