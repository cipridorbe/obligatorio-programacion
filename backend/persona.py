from abc import ABC, abstractmethod
from datetime import date
import util

'''
Abstract class
- nombre
- apellido
- cedula
- fecha de nacimiento
- fecha de ingreso a institucion
- numero de celular
'''

class Persona(ABC):
    def __init__(self, 
                 nombre: str, 
                 apellido: str, 
                 cedula: int, 
                 fecha_nacimiento: date, 
                 fecha_ingreso: date, 
                 celular: str):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_ingreso = fecha_ingreso
        self.celular = celular
    
    def dar_de_alta_persona(self):
        self.nombre =           util.input_nombre("Ingrese el nombre: ")
        self.apellido =         util.input_apellido("Ingrese el apellido: ")
        self.cedula =           util.input_cedula("Ingrese la cédula de identidad: ")
        self.fecha_nacimiento = util.input_fecha_nacimiento("Ingrese la fecha de nacimiento en formato aaaa-mm-dd: ")
        self.fecha_ingreso =    util.input_fecha_ingreso("Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd: ")
        self.celular =          util.input_numero_celular("Ingrese el número de celular: ")    