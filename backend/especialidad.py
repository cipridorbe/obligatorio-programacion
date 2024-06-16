from backend import util

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
    def dar_de_alta_especialidad(lista):
        nombre = util.input_nombre("Ingrese el nombre de la especialidad: ")
        while lista.contains_str(nombre):
            print(util.amarillo("Esta especialidad ya existe."))
            if util.input_tipo("1 - Ingresar devuelta el nombre.\n2 - Salir.\n"):
                nombre = util.input_nombre("Ingrese el nombre de la especialidad: ")
            else:
                return None
        precio = util.input_precio("Ingrese el precio asociado: ")
        return Especialidad(nombre, precio)


class ListaEspecialidad:
    def __init__(self, length: int = 0):
        self.lista = [None] * length
    
    def contains(self, especialidad: Especialidad) -> bool:
        for esp in self.lista:
            if esp.nombre == especialidad.nombre:
                return True
        return False

    def contains_str(self, nombre_especialidad: str) -> bool:
        for esp in self.lista:
            if esp.nombre == nombre_especialidad:
                return True
        return False
    
    def search(self, nombre_especialidad: str) -> Especialidad:
        for esp in self.lista:
            if esp.nombre == nombre_especialidad:
                return esp
        return None
    
    def append(self, especialidad: Especialidad):
        self.lista.append(especialidad)
    
    def insert(self, index: int, especialidad: Especialidad):
        self.lista.insert(index, especialidad)