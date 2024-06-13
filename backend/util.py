from datetime import date
from excepciones.excepciones import ExitException, NoneError, EmptyError, FechaInvalida, ParseIntError, NumeroAtencionNoDisponible


# --------------------- Parse section --------------------- #

def format_string(string: str) -> str:
    string = string.lower()
    string = string.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    string = string.split()
    string = " ".join(string)
    return string

def is_EXIT(string: str):
    if string == "EXIT":
        raise ExitException()

def parse_int(num: str):
    try:
        return int(num)
    except Exception as e:
        raise ParseIntError(num)

def verde(string: str) -> str:
    return f"\033[32;1m{string}\033[0m"

def rojo(string: str) -> str:
    return f"\033[31;1m{string}\033[0m"

def amarillo(string: str) -> str:
    return f"\033[33;1m{string}\033[0m"

def parse_nombre(nombre: str) -> str:
    is_EXIT(nombre)
    # Check for errors
    if nombre is None:
        raise NoneError("nombre")
        # raise TypeError("nombre no puede ser None")
    nombre = nombre.strip()
    if nombre == "":
        raise EmptyError("nombre", True)
    if not all(c.isalpha() or c.isspace() for c in nombre):
        raise ValueError("nombre debe contener solo letras y espacios")
    # Convert to lowercase and remove multiple spaces
    # nombre = nombre.lower()
    # split = nombre.split()
    # joined = " ".join(split)
    # return joined
    return format_string(nombre)

def parse_apellido(apellido: str) -> str:
    is_EXIT(apellido)
    # Check for errors
    if apellido is None:
        raise NoneError("apellido")
    apellido = apellido.strip()
    if apellido == "":
        raise EmptyError("apellido", True)
    if not all(c.isalpha() or c.isspace() for c in apellido):
        raise ValueError("apellido debe contener solo letras y espacios")
    # Convert to lowercase and remove multiple spaces
    # apellido = apellido.lower()
    # split = apellido.split()
    # joined = " ".join(split)
    # return joined
    return format_string(apellido)

def parse_cedula(cedula: str) -> int:
    is_EXIT(cedula)
    # Check for errors
    if cedula is None:
        raise NoneError("cédula")
    cedula = cedula.strip()
    if cedula == "":
        raise EmptyError("cédula", False)
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
    is_EXIT(celular)
    # Check for errors
    if celular is None:
        raise NoneError("número de celular")
    celular = celular.strip()
    if celular == "":
        raise EmptyError("número de celular", True)
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
    is_EXIT(fecha)
    if fecha is None:
        raise NoneError("fecha")
    try:
        return date.fromisoformat(fecha)
    except Exception as e:
        raise FechaInvalida(fecha)

def parse_fecha_nacimiento(fecha: str) -> date:
    is_EXIT(fecha)
    _fecha = parse_fecha(fecha)
    if _fecha > date.today():
        raise ValueError("La fecha de nacimiento debe ubicarse en el pasado")
    return _fecha

def parse_fecha_ingreso(fecha: str) -> date:
    is_EXIT(fecha)
    _fecha = parse_fecha(fecha)
    if _fecha > date.today():
        raise ValueError("La fecha de ingreso debe ubicarse en el presente o en el pasado")
    return _fecha

def parse_fecha_consulta(fecha: str) -> date:
    is_EXIT(fecha)
    _fecha = parse_fecha(fecha)
    if _fecha < date.today():
        raise ValueError("La fecha de la consulta debe ubicarse en el presente o en el futuro")
    return _fecha

# 1 (true) = bonificado
# 2 (false) = no bonificado
def parse_tipo(tipo: str) -> bool:
    is_EXIT(tipo)
    if tipo == None:
        raise NoneError("opción")
    tipo = tipo.strip()
    if tipo == "1":
        return True
    if tipo == "2":
        return False
    raise ValueError("opción debe ser 1 o 2")
  
def parse_precio(precio: str) -> int:
    is_EXIT(precio)
    _precio = parse_int(precio)
    if _precio < 0:
        raise ValueError("Precio no puede ser negativo")
    return _precio

def parse_opcion(opcion: str, _max: int) -> str:
    is_EXIT(opcion)
    _opcion = parse_int(opcion)
    if _opcion <= 0 or _opcion > _max:
        raise ValueError(f"Opcion no esta dentro del rango 1-{_max}")
    return _opcion

def parse_pacientes(precio: str) -> int:
    is_EXIT(precio)
    _precio = parse_int(precio)
    if _precio <= 0:
        raise ValueError("La cantidad de pacientes debe ser positiva")
    return _precio

def parse_numero_atencion(numero_input: str, numeros_disponibles: list) -> int:
    is_EXIT(numero_input)
    numero = parse_int(numero_input)
    if not (numero in numeros_disponibles):
        raise NumeroAtencionNoDisponible(numero)
    return numero

# --------------------- Input section --------------------- #

def __input_generico(msg: str, parse_func):
    while True:
        try:
            input_ = input(msg)
            return parse_func(input_)
        except ExitException as e:
            raise e
        except Exception as e:
            print(f"\033[31;1m{e}\033[0m")

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
            is_EXIT(input_)
            return parse_opcion(input_, _max)
        except ExitException as e:
            raise e
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
            is_EXIT(input_)
            return parse_numero_atencion(input_, numeros)
        except ExitException as e:
            raise e
        except Exception as e:
            print(f"\033[31;1m{e}\033[0m")

def input_dos_fechas() -> tuple[date, date]:
    while True:
        inicio = input_fecha("Ingrese la fecha de inicio en formato aaaa-mm-dd: ")
        fin = input_fecha("Ingrese la fecha final en formato aaaa-mm-dd: ")
        if fin >= inicio:
            return (inicio, fin)
        print("\033[31;1mLa fecha final debe ser posterior o igual a la inicial. Ingrese nuevamente las fechas.\033[0m]")