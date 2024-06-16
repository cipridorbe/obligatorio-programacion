from datetime import date
from backend.persona import Persona
from backend import util

'''
Hereda Persona
- Tipo (true = bonificado, false = no bonificado)
- Deuda
'''

class Socio(Persona):
    def __init__(self, 
                 nombre: str, 
                 apellido: str, 
                 cedula: int, 
                 fecha_nacimiento: date, 
                 fecha_ingreso: date, 
                 celular: str,
                 tipo: bool,
                 deuda: float):
        super().__init__(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, celular)
        self.tipo = tipo
        self.deuda = deuda

    @staticmethod
    def dar_de_alta_socio(lista):
        vacio = Socio(None, None, 0, None, None, None, False, 0.0)
        cedula = util.input_cedula("Ingrese la cédula de identidad: ")
        while lista.contains_cedula(cedula):
            print(util.amarillo("Esta cédula ya está registrada."))
            if util.input_tipo("1 - Ingresar una nueva cédula.\n2 - Salir.\n"):
                cedula = util.input_cedula("Ingrese la cédula de identidad: ")
            else:
                return None
        vacio.dar_de_alta_persona(cedula=cedula)
        vacio.tipo = util.input_tipo("Ingrese el tipo de socio: 1- Bonificado 2- No bonificado: ")
        vacio.deuda = 0.0
        return vacio
    
    @staticmethod
    def dar_de_alta_socio_sin_cedula(cedula: int):
        vacio = Socio(None, None, 0, None, None, None, False, 0.0)
        vacio.dar_de_alta_persona(cedula=cedula)
        vacio.tipo = util.input_tipo("Ingrese el tipo de socio: 1- Bonificado 2- No bonificado: ")
        vacio.deuda = 0.0
        return vacio
    

class ListaSocio:
    def __init__(self, length: int = 0):
        self.lista = [None] * length
    
    def contains(self, socio: Socio) -> bool:
        for soc in self.lista:
            if soc.cedula == socio.cedula:
                return True
        return False

    def contains_cedula(self, cedula_socio: int) -> bool:
        for soc in self.lista:
            if soc.cedula == cedula_socio:
                return True
        return False
    
    def search_cedula(self, cedula_socio: int) -> Socio:
        for soc in self.lista:
            if soc.cedula == cedula_socio:
                return soc
        return None

    def append(self, socio: Socio):
        self.lista.append(socio)
    
    def insert(self, index: int, socio: Socio):
        self.lista.insert(index, socio)