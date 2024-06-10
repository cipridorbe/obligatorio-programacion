import jsonpickle

import backend
from backend.consulta_medica import ConsultaMedica, ListaConsultaMedica
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
            case 4:
                dar_alta_consulta_medica()
            case 5:
                emitir_ticket_de_consulta()
            case 6:
                realizar_consulta()

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

# opcion 4
def dar_alta_consulta_medica():
    consulta = ConsultaMedica.dar_de_alta_consulta(policlinica_main.especialidades, policlinica_main.medicos)
    if consulta != None:
        policlinica_main.consultas.append(consulta)
        if not policlinica_main.especialidades.contains(consulta.especialidad):
            policlinica_main.especialidades.append(consulta.especialidad)
            print(f"La especialidad {consulta.especialidad.nombre} se ha creado con éxito.")
        if not policlinica_main.medicos.contains(consulta.medico):
            policlinica_main.medicos.append(consulta.medico)
            print(f"El médico {consulta.medico.nombre} {consulta.medico.apellido} se ha creado con éxito.")
        print("La consulta se ha creado con éxito")

# opcion 5
def emitir_ticket_de_consulta():
    # especialidad
    especialidad_nombre = util.input_nombre("Ingrese la especialidad: ")
    especialidad = policlinica_main.especialidades.search(especialidad_nombre)
    while especialidad == None:
            print("Esta especialidad no está dada de alta, elija una opción:")
            if util.input_tipo(f"1 - Volver a ingresar la especialidad\n2 - Dar de alta la especialidad {especialidad_nombre}\n"):
                especialidad_nombre = util.input_nombre("Ingrese la especialidad: ")
                especialidad = policlinica_main.especialidades.search(especialidad_nombre)
            else:
                precio = util.input_precio("Ingrese el precio asociado: ")
                especialidad = Especialidad(especialidad_nombre, precio)
                policlinica_main.especialidades.append(especialidad)
    # consultas con especialidad 
    consultas = policlinica_main.consultas.search_by_especialidad(especialidad_nombre)
    if consultas.length() == 0:
        print(f"No se encontraron consultas con la especialidad {especialidad_nombre}. Volviendo al menu principal.")
        return
    for i in range(consultas.length()):
        consulta = consultas.lista[i]
        print(f"{i+1} - Doctor: {consulta.medico.nombre} {consulta.medico.apellido}. Día de la consulta {consulta.fecha}")
    opcion = util.input_opcion(consultas.length())
    consulta = consultas.lista[opcion-1]
    # numero de atencion
    numeros_de_atencion_disponible = []
    for i in range(consulta.cantidad_pacientes):
        if consulta.pacientes.lista[i] == None:
            numeros_de_atencion_disponible.append(i+1)
    if len(numeros_de_atencion_disponible) == 0:
        print(f"No hay números de atención disponibles para esta consulta. Volviendo al menu principal.")
        return
    numero_atencion = util.input_numero_atencion(numeros_de_atencion_disponible)
    # socio
    cedula = util.input_cedula("Ingrese la cédula de identidad del socio: ")
    socio = policlinica_main.socios.search_cedula(cedula)
    while socio == None:
        print("Este socio no está dado de alta, elija una opción:")
        if util.input_tipo(f"1 - Volver a ingresar el socio\n2 - Dar de alta el socio con cédula {cedula}\n"):
            cedula = util.input_cedula("Ingrese la cedula: ")
            socio = policlinica_main.socios.search_cedula(cedula)
        else:
            socio = Socio.dar_de_alta_socio_sin_cedula(cedula)
            policlinica_main.socios.append(socio)
    # agregar socio a consulta
    consulta.pacientes.lista[numero_atencion-1] = socio
    socio.deuda += especialidad.precio * (1 - socio.tipo * 0.2)
    print("Se ha emitido el ticket con éxito")

# opcion 6
def realizar_consulta():
    print("Seleccione una opción:\n\
1. Obtener todos los médicos asociados a una especialidad específica.\n\
2. Obtener el precio de una consulta de una especialidad en específico.\n\
3. Listar todos los socios con sus deudas asociadas en orden ascendente.\n\
4. Realizar consultas respecto a cantidad de consultas entre dos fechas\n\
5. Realizar consultas respecto a las ganancias obtenidas entre dos fechas.\n\
6. Salir")
    opcion = input().strip()
    match opcion:
        case "1":
            medicos_asociados_a_especialidad()
        case "2":
            obtener_precio_de_consulta()
        case "3":
            listar_deudas_ascendente()
        case "4":
            consultas_entre_fechas()
        case "5":
            ganancias_entre_fechas()
        case "6":
            return
        case _:
            print("Opción inválida.")
            realizar_consulta()

# opcion 6.1
def medicos_asociados_a_especialidad():
    especialidad_nombre = util.input_nombre("Ingrese la especialidad: ")
    medicos = policlinica_main.medicos.search_especialidad(especialidad_nombre)
    if medicos.length() > 0:
        for medico in medicos.lista:
            print(f" • {medico.nombre} {medico.apellido}")
    else:
        if policlinica_main.especialidades.contains_str(especialidad_nombre):
            print("La especialidad existe pero no hay médicos asociados.")
        else:
            print(f"La especialidad {especialidad_nombre} no existe.")

# opcion 6.2
def obtener_precio_de_consulta():
    especialidad_nombre = util.input_nombre("Ingrese la especialidad: ")
    especialidad = policlinica_main.especialidades.search(especialidad_nombre)
    if especialidad != None:
        print(f"El precio de la especialidad es: {especialidad.precio}.")
    else:
        print(f"La especialidad {especialidad_nombre} no existe.")

# opcion 6.3
def listar_deudas_ascendente():
    socios = policlinica_main.socios.lista
    if len(socios) == 0:
        print("No hay socios asociados.")
        return
    ordenados = sorted(socios, key=lambda socio: socio.deuda)
    # ordenados = reversed(ordenados)
    for socio in ordenados:
        print(f"{socio.nombre} {socio.apellido}, {socio.deuda}")

# opcion 6.4
def consultas_entre_fechas():
    (inicio, fin) = util.input_dos_fechas()
    consultas = policlinica_main.consultas.consultas_entre_fechas(inicio, fin)
    if consultas.length() == 0:
        print(f"No se encontraron consultas entre {inicio} y {fin}.")
        return
    consultas_ordenadas = sorted(consultas.lista, key=lambda consulta: consulta.fecha)
    print(f"Se encontraron {len(consultas_ordenadas)} consultas entre {inicio} y {fin}.")
    print(f"Desea ver las consultas")
    if util.input_tipo("1- Sí   2- No:  "):
        for consulta in consultas_ordenadas:
            print(consulta)

# opcion 6.5
def ganancias_entre_fechas():
    (inicio, fin) = util.input_dos_fechas()
    consultas = policlinica_main.consultas.consultas_entre_fechas(inicio, fin)
    if consultas.length() == 0:
        print(f"No se encontraron consultas entre {inicio} y {fin}.")
        return
    ganancias = 0
    for consulta in consultas.lista:
        precio = consulta.especialidad.precio
        for paciente in consulta.pacientes.lista:
            if paciente == None:
                continue
            ganancias += precio * (1 - paciente.tipo * 0.2)
    print(f"Las ganancias entre {inicio} y {fin} son ${ganancias}.")

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
        case _: 
            print("La opción seleccionada no es correcta, vuelva a intentar con otra opción.\n")
            return menu()

# Execute code
if __name__ == '__main__':
    main()
