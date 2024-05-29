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
    def dar_de_alta_socio():
        vacio = Socio(None, None, 0, None, None, None, False, 0.0)
        vacio.dar_de_alta_persona()
        vacio.tipo = util.input_tipo("Ingrese el tipo de socio: 1- Bonificado 2- No bonificado: ")
        vacio.deuda = 0.0
        return vacio
