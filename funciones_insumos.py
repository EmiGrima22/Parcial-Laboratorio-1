def fabricar_lista_diccionarios_insumos(lista:list)->list:
    
    if len(lista) > 0:
        
        lista_diccionarios_insumos = []
        
        claves = lista.pop(0)
        
        for elemento in lista:
            insumo = {}
            insumo[claves[0].lower()] = elemento[0]
            insumo[claves[1].lower()] = elemento[1]
            insumo[claves[2].lower()] = elemento[2]
            insumo[claves[3].lower()] = elemento[3]
            insumo[claves[4].lower()] = elemento[4]
            lista_diccionarios_insumos.append(insumo)

        return lista_diccionarios_insumos
    
    else:
        return -1

def encabezado_insumos():
    print("\n  ID           NOMBRE                        MARCA                    PRECIO                     CARACTERISTICAS\n")
    
def mostrar_insumo(insumo:dict):
    print(f"  {insumo['id']:5s} {insumo['nombre']:35s} {insumo['marca']:25s} {insumo['precio']:10} {insumo['caracteristicas']}")

def mostrar_insumos(lista:list):
    encabezado_insumos()
    for insumo in lista:
        mostrar_insumo(insumo)

