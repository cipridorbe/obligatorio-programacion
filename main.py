import jsonpickle

from backend import policlinica
from excepciones.excepciones import ExitException

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
    load()
    print("\033[1mIngrese EXIT en cualquier momento para volver al menu principial\033[0m")
    while True:
        try:
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

# # opcion 6
# def realizar_consulta():
#     print("Seleccione una opción:\n\
# 1. Obtener todos los médicos asociados a una especialidad específica.\n\
# 2. Obtener el precio de una consulta de una especialidad en específico.\n\
# 3. Listar todos los socios con sus deudas asociadas en orden ascendente.\n\
# 4. Realizar consultas respecto a cantidad de consultas entre dos fechas\n\
# 5. Realizar consultas respecto a las ganancias obtenidas entre dos fechas.\n\
# 6. Salir")
#     opcion = input().strip()
#     match opcion:
#         case "1":
#             medicos_asociados_a_especialidad()
#         case "2":
#             obtener_precio_de_consulta()
#         case "3":
#             listar_deudas_ascendente()
#         case "4":
#             consultas_entre_fechas()
#         case "5":
#             ganancias_entre_fechas()
#         case "6":
#             return
#         case _:
#             print("Opción inválida.")
#             realizar_consulta()

# # opcion 6.1
# def medicos_asociados_a_especialidad():
#     especialidad_nombre = util.input_nombre("Ingrese la especialidad: ")
#     medicos = policlinica_main.medicos.search_especialidad(especialidad_nombre)
#     if medicos.length() > 0:
#         for medico in medicos.lista:
#             print(f" • {medico.nombre} {medico.apellido}")
#     else:
#         if policlinica_main.especialidades.contains_str(especialidad_nombre):
#             print("La especialidad existe pero no hay médicos asociados.")
#         else:
#             print(f"La especialidad {especialidad_nombre} no existe.")

# # opcion 6.2
# def obtener_precio_de_consulta():
#     especialidad_nombre = util.input_nombre("Ingrese la especialidad: ")
#     especialidad = policlinica_main.especialidades.search(especialidad_nombre)
#     if especialidad != None:
#         print(f"El precio de la especialidad es: {especialidad.precio}.")
#     else:
#         print(f"La especialidad {especialidad_nombre} no existe.")

# # opcion 6.3
# def listar_deudas_ascendente():
#     socios = policlinica_main.socios.lista
#     if len(socios) == 0:
#         print("No hay socios asociados.")
#         return
#     ordenados = sorted(socios, key=lambda socio: socio.deuda)
#     # ordenados = reversed(ordenados)
#     for socio in ordenados:
#         print(f"{socio.nombre} {socio.apellido}, {socio.deuda}")

# # opcion 6.4
# def consultas_entre_fechas():
#     (inicio, fin) = util.input_dos_fechas()
#     consultas = policlinica_main.consultas.consultas_entre_fechas(inicio, fin)
#     if consultas.length() == 0:
#         print(f"No se encontraron consultas entre {inicio} y {fin}.")
#         return
#     consultas_ordenadas = sorted(consultas.lista, key=lambda consulta: consulta.fecha)
#     print(f"Se encontraron {len(consultas_ordenadas)} consultas entre {inicio} y {fin}.")
#     print(f"Desea ver las consultas")
#     if util.input_tipo("1- Sí   2- No:  "):
#         for consulta in consultas_ordenadas:
#             print(consulta)

# # opcion 6.5
# def ganancias_entre_fechas():
#     (inicio, fin) = util.input_dos_fechas()
#     consultas = policlinica_main.consultas.consultas_entre_fechas(inicio, fin)
#     if consultas.length() == 0:
#         print(f"No se encontraron consultas entre {inicio} y {fin}.")
#         return
#     ganancias = 0
#     for consulta in consultas.lista:
#         precio = consulta.especialidad.precio
#         for paciente in consulta.pacientes.lista:
#             if paciente == None:
#                 continue
#             ganancias += precio * (1 - paciente.tipo * 0.2)
#     print(f"Las ganancias entre {inicio} y {fin} son ${ganancias}.")

# opcion 7
def save():
    jsonpickle.set_encoder_options('json', indent=4)
    json = jsonpickle.encode(policlinica_main)
    with open("data.txt", "w") as data:
        data.write(json)

def load():
    global policlinica_main
    with open("data.txt") as data:
        json = data.read()
        policlinica_main = jsonpickle.decode(json)

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
            print("La opción seleccionada no es correcta, vuelva a intentar con otra opción.")
            return menu()

# Execute code
if __name__ == '__main__':
    main()
