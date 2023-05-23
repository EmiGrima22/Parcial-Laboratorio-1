import json

def conseguir_lista_insumos_limpia(lista_insumos:list)-> int | list:
    """Quita los elementos vacios de la ultima posicion

    Args:
        lista_insumos (list): Lista a trabajar

    Returns:
        int | list: Retorna la lista si salio todo bien o -1 en caso contrario
    """

    if len(lista_insumos) > 0:
        lista_limpia= []    
        i = 0
        while i < len(lista_insumos)-1:
            lista_limpia.append(lista_insumos[i])
            i = i + 1
    
        return lista_limpia
    else:
        return -1

def leer_archivo_csv(nombre_archivo:str)->list | int:
    """ Lee un archivo CSV y lo transforma en una lista de elementos

    Args:
        nombre_archivo (str): El nombre del archivo csv

    Returns:
        list | int: Retorna la lista en caso de salir todo bien, de lo contrario -1
    """
    
    lista = []
    
    with open(nombre_archivo,"r", encoding='utf-8') as archivo:
        for linea in archivo:
            linea = linea.replace("\n","")
            linea = linea.split(",")
            lista.append(linea)
        
    if  len(lista) > 0 and not conseguir_lista_insumos_limpia(lista) == -1:
        lista = conseguir_lista_insumos_limpia(lista)
        return lista
    else:
        return -1

def escribir_archivo(nombre_archivo:str, datos:list):
    """Abre un archivo en modo escritura y lo escribe con datos de una lista

    Args:
        nombre_archivo (str): El nombre y la extension del archivo\n
        datos (list): La lista de datos a escribir en el archivo
    """
    with open(nombre_archivo,"w") as archivo:
        archivo.writelines("\n".join(datos))

def escribir_json(nombre_archivo:str, lista_filtrada:list):
    """Abre un archivo en modo escritura, si no existe lo crea. Y lo escribe con datos de una lista

    Args:
        nombre_archivo (str): Nombre y extension del archivo\n
        lista_filtrada (list): Lista filtrada de datos
    """
    with open(nombre_archivo, "w", encoding='utf-8') as archivo:
        json.dump(lista_filtrada, archivo, indent=4, separators=(", ", " : "), ensure_ascii=False)

def leer_json(nombre_archivo:str)->dict:
    """Abre un archivo json en modo lectura y carga los datos

    Args:
        nombre_archivo (str): _description_

    Returns:
        dict: Un diccionario con los datos del archivo cargado
    """
    
    with open(nombre_archivo, "r", encoding='utf-8') as archivo:
        datos = json.load(archivo)
    
    return datos
    
    