class ExitException(Exception):
    def __init__(self):
        super().__init__()

class NoneError(Exception):
    def __init__(self, var: str):
        super().__init__(f"{var} no puede ser None")

class EmptyError(Exception):
    def __init__(self, var: str, masculino: bool):
        super().__init__(f"{var} no puede ser vací{"o" if masculino else "a"}")

class FechaInvalida(Exception):
    def __init__(self, fecha: str):
        super().__init__(f"la fecha {fecha} es de formato inválido")

class ParseIntError(Exception):
    def __init__(self, num: str):
        super().__init__(f"el número {num} es de formato incorrecto")

class NumeroAtencionNoDisponible(Exception):
    def __init__(self, numero: int):
        super().__init__(f"número {numero} no disponible")