from datetime import date
from backend.persona import Persona
import backend.util

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
                 celular: str,):
        super().__init__(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, celular)
    
    @staticmethod
    def dar_de_alta_medico():
        vacio = Medico(None, None, 0, None, None, None)
        vacio.dar_de_alta_persona()
        return vacio
