from funciones_archivos import *
from functools import reduce

def fabricar_lista_diccionarios_insumos(lista:list)->list:
    """Fabrica una lista de diccionarios a partir de una lista 

    Args:
        lista (list): Lista de elementos a transformar

    Returns:
        list: Lista con los diccionarios de cada elemento
    """
    
    if len(lista) > 0:
        
        lista_dict = []
        
        claves = lista.pop(0)
        
        for valor in lista:
            item = {}
            item[claves[0].lower()] = valor[0]
            item[claves[1].lower()] = valor[1]
            item[claves[2].lower()] = valor[2]
            item[claves[3].lower()] = valor[3]
            item[claves[4].lower()] = valor[4]
            lista_dict.append(item)

        return lista_dict
    
    else:
        return -1

def imprimir_dato(dato:str)->None:
    """Imprime una cadena

    Args:
        dato (str): Cadena a imprimir
    """
    print(dato)

def encabezado_insumos()->None:
    """Imprime el encabezado de insumos
    """
    
    imprimir_dato("\n  ID           NOMBRE                        MARCA                    PRECIO                     CARACTERISTICAS\n")

def mostrar_insumo(insumo:dict, formato = True):
    """Imprime un insumo en formato lista o diccionario

    Args:
        insumo (dict): El diccionario del insumo\n
        formato (bool, optional): En True en formato diccionario, False formato lista. Defaults to True.
    """
    if formato:
        imprimir_dato(f"\n ID: {insumo['id']}\n NOMBRE: {insumo['nombre']}\n MARCA: {insumo['marca']}\n PRECIO: {insumo['precio']}\n CARACTERISTICAS: {insumo['caracteristicas']}\n")
    else:
        imprimir_dato(f"  {insumo['id']:5s} {insumo['nombre']:35s} {insumo['marca']:25s} {insumo['precio']:10} {insumo['caracteristicas']}")

def mostrar_insumos(lista:list, formato = True):
    """Imprime los insumos en formato lista con un encabezado o en formato diccionario

    Args:
        lista (list): Lista de diccionarios de los insumos\n
        formato (bool, optional): En True en formato diccionario, False formato lista. Defaults to True.
    """
    if not formato:
        encabezado_insumos()  

    for insumo in lista:
        mostrar_insumo(insumo,formato) 

def cargar_datos_desde_archivo(nombre_archivo:str)-> list:
    """Lee un archivo CSV, carga los datos en una lista, fabrica una lista de diccionarios.

    Args:
        nombre_archivo (str): Nombre del archivo CSV fuente

    Returns:
        list: Lista de diccionarios o -1 si sale mal
    """
    if leer_archivo_csv(nombre_archivo) != -1:
        lista_insumos = leer_archivo_csv(nombre_archivo)
        insumos = fabricar_lista_diccionarios_insumos(lista_insumos)
        if insumos != -1:
            return insumos
        else:
            return -1
    else:
        return -1  

def filtrar_categoria(lista:list, key:str)-> list | int:
    """Filtra los elementos de un diccionario por clave(key)

    Args:
        lista (list): Lista de diccionarios a evaluar\n
        key (str): Clave del diccionario a filtrar

    Returns:
        list | int: Si sale bien la lista filtrada, de lo contrario -1
    """

    if len(lista) > 0:
        lista_filtrada = list(map(lambda insumo: insumo[key],lista))
        return lista_filtrada
    else:
        return -1
    
def contar_item_por_categoria(lista_filtrada:list)->dict:
    """Cuenta los items iguales en una lista y los agrega a un diccionario que tiene como clave el item y como valor la cantidad

    Args:
        lista_filtrada (list): Lista filtrada a contar los items

    Returns:
        dict: Si sale todo bien un diccionario con los items contados, de lo contrario -1
    """
    
    if len(lista_filtrada) > 0:
        
        categoria_cantidad = {}
        
        for insumo in lista_filtrada:
            if insumo in categoria_cantidad:
                categoria_cantidad[insumo] += 1
            else:
                categoria_cantidad[insumo] = 1
        
        return categoria_cantidad
    else:
        return -1

def mostrar_cantidad_por_categoria(cantidad_categoria:dict):
    """Imprime pares clave - valor de un diccionario

    Args:
        cantidad_categoria (dict): El diccionario a imprimir
    """
    for categoria, cantidad in cantidad_categoria.items():
        print(f" {categoria:22}     |      {cantidad}")

