from abc import ABC
from datetime import date
from backend import util

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
    
    def dar_de_alta_persona(self, 
                 nombre: str = None, 
                 apellido: str = None, 
                 cedula: int = -1, 
                 fecha_nacimiento: date = None, 
                 fecha_ingreso: date = None, 
                 celular: str = None):
        if nombre == None:
            nombre = util.input_nombre("Ingrese el nombre: ")
        if apellido == None:
            apellido = util.input_apellido("Ingrese el apellido: ")
        if cedula == -1:
            cedula = util.input_cedula("Ingrese la cédula de identidad: ")
        if fecha_nacimiento == None:
            fecha_nacimiento = util.input_fecha_nacimiento("Ingrese la fecha de nacimiento en formato aaaa-mm-dd: ")
        if fecha_ingreso == None:
            fecha_ingreso = util.input_fecha_ingreso("Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd: ")
        while fecha_ingreso < fecha_nacimiento:
            print("La fecha de ingreso no puede ser anterior a la fecha de nacimiento. Vuelva a ingresarlas.")
            fecha_nacimiento = util.input_fecha_nacimiento("Ingrese la fecha de nacimiento en formato aaaa-mm-dd: ")
            fecha_ingreso = util.input_fecha_ingreso("Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd: ")
        if celular == None:
            celular = util.input_celular("Ingrese el número de celular: ")
        
        self.nombre =           nombre
        self.apellido =         apellido
        self.cedula =           cedula
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_ingreso =    fecha_ingreso
        self.celular =          celular