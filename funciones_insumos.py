from funciones_archivos import *

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

def encabezado_insumos()->None:
    print("\n  ID           NOMBRE                        MARCA                    PRECIO                     CARACTERISTICAS\n")
    
def mostrar_insumo(insumo:dict):
    print(f"  {insumo['id']:5s} {insumo['nombre']:35s} {insumo['marca']:25s} {insumo['precio']:10} {insumo['caracteristicas']}")

def mostrar_insumos(lista:list)->None:
    encabezado_insumos()
    for insumo in lista:
        mostrar_insumo(insumo)

def cargar_datos_desde_archivo(nombre_archivo:str)-> list:
    lista_insumos = leer_archivo(nombre_archivo)
    insumos = fabricar_lista_diccionarios_insumos(lista_insumos)
    return insumos  

def filtrar_categoria(lista:list, key:str)->list:

    if len(lista) > 0:
        lista_filtrada = list(map(lambda insumo: insumo[key],lista))
        return lista_filtrada
    else:
        return -1
    
def contar_insumos_por_categoria(insumos:list)->dict:
    
    if len(insumos) > 0:
        categoria_cantidad = {}
        for item in insumos:
            if item in categoria_cantidad:
                categoria_cantidad[item] += 1
            else:
                categoria_cantidad[item] = 1
        
        return categoria_cantidad
    else:
        return -1

def mostrar_cantidad_por_categoria(cantidad_categoria:dict)->None:
    for categoria, cantidad in cantidad_categoria.items():
        print(f"{categoria:25}  |  {cantidad}")

def listar_cantidad_por_marca(lista_insumos:list)->None:
    marcas_insumos = filtrar_categoria(lista_insumos,"marca")
    cantidad_de_marcas = contar_insumos_por_categoria(marcas_insumos)
    mostrar_cantidad_por_categoria(cantidad_de_marcas)

def obtener_insumo_por_tipo(lista_insumos:list, set_datos:set, key_evaluar:str)-> dict:
    
    dic_tipo_nombres_precios = {}

    for set in set_datos:
        for insumo in lista_insumos:
            if insumo[key_evaluar] == set:
                if set not in dic_tipo_nombres_precios:
                    dic_tipo_nombres_precios[set] = []
                     
                dic_tipo_nombres_precios[set].append(f'{insumo["nombre"]:35s} {insumo["precio"]}')
                
    return dic_tipo_nombres_precios

def mostrar_marca_nombre_precio(dic_tipos:dict):
    print("\n MARCA                        NOMBRE                          PRECIO\n")
    for clave,valores in dic_tipos.items():
        for valor in valores:
            print(f"{clave:25s} {valor}")

def listar_insumos_por_marca(lista_insumos:list)->None:

    marcas = set(filtrar_categoria(lista_insumos,"marca"))
    dic_marcas_nombres_precios = obtener_insumo_por_tipo(lista_insumos, marcas, "marca")
    mostrar_marca_nombre_precio(dic_marcas_nombres_precios)

def buscar_coincidencias(lista:list, key:str, elemento_buscar:str):
    coincidencias = []

    for item in lista:
        if elemento_buscar in item[key]: 
            coincidencias.append(item)
    
    return coincidencias

def buscar_insumo_por_característica(lista_insumos:list, caracteristica_buscada:str):
    insumos_caracteristicas = buscar_coincidencias(lista_insumos, "caracteristicas", caracteristica_buscada)
    if len(insumos_caracteristicas) > 0:
        mostrar_insumos(insumos_caracteristicas)
    else:
        print("No hay insumos con esas caracteristicas")

def dejar_una_caracteristica(lista_insumos:list)->None:
    for insumo in lista_insumos:
        insumo["caracteristicas"] = insumo["caracteristicas"].split("~")
        insumo["caracteristicas"] = insumo["caracteristicas"][0]

def mostrar_insumos_con_una_caracteristica(lista_insumos):
    dejar_una_caracteristica(lista_insumos)
    mostrar_insumos(lista_insumos)

def reemplazar_caracter(lista:list,key:str, caracter_quitar:str, caracter_nuevo:str):
    for item in lista:
        item[key] = item[key].replace(caracter_quitar,caracter_nuevo)

def convertir_str_flotante(lista:list, key:str):

    for item in lista:
        try:
            item[key] = float(item[key])
            flag = True
        except:
            flag = False
    
    if flag:
        return flag

def ordenar_por_doble_criterio(lista:list, key_principal:str, key_secundaria:str)->None:
    tam = len(lista)

    for i in range(tam-1):
        for j in range(i+1, tam):
            if (lista[i][key_principal] > lista[j][key_principal]) or (lista[i][key_principal] == lista[j][key_principal] and lista[i][key_secundaria] < lista[j][key_secundaria]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    
    
def convertir_en_pesos(lista:list):
    for item in lista:
        item["precio"] = f"${item['precio']}"
    
def listar_insumos_ordenados(lista_insumos):
    reemplazar_caracter(lista_insumos, "precio", "$", "")
    if convertir_str_flotante(lista_insumos,"precio"):
        ordenar_por_doble_criterio(lista_insumos, "marca", "precio")
        convertir_en_pesos(lista_insumos)
        mostrar_insumos(lista_insumos)

def buscar_producto_esta(lista:list, key:str, producto_buscado:str) -> bool:

    flag_esta = False

    if len(lista) > 0:
        for insumo in lista:
            if producto_buscado == insumo[key]:
                flag_esta = True
                
    return flag_esta 

def calcular_subtotal(operando_a:int | float, operando_b:int | float)-> int | float:
    subtotal  =  operando_a * operando_b
    return subtotal