def listar_cantidad_por_marca(lista_insumos:list):
    """Filtra las marcas, obtiene la cantidad de marcas iguales y muestra en pantalla marca - cantidad

    Args:
        lista_insumos (list): Lista de insumos a trabajar
    """
    if len(lista_insumos) > 0:
        marcas_insumos = filtrar_categoria(lista_insumos,"marca")
        if not marcas_insumos == -1:
            cantidad_de_marcas = contar_item_por_categoria(marcas_insumos)
            if not cantidad_de_marcas == -1:
                imprimir_dato("\n  MARCA                     |   CANTIDAD\n")  
                mostrar_cantidad_por_categoria(cantidad_de_marcas)
            else:
                return -1
        else:
            return -1
    else:
        return -1


def listar_marca_nombre_precio(lista_insumos:list)->None:

    marcas_nombres_precios = list(map(lambda ins: [ins["marca"], ins["nombre"], ins["precio"]], lista_insumos))
    imprimir_dato("\n MARCA                        NOMBRE                          PRECIO\n")
    for item in marcas_nombres_precios:
        print(f"{item[0]:25s} {item[1]:35s} {item[2]}")
    

def buscar_coincidencias_caracteristicas(lista_insumos:list, elemento_buscar:str):
    insumo_con_esas_caracteristicas = []
    
    for insumo in lista_insumos:
        insumo["caracteristicas"] = insumo["caracteristicas"].split("~")
        
    for insumo in lista_insumos:
        if elemento_buscar in insumo["caracteristicas"]:
            insumo_con_esas_caracteristicas.append(insumo)
    
    for insumo in lista_insumos:
        insumo["caracteristicas"] = "~".join(insumo["caracteristicas"])
    
    return insumo_con_esas_caracteristicas

def buscar_insumo_por_característica(lista_insumos:list, caracteristica_buscada:str):
    insumos_con_esa_caracteristica = buscar_coincidencias_caracteristicas(lista_insumos,caracteristica_buscada)
      
    if len(insumos_con_esa_caracteristica) > 0:
        mostrar_insumos(insumos_con_esa_caracteristica, formato=False)
    else:
        print("No se encontro ese producto") 
    
    
def dejar_una_caracteristica(lista_insumos:list)->None:
    for insumo in lista_insumos:
        insumo["caracteristicas"] = insumo["caracteristicas"].split("~")
        insumo["caracteristicas"] = insumo["caracteristicas"][0]

def mostrar_insumos_con_una_caracteristica(lista_insumos):
    dejar_una_caracteristica(lista_insumos)
    mostrar_insumos(lista_insumos,formato= False)

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
    
    return flag

def copiar_lista(lista_original:list)->list:

    if len(lista_original) > 0:
        lista_aux = []
        for item in lista_original:
            lista_aux.append(item)
        return lista_aux
    else:
        return -1
    
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
    
def listar_insumos_ordenados(lista_copia):
    reemplazar_caracter(lista_copia, "precio", "$", "")
    if convertir_str_flotante(lista_copia,"precio"):
        ordenar_por_doble_criterio(lista_copia, "marca", "precio")
        convertir_en_pesos(lista_copia)
        mostrar_insumos_con_una_caracteristica(lista_copia)

def buscar_por_key(lista:list, buscado:str):

    flag = False

    for item in lista:
        if item == buscado:
            flag = True
    
    return flag

def calcular_subtotal(operando_a:int | float, operando_b:int | float)-> int | float:
    subtotal  =  operando_a * operando_b
    return subtotal

def buscar_insumos_por_key(lista_insumos, elemento_buscar, key):
    
    if len(lista_insumos) > 0:
        lista_filtrada = list(filter(lambda ins: ins[key] == elemento_buscar, lista_insumos))
        return lista_filtrada
    else:
        return -1

def obtener_dato(lista:list, key:str)->str:
    for item in lista:
        dato = item[key]
    
    return dato

def pedir_validar_entero(mensaje:str):
    
    try:
        entero = int(input(f"\n{mensaje}\n"))
        return entero
    except ValueError:
        print("Error! No ingresaste un entero")
        return False


