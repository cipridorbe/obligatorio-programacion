from backend import util
from backend.especialidad import Especialidad, ListaEspecialidad
from backend.socio import Socio, ListaSocio
from backend.medico import Medico, ListaMedico
from backend.consulta_medica import ConsultaMedica, ListaConsultaMedica

'''
+ dar_alta_medico()
+ dar_alta_consulta()
+ emitir_ticket()
+ realizar_consulta()
'''

class Policlinica:
    def __init__(self):
        self.especialidades = ListaEspecialidad()
        self.socios = ListaSocio()
        self.medicos = ListaMedico()
        self.consultas = ListaConsultaMedica()
        

    def dar_alta_especialidad(self):
        esp = Especialidad.dar_de_alta_especialidad(self.especialidades)
        if esp != None:
            self.especialidades.append(esp)
            print(util.verde(f"La especialidad {esp.nombre} se ha creado con éxito."))

    def dar_alta_socio(self):
        soc = Socio.dar_de_alta_socio(self.socios)
        if soc != None:
            self.socios.append(soc)
            print(util.verde(f"El socio {soc.nombre} {soc.apellido} con cédula {soc.cedula} se ha registrado con éxito."))

    def dar_alta_medico(self):
        medico = Medico.dar_de_alta_medico(self.medicos, self.especialidades)
        if medico != None:
            self.medicos.append(medico)
            if not self.especialidades.contains(medico.especialidad):
                self.especialidades.append(medico.especialidad)
                print(util.verde(f"La especialidad {medico.especialidad.nombre} se ha creado con éxito."))
            print(util.verde(f"El medico {medico.nombre} {medico.apellido} con cédula {medico.cedula} se ha registrado con éxito."))

    def dar_alta_consulta_medica(self):
        consulta = ConsultaMedica.dar_de_alta_consulta(self.especialidades, self.medicos)
        if consulta != None:
            self.consultas.append(consulta)
            if not self.especialidades.contains(consulta.especialidad):
                self.especialidades.append(consulta.especialidad)
                print(util.verde(f"La especialidad {consulta.especialidad.nombre} se ha creado con éxito."))
            if not self.medicos.contains(consulta.medico):
                self.medicos.append(consulta.medico)
                print(util.verde(f"El médico {consulta.medico.nombre} {consulta.medico.apellido} se ha creado con éxito."))
            print(util.verde(f"La consulta de especialidad {consulta.especialidad.nombre} a cargo del médico {consulta.medico.nombre} {consulta.medico.apellido} ha creado con éxito"))

    def emitir_ticket(self):
        # especialidad
        especialidad_nombre = util.input_nombre("Ingrese la especialidad: ")
        especialidad = self.especialidades.search(especialidad_nombre)
        while especialidad == None:
                print(util.amarillo("Esta especialidad no está dada de alta, elija una opción:"))
                if util.input_tipo(f"1 - Volver a ingresar la especialidad\n2 - Dar de alta la especialidad {especialidad_nombre}\n"):
                    especialidad_nombre = util.input_nombre("Ingrese la especialidad: ")
                    especialidad = self.especialidades.search(especialidad_nombre)
                else:
                    precio = util.input_precio("Ingrese el precio asociado: ")
                    especialidad = Especialidad(especialidad_nombre, precio)
                    self.especialidades.append(especialidad)
        # consultas con especialidad 
        consultas = self.consultas.search_by_especialidad(especialidad_nombre)
        if consultas.length() == 0:
            print(util.rojo(f"No se encontraron consultas con la especialidad {especialidad_nombre}. Volviendo al menu principal."))
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
            print(util.rojo("No hay números de atención disponibles para esta consulta. Volviendo al menu principal."))
            return
        numero_atencion = util.input_numero_atencion(numeros_de_atencion_disponible)
        # socio
        cedula = util.input_cedula("Ingrese la cédula de identidad del socio: ")
        socio = self.socios.search_cedula(cedula)
        while socio == None:
            print(util.amarillo("Este socio no está dado de alta, elija una opción:"))
            if util.input_tipo(f"1 - Volver a ingresar el socio\n2 - Dar de alta el socio con cédula {cedula}\n"):
                cedula = util.input_cedula("Ingrese la cedula: ")
                socio = self.socios.search_cedula(cedula)
            else:
                socio = Socio.dar_de_alta_socio_sin_cedula(cedula)
                self.socios.append(socio)
        # agregar socio a consulta
        consulta.pacientes.lista[numero_atencion-1] = socio
        socio.deuda += especialidad.precio * (1 - socio.tipo * 0.2)
        print(util.verde(f"Se ha emitido el ticket con número {numero_atencion} para el socio {socio.nombre} {socio.apellido} con éxito"))

        # opcion 6
    def realizar_consulta(self):
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
                self.medicos_asociados_a_especialidad()
            case "2":
                self.obtener_precio_de_consulta()
            case "3":
                self.listar_deudas_ascendente()
            case "4":
                self.consultas_entre_fechas()
            case "5":
                self.ganancias_entre_fechas()
            case "6":
                return
            case "EXIT":
                return
            case _:
                print(util.rojo("Opción inválida."))
                self.realizar_consulta()

    # opcion 6.1
    def medicos_asociados_a_especialidad(self):
        especialidad_nombre = util.input_nombre("Ingrese la especialidad: ")
        medicos = self.medicos.search_especialidad(especialidad_nombre)
        if medicos.length() > 0:
            for medico in medicos.lista:
                print(f" • {medico.nombre} {medico.apellido}")
        else:
            if self.especialidades.contains_str(especialidad_nombre):
                print(util.amarillo("La especialidad existe pero no hay médicos asociados."))
            else:
                print(util.rojo(f"La especialidad {especialidad_nombre} no existe."))

    # opcion 6.2
    def obtener_precio_de_consulta(self):
        especialidad_nombre = util.input_nombre("Ingrese la especialidad: ")
        especialidad = self.especialidades.search(especialidad_nombre)
        if especialidad != None:
            print(f"El precio de la especialidad es: {especialidad.precio}.")
        else:
            print(util.rojo(f"La especialidad {especialidad_nombre} no existe."))

    # opcion 6.3
    def listar_deudas_ascendente(self):
        socios = self.socios.lista
        if len(socios) == 0:
            print(util.rojo("No hay socios asociados."))
            return
        ordenados = sorted(socios, key=lambda socio: socio.deuda)
        ordenados = reversed(ordenados)
        for socio in ordenados:
            print(f"{socio.nombre} {socio.apellido}: {socio.deuda}")

    # opcion 6.4
    def consultas_entre_fechas(self):
        (inicio, fin) = util.input_dos_fechas()
        consultas = self.consultas.consultas_entre_fechas(inicio, fin)
        if consultas.length() == 0:
            print(util.rojo(f"No se encontraron consultas entre {inicio} y {fin}."))
            return
        consultas_ordenadas = sorted(consultas.lista, key=lambda consulta: consulta.fecha)
        print(f"Se encontraron {len(consultas_ordenadas)} consultas entre {inicio} y {fin}.")
        print("Desea ver las consultas")
        if util.input_tipo("1- Sí   2- No:  "):
            for consulta in consultas_ordenadas:
                print(consulta)

    # opcion 6.5
    def ganancias_entre_fechas(self):
        (inicio, fin) = util.input_dos_fechas()
        consultas = self.consultas.consultas_entre_fechas(inicio, fin)
        if consultas.length() == 0:
            print(util.rojo(f"No se encontraron consultas entre {inicio} y {fin}."))
            return
        ganancias = 0
        for consulta in consultas.lista:
            precio = consulta.especialidad.precio
            for paciente in consulta.pacientes.lista:
                if paciente == None:
                    continue
                ganancias += precio * (1 - paciente.tipo * 0.2)
        print(f"Las ganancias entre {inicio} y {fin} son ${ganancias}.")