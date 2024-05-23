from datetime import date


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

def parse_tipo(tipo: str) -> bool


# --------------------- Input section --------------------- #

def __input_generico(msg: str, parse_func):
    while True:
        try:
            input_ = input(msg)
            return parse_func(input_)
        except Exception as e:
            print(e)

def input_nombre(msg: str) -> str:
    __input_generico(msg, parse_nombre)

def input_apellido(msg: str) -> str:
    __input_generico(msg, parse_apellido)

def input_cedula(msg: str) -> int:
    __input_generico(msg, parse_cedula)

def input_celular(msg: str) -> str:
    __input_generico(msg, parse_celular)

def input_fecha(msg: str) -> date:
    __input_generico(msg, parse_fecha)

def input_fecha_nacimiento(msg: str) -> date:
    __input_generico(msg, parse_fecha_nacimiento)

def input_fecha_ingreso(msg: str) -> date:
    __input_generico(msg, parse_fecha_ingreso)