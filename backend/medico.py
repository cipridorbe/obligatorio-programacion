from datetime import date
from backend.persona import Persona
from backend import util
from backend.especialidad import Especialidad

'''
Hereda Persona
- Tipo (true = bonificado, false = no bonificado)
- Deuda
'''

class Medico(Persona):
    def __init__(self, 
                 nombre: str, 
                 apellido: str, 
                 cedula: int, 
                 fecha_nacimiento: date, 
                 fecha_ingreso: date, 
                 celular: str,
                 especialidad):
        super().__init__(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, celular)
        self.especialidad = especialidad

    @staticmethod
    def dar_de_alta_medico(lista_medicos, lista_especialidades):
        vacio = Medico(None, None, 0, None, None, None, None)
        cedula = util.input_cedula("Ingrese la cédula de identidad: ")
        while lista_medicos.contains_cedula(cedula):
            print(util.amarillo("Esta cédula ya está registrada."))
            if util.input_tipo("1 - Ingresar una nueva cédula.\n2 - Salir.\n"):
                cedula = util.input_cedula("Ingrese la cédula de identidad: ")
            else:
                return None
        vacio.dar_de_alta_persona(cedula=cedula)
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
        vacio.especialidad = especialidad
        return vacio
    
    @staticmethod
    def dar_alta_medico_sin_nombre(nombre: str, lista_medicos, lista_especialidades):
        vacio = Medico(None, None, 0, None, None, None, None)
        cedula = util.input_cedula("Ingrese la cédula de identidad: ")
        while lista_medicos.contains(cedula):
            print(util.amarillo("Esta cédula ya está registrada."))
            if util.input_tipo("1 - Ingresar una nueva cédula.\n2 - Salir.\n"):
                cedula = util.input_cedula("Ingrese la cédula de identidad: ")
            else:
                return None
        vacio.dar_de_alta_persona(nombre=nombre, cedula=cedula)
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
                if especialidad == None:
                    return None
        vacio.especialidad = especialidad
        return vacio
    
    @staticmethod
    def dar_alta_medico_sin_nombre_apellido_especialidad(nombre: str, apellido: str, especialidad: Especialidad, lista_medicos):
        vacio = Medico(None, None, 0, None, None, None, None)
        cedula = util.input_cedula("Ingrese la cédula de identidad: ")
        while lista_medicos.contains_cedula(cedula):
            print(util.amarillo("Esta cédula ya está registrada."))
            if util.input_tipo("1 - Ingresar una nueva cédula.\n2 - Salir.\n"):
                cedula = util.input_cedula("Ingrese la cédula de identidad: ")
            else:
                return None
        vacio.dar_de_alta_persona(nombre=nombre, apellido=apellido, cedula=cedula)
        vacio.especialidad = especialidad
        return vacio


class ListaMedico:
    def __init__(self, length: int = 0):
        self.lista = [None] * length
    
    def contains(self, medico: Medico) -> bool:
        for soc in self.lista:
            if soc.cedula == medico.cedula:
                return True
        return False

    def contains_cedula(self, cedula_medico: int) -> bool:
        for soc in self.lista:
            if soc.cedula == cedula_medico:
                return True
        return False
    
    def search_cedula(self, cedula_medico: int) -> Medico:
        for medico in self.lista:
            if medico.cedula == cedula_medico:
                return medico
        return None

    def search_especialidad(self, especialidad_nombre: str):
        lista = ListaMedico()
        for medico in self.lista:
            if medico.especialidad.nombre == especialidad_nombre:
                lista.append(medico)
        return lista
    
    def search(self, nombre: str, apellido: str = None):
        lista = ListaMedico()
        for medico in self.lista:
            if medico.nombre == nombre:
                if apellido == None:
                    lista.append(medico)
                elif medico.apellido == apellido:
                    lista.append(medico)
        return lista
    
    def search_nombre_apellido(self, nombre_apellido: str):
        lista = ListaMedico()
        for medico in self.lista:
            if medico.nombre == nombre_apellido:
                lista.append(medico)
            elif medico.nombre + " " + medico.apellido == nombre_apellido:
                lista.append(medico)
        return lista

    def length(self) -> int:
        return len(self.lista)

    def append(self, medico: Medico):
        self.lista.append(medico)
    
    def insert(self, index: int, medico: Medico):
        self.lista.insert(index, medico)