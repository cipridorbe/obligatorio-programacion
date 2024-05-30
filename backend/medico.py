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
    
    # @staticmethod
    # def dar_de_alta_medico():
    #     vacio = Medico(None, None, 0, None, None, None)
    #     vacio.dar_de_alta_persona()
    #     return vacio

    @staticmethod
    def dar_de_alta_medico(lista_medicos, lista_especialidades):
        vacio = Medico(None, None, 0, None, None, None, None)
        cedula = util.input_cedula("Ingrese la cédula de identidad: ")
        while lista_medicos.contains(cedula):
            print("Esta cédula ya está registrada.")
            if util.input_tipo("1 - Ingresar una nueva cédula.\n2 - Salir.\n"):
                cedula = util.input_cedula("Ingrese la cédula de identidad: ")
            else:
                return None
        vacio.dar_de_alta_persona(cedula)
        especialidad_nombre = util.input_nombre("Ingrese la especialidad: ")
        especialidad = lista_especialidades.search(especialidad_nombre)
        while especialidad == None:
            print("Esta especialidad no está dada de alta, elija una opción:")
            if util.input_tipo(f"1 - Volver a ingresar la especialidad\n2 - Dar de alta la especialidad {especialidad_nombre}\n"):
                especialidad_nombre = util.input_nombre("Ingrese la especialidad: ")
                especialidad = lista_especialidades.search(especialidad_nombre)
            else:
                precio = util.input_precio("Ingrese el precio asociado: ")
                especialidad = Especialidad(especialidad_nombre, precio)
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
    
    def append(self, medico: Medico):
        self.lista.append(medico)
    
    def insert(self, index: int, medico: Medico):
        self.lista.insert(index, medico)