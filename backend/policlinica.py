from backend import persona
from backend import consulta_medica
from backend.especialidad import ListaEspecialidad
from backend.socio import ListaSocio
from backend.medico import ListaMedico

'''
+ dar_alta_medico()
+ dar_alta_consulta()
+ emitir_ticket()
+ realizar_consulta()
'''

class Policlinica:
    def __init__(self):
        self.especialidades = ListaEspecialidad()
        self.socios = ListaSocio()
        self.medicos = ListaMedico()
        

    def dar_alta_medico():
        pass
    
    def dar_alta_consulta():
        pass

    def emitir_ticket():
        pass

    def realizar_consulta():
        pass