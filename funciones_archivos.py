def conseguir_lista_insumos_limpia(lista_insumos:list):

    if len(lista_insumos) > 0:
        lista_limpia= []    
        i = 0
        while i < len(lista_insumos)-1:
            lista_limpia.append(lista_insumos[i])
            i = i + 1
    
        return lista_limpia
    else:
        return -1

def leer_archivo(nombre_archivo:str)->list:
    
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

