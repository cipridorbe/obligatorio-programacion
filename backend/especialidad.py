from backend import util
from main import policlinica_main

'''
Especialidad
- Nombre
- Precio

 * Consulta medica
 * Medico
'''

class Especialidad:
    def __init__(self, nombre: str, precio: int):
        self.nombre = nombre
        self.precio = precio
    
    @staticmethod
    def dar_de_alta_especialidad():
        nombre = util.parse_nombre("Ingrese el nombre de la especialidad: ")
        while policlinica_main.lista_especialidad.contains(nombre):
            nombre = util.parse_nombre("Esta especialidad ya existe.\n1 - Ingresar devuelta el nombre.\n2 - Salir.")
        precio = util.input_precio("Ingrese el precio asociado: ")
        return Especialidad(nombre, precio)


class ListaEspecialidad:
    def __init__(self, length: int):
        self.lista = [None] * length
    
    def contains(self, especialidad: Especialidad) -> bool:
        for esp in self.lista:
            if esp.nombre == especialidad.nombre:
                return True
        return False

    def contains(self, nombre_especialidad: str) -> bool:
        for esp in self.lista:
            if esp.nombre == nombre_especialidad:
                return True
        return False
    
    def append(self, especialidad: Especialidad):
        self.lista.append(especialidad)
    
    def insert(self, index: int, especialidad: Especialidad):
        self.lista.insert(index, especialidad)