def mostrar_dato(lista:list,encabezado:str)->None:
    print(f"\n  {encabezado}\n")
    for dato in lista:
        print(f"    {dato}")

def quitar_marcas_repetidas_mostrarlos(lista_insumos:list)->list:
    marcas = filtrar_categoria(lista_insumos, "marca")
    if marcas != -1:
        marcas = set(marcas)
        mostrar_dato(marcas,"MARCAS DISPONIBLES")
        return marcas
    else:
        return -1


def realizar_compras(lista_insumos):
    total_compra = []
    registro_compras = []

    while True:
        
        marcas = quitar_marcas_repetidas_mostrarlos(lista_insumos)
        
        while True:
            marca_buscar = input("\nIngrese la marca que desea\n")
            if buscar_por_key(marcas, marca_buscar):
                break
            else:
                print("No existe esa marca")

        marcas_disponibles = buscar_insumos_por_key(lista_insumos, marca_buscar, "marca")
        
        while True:
            while True:
                mostrar_insumos(marcas_disponibles)
                id_ingresada = input("\n¿Ingrese el ID del producto que desee?\n")
                id_productos = filtrar_categoria(marcas_disponibles,"id")

                if buscar_por_key(id_productos, id_ingresada):
                    break
                else:
                    print("El producto no se encontro")

            reemplazar_caracter(lista_insumos,"precio","$","")
            convertir_str_flotante(lista_insumos, "precio")

            producto_nombre = obtener_dato(marcas_disponibles, "nombre")
            producto_precio = obtener_dato(marcas_disponibles, "precio")

            while True:
                cantidad = pedir_validar_entero("Ingrese cantidad la cantidad que desee")
                if cantidad != False and cantidad > 0:
                    break
            
            subtotal = calcular_subtotal(producto_precio, cantidad)

            total_compra.append(subtotal)

            registro_compras.append(f"Cantidad: {cantidad} - Producto: {producto_nombre:35s} - Subtotal: ${subtotal:.2f}")

            convertir_en_pesos(lista_insumos)

            while True:
                continuar = input("¿Quiere continuar comprando? s/n\n").lower()
                if continuar == "s" or continuar == "n": 
                    break

            if continuar == "s" or continuar == "n":
                break

        if continuar == "n":
            break
        
    total_final = reduce(lambda act, ant: ant + act, total_compra)

    registro_compras.append(f"                                                            - Total:    ${total_final:.2f}")
    
    imprimir_dato(f"El total de la compra fue {total_final:.2f}")
    
    escribir_archivo("Factura_compra.txt",registro_compras)
    
def filtrar_escribir_json(lista_insumos:list, nombre_archivo:str, nombre_filtrar:str):
    
    insumos_filtrados_alimento = list(filter(lambda ins: nombre_filtrar in ins["nombre"],lista_insumos))
    escribir_json(nombre_archivo, insumos_filtrados_alimento)

def leer_mostrar_json(nombre_archivo):
    datos = leer_json(nombre_archivo)
    mostrar_insumos(datos, formato= False)

def calcular_aumento(lista_insumos:list, key, aumento):
    
    aumentos = list(map(lambda ins: round((ins[key] * aumento) + ins[key], 2),lista_insumos))
    return aumentos

def reemplazar_valores(lista_original:list, lista_reemplazar:list):
    for i in range(len(lista_original)):
        lista_original[i]["precio"] = lista_reemplazar[i]

def escribir_csv(lista_insumos:list):
    
    with open("insumos_2.csv", "w", encoding='utf-8') as file:
                    
        encabezado = lista_insumos[0].keys()
        
        linea_columna = ",".join(encabezado)
        file.write(linea_columna.upper() + "\n")

        for insumo in lista_insumos:
            linea = insumo.values()
            linea_columna_valores = ','.join(linea)
            file.write(linea_columna_valores + '\n')

def calcular_aplicar_guardar_archivo(lista_insumos:list):
    
    reemplazar_caracter(lista_insumos,"precio","$","")
    convertir_str_flotante(lista_insumos, "precio")
    aumentos = calcular_aumento(lista_insumos, "precio", 0.084)
    reemplazar_valores(lista_insumos, aumentos)
    convertir_en_pesos(lista_insumos)
    escribir_csv(lista_insumos)