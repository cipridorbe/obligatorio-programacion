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
    
    def dar_de_alta_persona():
        nombre = util.input_nombre("Ingrese el nombre: ")
        apellido = util.input_apellido("Ingrese el apellido: ")
        cedula = util.input_cedula("Ingrese la cédula de identidad: ")
        