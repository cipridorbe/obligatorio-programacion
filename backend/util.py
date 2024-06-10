from datetime import date
from excepciones.excepciones import *


# --------------------- Parse section --------------------- #

def parse_nombre(nombre: str) -> str:
    # Check for errors
    if nombre is None:
        raise TypeError("nombre no puede ser None")
    nombre = nombre.strip()
    if nombre == "":
        raise ValueError("nombre no puede ser vacío")
    if not all(c.isalpha() or c.isspace() for c in nombre):
        raise ValueError("nombre debe contener solo letras y espacios")
    # Convert to lowercase and remove multiple spaces
    nombre = nombre.lower()
    split = nombre.split()
    joined = " ".join(split)
    return joined

def parse_apellido(apellido: str) -> str:
    # Check for errors
    if apellido is None:
        raise TypeError("apellido no puede ser None")
    apellido = apellido.strip()
    if apellido == "":
        raise ValueError("apellido no puede ser vacío")
    if not all(c.isalpha() or c.isspace() for c in apellido):
        raise ValueError("apellido debe contener solo letras y espacios")
    # Convert to lowercase and remove multiple spaces
    apellido = apellido.lower()
    split = apellido.split()
    joined = " ".join(split)
    return joined

def parse_cedula(cedula: str) -> int:
    # Check for errors
    if cedula is None:
        raise TypeError("cédula no puede ser None")
    cedula = cedula.strip()
    if cedula == "":
        raise ValueError("cédula no puede ser vacía")
    if not all(c.isnumeric() or c == "." or c == "," or c == "-" for c in cedula):
        raise ValueError("cédula debe contener solo números (puntos, comas, y guiones son aceptados)")
    # Remove . , - from cedula
    cedula = cedula.replace(".", "")
    cedula = cedula.replace(",", "")
    cedula = cedula.replace("-", "")
    if len(cedula) != 8:
        raise ValueError("cédula debe contener exactamente ocho dígitos")
    if cedula[0] == "0":
        raise ValueError("El primer dígito no puede ser 0")
    # convert to int and return
    return int(cedula)

def parse_celular(celular: str) -> str:
    # Check for errors
    if celular is None:
        raise TypeError("número de celular no puede ser None")
    celular = celular.strip()
    if celular == "":
        raise ValueError("número de celular no puede ser vacío")
    if not all(c.isnumeric() or c.isspace() for c in celular):
        raise ValueError("número de celular solo debe contener números")
    split = celular.split()
    joined = "".join(split)
    if len(joined) != 9:
        raise ValueError("número de celular debe contener nueve dígitos")
    if joined[0] != "0" or joined[1] != "9":
        raise ValueError("número de celular debe comenzar con 09")
    return joined

def parse_fecha(fecha: str) -> date:
    if fecha is None:
        raise TypeError("Fecha no puede ser None")
    try:
        return date.fromisoformat(fecha)
    except Exception as e:
        raise e

def parse_fecha_nacimiento(fecha: str) -> date:
    _fecha = parse_fecha(fecha)
    if _fecha > date.today():
        raise ValueError("La fecha de nacimiento debe ubicarse en el pasado")
    return _fecha

def parse_fecha_ingreso(fecha: str) -> date:
    _fecha = parse_fecha(fecha)
    if _fecha > date.today():
        raise ValueError("La fecha de ingreso debe ubicarse en el presente o en el pasado")
    return _fecha

def parse_fecha_consulta(fecha: str) -> date:
    _fecha = parse_fecha(fecha)
    if _fecha < date.today():
        raise ValueError("La fecha de la consulta debe ubicarse en el presente o en el futuro")
    return _fecha

# 1 (true) = bonificado
# 2 (false) = no bonificado
def parse_tipo(tipo: str) -> bool:
    if tipo == None:
        raise TypeError("Tipo no puede ser None")
    tipo = tipo.strip()
    if tipo == "1":
        return True
    if tipo == "2":
        return False
    raise ValueError("Tipo debe ser 1 o 2")

def parse_precio(precio: str) -> int:
    _precio = int(precio)
    if _precio < 0:
        raise ValueError("Precio no puede ser negativo")
    return _precio

def parse_opcion(opcion: str, _max: int) -> str:
    _opcion = int(opcion)
    if _opcion <= 0 or _opcion > _max:
        raise ValueError(f"Opcion no esta dentro del rango 1-{_max}")
    return _opcion

def parse_pacientes(precio: str) -> int:
    _precio = int(precio)
    if _precio <= 0:
        raise ValueError("La cantidad de pacientes debe ser positiva")
    return _precio

def parse_numero_atencion(numero_input: str, numeros_disponibles: list) -> int:
    numero = int(numero_input)
    if not (numero in numeros_disponibles):
        raise NumeroAtencionNoDisponible(numero)
    return numero

# --------------------- Input section --------------------- #

def __input_generico(msg: str, parse_func):
    while True:
        try:
            input_ = input(msg)
            return parse_func(input_)
        except Exception as e:
            print(e)

def input_nombre(msg: str) -> str:
    return __input_generico(msg, parse_nombre)

def input_apellido(msg: str) -> str:
    return __input_generico(msg, parse_apellido)

def input_cedula(msg: str) -> int:
    return __input_generico(msg, parse_cedula)

def input_celular(msg: str) -> str:
    return __input_generico(msg, parse_celular)

def input_fecha(msg: str) -> date:
    return __input_generico(msg, parse_fecha)

def input_fecha_nacimiento(msg: str) -> date:
    return __input_generico(msg, parse_fecha_nacimiento)

def input_fecha_ingreso(msg: str) -> date:
    return __input_generico(msg, parse_fecha_ingreso)

def input_tipo(msg: str) -> bool:
    return __input_generico(msg, parse_tipo)

def input_precio(msg: str) -> int:
    return __input_generico(msg, parse_precio)

def input_fecha_consulta(msg: str) -> date:
    return __input_generico(msg, parse_fecha_consulta)

def input_opcion(_max: int) -> int:
    while True:
        try:
            input_ = input()
            return parse_opcion(input_, _max)
        except Exception as e:
            print(e)

def input_pacientes(msg: str) -> int:
    return __input_generico(msg, parse_pacientes)

def input_numero_atencion(numeros: list) -> int:
    print("Seleccione el número de atención")
    for i in range(len(numeros)):
        if  i % 5 == 4:
            print(numeros[i])
        else:
            print(numeros[i], end=" \t")
    print()
    while True:
        try:
            input_ = input()
            return parse_numero_atencion(input_, numeros)
        except Exception as e:
            print(e)

def input_dos_fechas() -> tuple[date, date]:
    while True:
        inicio = input_fecha("Ingrese la fecha de inicio en formato aaaa-mm-dd: ")
        fin = input_fecha("Ingrese la fecha final en formato aaaa-mm-dd: ")
        if fin >= inicio:
            return (inicio, fin)
        print("La fecha final debe ser posterior a la inicial. Ingrese nuevamente las fechas.")