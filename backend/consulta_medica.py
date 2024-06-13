from backend import util
from datetime import date
from backend.socio import ListaSocio
from backend.especialidad import Especialidad
from backend.medico import Medico

'''
Consulta Medica
- Fecha

 * Socio
 1 medico
 1 especialidad
'''

class ConsultaMedica:
    def __init__(self, fecha: date, medico, cantidad_pacientes: int, especialidad):
        self.fecha = fecha
        self.medico = medico
        self.especialidad = especialidad
        self.cantidad_pacientes = cantidad_pacientes
        self.pacientes = ListaSocio(cantidad_pacientes)
    
    def __str__(self) -> str:
        return f"Consulta de {self.especialidad.nombre} por {self.medico.nombre} {self.medico.apellido}. \
Fecha: {self.fecha}. Cupos totales: {self.cantidad_pacientes}, cupos ocupados: {self.pacientes_anotados()}."

    def pacientes_anotados(self) -> int:
        return self.cantidad_pacientes - self.pacientes.lista.count(None)
    
    def dar_de_alta_consulta(lista_especialidades, lista_medicos):
        # especialidad
        especialidad_nombre = util.input_nombre("Ingrese la especialidad: ")
        especialidad = lista_especialidades.search(especialidad_nombre)
        while especialidad == None:
            print(util.amarillo("Esta especialidad no está dada de alta, elija una opción:"))
            if util.input_tipo(f"1 - Volver a ingresar la especialidad\n2 - Dar de alta la especialidad {especialidad_nombre}\n"):
                especialidad_nombre = util.input_nombre("Ingrese la especialidad: ")
                especialidad = lista_especialidades.search(especialidad_nombre)
            else:
                precio = util.input_precio("Ingrese el precio asociado: ")
                especialidad = Especialidad(especialidad_nombre, precio)
        
        # medico
        nombre_medico = util.input_nombre("Ingrese el nombre del médico: ")
        apellido_medico = util.input_apellido("Ingrese el apellido del médico: ")
        nombre_completo_medico = nombre_medico + " " + apellido_medico
        medicos = lista_medicos.search_nombre_apellido(nombre_completo_medico).search_especialidad(especialidad_nombre)
        while medicos.length() != 1:
            # Caso 1: no se encontro un medico
            if medicos.length() == 0:
                print(util.amarillo(f"El médico {nombre_completo_medico} con especialidad {especialidad_nombre} no se pudo encontrar, elija una opción:"))
                if util.input_tipo("1 - Volver a ingresar el médico\n2 - Dar de alta el médico\n"):
                    nombre_medico = util.input_nombre("Ingrese el nombre del médico: ")
                    apellido_medico = util.input_apellido("Ingrese el apellido del médico: ")
                    nombre_completo_medico = nombre_medico + " " + apellido_medico
                    medicos = lista_medicos.search_nombre_apellido(nombre_medico).search_especialidad(especialidad_nombre)
                else:
                    medico = Medico.dar_alta_medico_sin_nombre_apellido_especialidad(nombre_medico, apellido_medico, especialidad, lista_medicos)
                    if medico == None:
                        return None
                    medicos.append(medico)
            # Caso 2: se encontraron varios médicos
            else:
                print("Se han encontrado los siguientes médicos. Elija el médico: ")
                print("1 - Ingresar otro nombre")
                for i in range(0, medicos.length):
                    print(f"{i+2} - {medicos.lista[i].nombre} {medicos.lista[i].apellido} CI: {medico.lista[i].cedula}")
                opcion = util.input_opcion(medicos.length+2)
                if opcion == 1:
                    nombre_medico = util.input_nombre("Ingrese el nombre del médico: ")
                    medicos = lista_medicos.search(nombre_medico).search_especialidad(especialidad_nombre)
                else:
                    medico = medicos.lista[i-2]
                    medicos.lista = [medico]
        
        # fecha
        fecha = util.input_fecha_consulta("Ingrese la fecha de consulta: ")

        # Cantidad pacientes
        pacientes = util.input_pacientes("Ingrese la cantidad de pacientes: ")
    	
        return ConsultaMedica(fecha,medicos.lista[0], pacientes,especialidad)

class ListaConsultaMedica:
    def __init__(self, length: int = 0):
        self.lista = [None] * length
    
    def append(self, consulta: ConsultaMedica):
        self.lista.append(consulta)
    
    def insert(self, index: int, consulta: ConsultaMedica):
        self.lista.insert(index, consulta)
    
    def search_by_especialidad(self, especialidad_nombre):
        consultas = ListaConsultaMedica()
        for consulta in self.lista:
            if consulta.especialidad.nombre == especialidad_nombre:
                consultas.append(consulta)
        return consultas
    
    def length(self) -> int:
        return len(self.lista)
    
    def consultas_entre_fechas(self, inicio: date, fin: date):
        consultas = ListaConsultaMedica()
        for consulta in self.lista:
            if inicio <= consulta.fecha <= fin:
                consultas.append(consulta)
        return consultas
