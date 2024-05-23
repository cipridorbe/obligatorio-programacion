from datetime import date
from persona import Persona

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
    
    def dar_de_alta_socio():
        # super().__init__(None, None, None, None, None, None)
        super().dar_de_alta_persona()
