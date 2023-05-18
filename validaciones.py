from re import *

def validar_entero(string_num:str)->bool:
    """Valida que el string ingresado tenga solo numeros

    Args:
        string_num (str): El string a validar

    Returns:
        bool: True si tiene unicamente digitos y False en caso contrario
    """
    patron = compile("^[0-9]+$")
    
    if match(patron,string_num):
        return True
    else:
        return False