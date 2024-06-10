class NumeroAtencionNoDisponible(Exception):
    def __init__(self, numero: int):
        super().__init__(f"número {numero} no disponible")