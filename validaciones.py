import re

def validar_entero(string_num:str)->bool:
    """Valida que el string ingresado tenga solo numeros

    Args:
        string_num (str): El string a validar

    Returns:
        bool: True si tiene unicamente digitos y False en caso contrario
    """
    patron = re.compile("^[0-9]+$")
    
    if re.match(patron,string_num):
        return True
    else:
        return False

def validar_string_vacio(string:str)-> bool:
    patron = re.compile("^[ ]+$")
    
    if re.match(patron,string):
        return True
    else:
        return False