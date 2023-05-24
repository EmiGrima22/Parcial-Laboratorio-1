from funciones_archivos import *
from functools import reduce

def fabricar_lista_diccionarios_insumos(lista:list)->list | int:
    """Fabrica una lista de diccionarios a partir de una lista 

    Args:
        lista (list): Lista de elementos a transformar

    Returns:
        list | int: Lista con los diccionarios de cada elemento, -1 en caso de lista vacia
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
    """Imprime un insumo en formato lista o diccionario, dependiendo el valor bool que le pase a formato

    Args:
        insumo (dict): El diccionario del insumo\n
        formato (bool, optional): En True en formato diccionario, False formato lista. Defaults en formato diccionario.
    """
    if formato:
        imprimir_dato(f"\n ID: {insumo['id']}\n NOMBRE: {insumo['nombre']}\n MARCA: {insumo['marca']}\n PRECIO: {insumo['precio']}\n CARACTERISTICAS: {insumo['caracteristicas']}\n")
    else:
        imprimir_dato(f"  {insumo['id']:5s} {insumo['nombre']:35s} {insumo['marca']:25s} {insumo['precio']:10} {insumo['caracteristicas']}")

def mostrar_insumos(lista:list, formato = True):
    """Imprime los insumos en formato lista con un encabezado o en formato diccionario

    Args:
        lista (list): Lista de diccionarios de los insumos\n
        formato (bool, optional): En True en formato diccionario, False formato lista. Defaults en formato diccionario.
    """
    if not formato:
        encabezado_insumos()  

    for insumo in lista:
        mostrar_insumo(insumo,formato) 

def cargar_datos_desde_archivo(nombre_archivo:str)-> list:
    """Lee un archivo CSV, carga los datos en una lista, fabrica una lista de diccionarios.

    Args:
        nombre_archivo (str): Nombre del archivo CSV fuente de datos

    Returns:
        list: Lista de diccionarios, -1 si sale mal la lectura del archivo, -2 si salio mal la fabricacion de la lista de diccionarios
    """
    if leer_archivo_csv(nombre_archivo) != -1:
        lista_insumos = leer_archivo_csv(nombre_archivo)
        insumos = fabricar_lista_diccionarios_insumos(lista_insumos)
        if insumos != -1:
            return insumos
        else:
            return -2
    else:
        return -1  

def filtrar_categoria(lista:list, key:str)-> list | int:
    """Filtra los elementos de un diccionario por clave(key)

    Args:
        lista (list): Lista de diccionarios de insumos\n
        key (str): Clave del diccionario a filtrar

    Returns:
        list | int: Si sale bien la lista filtrada, -1 en caso de lista vacia
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
        dict: Si sale todo bien un diccionario con los items contados, -1 en caso de lista vacia
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

def listar_cantidad_por_marca(lista_insumos:list) -> int:
    """Filtra las marcas, obtiene la cantidad de marcas iguales y muestra en pantalla la marca con su correspondiente cantidad

    Args:
        lista_insumos (list): Lista de insumos a trabajar
        
    Returns:
        int: -1 en caso de una lista vacia, -2 en caso de error en el filtrado, -3 en caso de error en el contado de marcas
    """
    if len(lista_insumos) > 0:
        marcas_insumos = filtrar_categoria(lista_insumos,"marca")
        if not marcas_insumos == -1:
            cantidad_de_marcas = contar_item_por_categoria(marcas_insumos)
            if not cantidad_de_marcas == -1:
                imprimir_dato("\n  MARCA                     |   CANTIDAD\n")  
                mostrar_cantidad_por_categoria(cantidad_de_marcas)
            else:
                return -3
        else:
            return -2
    else:
        return -1


def listar_marca_nombre_precio(lista_insumos:list):
    """Filtra marca - nombre - precio de los insumos y los muestra

    Args:
        lista_insumos (list): Lista de diccionarios de insumos
    """
    marcas_nombres_precios = list(map(lambda ins: [ins["marca"], ins["nombre"], ins["precio"]], lista_insumos))
    imprimir_dato("\n MARCA                        NOMBRE                          PRECIO\n")
    for item in marcas_nombres_precios:
        imprimir_dato(f"{item[0]:25s} {item[1]:35s} {item[2]}")
    
def separar_caracteristicas(lista_insumos:list):
    """Separa un string de caracteristicas en caracteristicas individuales

    Args:
        lista_insumos (list): Lista de diccionarios de insumos
    """
    for insumo in lista_insumos:
        insumo["caracteristicas"] = insumo["caracteristicas"].split("~")

def unir_caracteristicas(lista_insumos:list):
    """Junta las caracteristicas separadas, en un string 

    Args:
        lista_insumos (list): Lista de diccionarios de insumos
    """
    for insumo in lista_insumos:
        insumo["caracteristicas"] = "~".join(insumo["caracteristicas"])


def buscar_coincidencias_caracteristicas(lista_insumos:list, caracteristica_buscar:str) -> list:
    """Busca coincidencias de caracteristicas y las guarda en una lista auxiliar

    Args:
        lista_insumos (list): Lista de diccionarios de insumos\n
        elemento_buscar (str): La caracteristica a buscar

    Returns:
        list: La lista de insumos con las caracteristicas solicitadas
    """
    insumo_con_esas_caracteristicas = []
    
    separar_caracteristicas(lista_insumos)
    
    for insumo in lista_insumos:
        if caracteristica_buscar in insumo["caracteristicas"]:
            insumo_con_esas_caracteristicas.append(insumo)
    
    unir_caracteristicas(lista_insumos)
    
    return insumo_con_esas_caracteristicas

def buscar_insumo_por_característica(lista_insumos:list, caracteristica_buscada:str):
    """Busca coincidencias de caracteristicas y muestra los insumos encontrados con esas caracteristicas, de no encontrar ninguno lo informa en pantalla

    Args:
        lista_insumos (list): Lista de diccionarios de insumos\n
        elemento_buscar (str): La caracteristica a buscar
    """

    insumos_con_esa_caracteristica = buscar_coincidencias_caracteristicas(lista_insumos,caracteristica_buscada)
    if len(insumos_con_esa_caracteristica) > 0:
        mostrar_insumos(insumos_con_esa_caracteristica, formato=False)
    else:
        imprimir_dato("No existe esa caracteristica")
    
def mostrar_insumos_con_una_caracteristica(lista_insumos:list):
    """Imprime en pantalla la lista de insumos con la primer caracteristica solamente

    Args:
        lista_insumos (list): La lista de diccionarios de insumos
    """

    separar_caracteristicas(lista_insumos)
    
    imprimir_dato("\n  ID           NOMBRE                        MARCA                    PRECIO           CARACTERISTICA\n")

    for insumo in lista_insumos:
        imprimir_dato(f"  {insumo['id']:5s} {insumo['nombre']:35s} {insumo['marca']:25s} {insumo['precio']:10} {insumo['caracteristicas'][0]}")

    unir_caracteristicas(lista_insumos)
    

def reemplazar_caracter(lista:list,key:str, caracter_reemplazar:str, caracter_nuevo:str):
    """Reemplaza un caracter por otro en una cadena 

    Args:
        lista (list): Lista de diccionarios de insumos\n
        key (str): Clave del diccionario a buscar el caracter a reemplazar\n
        caracter_quitar (str): Caracter a reemplazar en la cadena\n
        caracter_nuevo (str): Caracter nuevo en la cadena
    """
    for item in lista:
        item[key] = item[key].replace(caracter_reemplazar,caracter_nuevo)


def convertir_str_flotante(lista:list, key:str) -> bool:
    """Convierte un numero decimal que esta en string a tipo float(decimal)

    Args:
        lista (list): Lista de diccionarios de insumos\n
        key (str): Clave del diccionario donde se encuentra el string del numero decimal 

    Returns:
        bool: True si pudo parsear, caso contrario False
    """

    for item in lista:
        try:
            item[key] = float(item[key])
            flag = True
        except:
            flag = False
    
    return flag

def copiar_lista(lista_original:list, lista_nueva:list)->int:
    """Copia los elementos de una lista en una nueva lista

    Args:
        lista_original (list): Lista original de elementos\n
        lista_nueva (list): Lista donde se copiaran los elementos de la lista original

    Returns:
        int: -1 en caso de pasarle una lista vacia
    """

    if len(lista_original) > 0:
        for item in lista_original:
            lista_nueva.append(item)
    else:
        return -1
    
def ordenar_por_doble_criterio(lista:list, key_principal:str, key_secundaria:str)->None:
    """Ordena una lista de diccionarios por doble criterio, key principal en orden ascendente y si coinciden el mismo valor en las keys principales, ordena la key secundaria en orden descendente.

    Args:
        lista (list): Lista de diccionarios a ordenar\n
        key_principal (str): Clave del primer criterio a ordenar\n
        key_secundaria (str): Clave del segundo criterio a ordenar
    """
    tam = len(lista)

    for i in range(tam-1):
        for j in range(i+1, tam):
            if (lista[i][key_principal] > lista[j][key_principal]) or (lista[i][key_principal] == lista[j][key_principal] and lista[i][key_secundaria] < lista[j][key_secundaria]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    
    
def convertir_en_pesos(lista:list):
    """Agrega el signo pesos al precio del insumo

    Args:
        lista (list): Lista de diccionarios de insumos
    """
    for item in lista:
        item["precio"] = f"${item['precio']}"
    
def listar_insumos_ordenados(lista_insumos:list):
    """Ordena una lista de diccionarios por doble criterio (clave), quitandole el signo '$' al precio para poder parsearlo a float, luego de ordenar la lista, se le agrega el signo $ nuevamente e imprime la lista ordenada

    Args:
        lista_insumos (list): La lista de diccionarios con insumos
    """
    reemplazar_caracter(lista_insumos, "precio", "$", "")
    if convertir_str_flotante(lista_insumos,"precio"):
        ordenar_por_doble_criterio(lista_insumos, "marca", "precio")
        convertir_en_pesos(lista_insumos)
        imprimir_dato(" LISTA ORDENADA POR MARCA ASCENDENTE Y MISMA MARCA PRECIO DESCENDENTE")
        mostrar_insumos_con_una_caracteristica(lista_insumos)

def buscar_por_key(lista:list, elemento_buscado:str)->bool:
    """
        Verifica si un item esta o no esta dentro de la lista
    Args:
        lista (list): Lista elementos\n
        elemento_buscado (str): El valor a buscar dentro de la lista

    Returns:
        bool: Devuelve True si encontro coincidencias, False en caso contrario
    """

    flag = False

    for item in lista:
        if item == elemento_buscado:
            flag = True
            break
    
    return flag

def calcular_subtotal(precio:int | float, cantidad:int | float)-> int | float:
    """Calcula el subtotal de un insumo, multiplicando el precio por la cantidad

    Args:
        precio (int | float): Precio del insumo\n
        cantidad (int | float): Cantidad de insumo

    Returns:
        int | float: El subtotal del producto
    """
    subtotal  =  precio * cantidad
    return subtotal

def buscar_insumos_por_key(lista_insumos:list, elemento_buscar:str, key:str)-> list | int:
    """Obtiene una lista filtrada con el diccionario completo de los insumos que coinciden con la busqueda

    Args:
        lista_insumos (list): Lista de diccionarios con los insumos\n
        elemento_buscar (str): El string que quiero filtrar\n
        key (str): campo del diccionario donde realizar la busqueda

    Returns:
        list | int: La lista filtrada con los insumos que cumplen el criterio de busqueda, en caso de pasar una lista vacia -1
    """
    
    if len(lista_insumos) > 0:
        lista_filtrada = list(filter(lambda ins: ins[key] == elemento_buscar, lista_insumos))
        return lista_filtrada
    else:
        return -1

def obtener_dato(diccionario_insumo:dict, key:str)->str:
    """Obtiene el valor de una key en un diccionario

    Args:
        diccionario_insumo (dict): El diccionario de un insumo\n
        key (str): campo(key) del diccionario a obtener el valor

    Returns:
        str: El valor de la clave
    """
    dato = diccionario_insumo[key]

    return dato

def pedir_validar_entero(mensaje:str)-> int | bool:
    """Pide al usuario un string, valida que sea un entero y si lo es, lo parsea, sino tira una excepcion 

    Args:
        mensaje (str): El mensaje a mostrar al usuario

    Returns:
        int | bool: El entero parseado o False en caso de algun error en la conversion 
    """
    
    try:
        entero = int(input(f"\n{mensaje}\n"))
        return entero
    except ValueError:
        print("Error! No ingresaste un entero")
        return False


def mostrar_datos_con_encabezado(lista:list,encabezado:str)->None:
    """Imprimo una lista datos con un encabezado personalizable

    Args:
        lista (list): La lista de datos a imprimir\n
        encabezado (str): Una cadena que representa el encabezado
    """
    print(f"\n  {encabezado}\n")
    for dato in lista:
        print(f"    {dato}")

def quitar_marcas_repetidas_mostrarlos(lista_insumos:list)->list:
    """Filtra todas las marcas, luego quita las repetidas, dejando una de cada una. Muestra el encabezado con todas las marcas. Y ademas devuelve esa lista filtrada

    Args:
        lista_insumos (list): La lista de diccionarios de insumos

    Returns:
        list: La lista de marcas en caso de salir todo bien, -1 en caso de error en el filtrado de marcas
    """
    marcas = filtrar_categoria(lista_insumos, "marca")
    if marcas != -1:
        marcas = set(marcas)
        mostrar_datos_con_encabezado(marcas,"MARCAS DISPONIBLES")
        return marcas
    else:
        return -1


def realizar_compras(lista_insumos:list):
    """Permite realizar compras eligiendo una marca, la id del producto y la cantidad. Calcula el subtotal de cada compra, para finalmente calcular el total. Imprime en pantalla el total de la compra al finalizar. Escribe una factura de compra con la cantidad, el nombre, el subtotal y el total de la compra. 

    Args:
        lista_insumos (list): Lista de diccionarios con los insumos
    """
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

            producto_nombre = obtener_dato(marcas_disponibles[0], "nombre")
            producto_precio = obtener_dato(marcas_disponibles[0], "precio")

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
    """Filtra y devuelve una lista de los insumos que contienen esa cadena dentro de su nombre

    Args:
        lista_insumos (list): Lista de diccionarios de los insumos\n
        nombre_archivo (str): Nombre del archivo con su extension\n
        nombre_filtrar (str): Cadena a buscar dentro del campo(key) nombre
    """
    
    insumos_filtrados_alimento = list(filter(lambda ins: nombre_filtrar in ins["nombre"],lista_insumos))
    escribir_json(nombre_archivo, insumos_filtrados_alimento)

def leer_mostrar_json(nombre_archivo:str):
    """Lee y muestra en pantalla los insumos de un archivo json existente

    Args:
        nombre_archivo (str): El nombre del archivo existente con su extension
    """
    datos = leer_json(nombre_archivo)
    mostrar_insumos(datos, formato= False)

def calcular_aumento(lista_insumos:list, key:str, aumento:float)-> float:
    """Calcula el aumento y lo aplica a la key especificada

    Args:
        lista_insumos (list): Lista de diccionarios con los insumos\n
        key (str): El campo o key a calcular y aplicar el aumento\n
        aumento (float): El aumento a aplicar

    Returns:
        float: Devuelve una lista con los precios con el aumento aplicado
    """
    
    aumentos = list(map(lambda ins: round((ins[key] * aumento) + ins[key], 2),lista_insumos))
    return aumentos

def reemplazar_valores(lista_original:list, lista_reemplazar:list):
    """Reemplaza los valores de la key "precio" de la lista original con los valores que contiene la lista reemplazar

    Args:
        lista_original (list): Lista original de los diccionarios con los insumos\n
        lista_reemplazar (list): Lista secundaria con los precios actualizados
    """
    for i in range(len(lista_original)):
        lista_original[i]["precio"] = lista_reemplazar[i]

def escribir_csv(lista_insumos:list, nombre_archivo:str):
    """Crea un archivo csv a partir de la lista de diccionarios con los insumos

    Args:
        lista_insumos (list): lista de diccionarios con los insumos\n
        nombre_archivo (str): nombre del archivo con su extension csv
    """
    with open(nombre_archivo, "w", encoding='utf-8') as file:
                    
        encabezado = lista_insumos[0].keys()
        
        linea_columna = ",".join(encabezado)
        file.write(linea_columna.upper() + "\n")

        for insumo in lista_insumos:
            linea = insumo.values()
            linea_columna_valores = ','.join(linea)
            file.write(linea_columna_valores + '\n')

def calcular_aumento_aplicar_guardar_archivo(lista_insumos:list, nombre_archivo:str):
    """Quita los caracteres '$' para poder parsear los valores de los precios a float, y poder realizar el calculo del aumento, reemplaza los valores de los precios antiguos con los nuevos, vuelve a poner el signo '$' al precio y escribe el csv con los precios actualizados con el aumento

    Args:
        lista_insumos (list): lista de diccionarios con los insumos\n
        nombre_archivo (str): nombre del archivo con su extension csv
    """
    reemplazar_caracter(lista_insumos,"precio","$","")
    convertir_str_flotante(lista_insumos, "precio")
    aumentos = calcular_aumento(lista_insumos, "precio", 0.084)
    reemplazar_valores(lista_insumos, aumentos)
    convertir_en_pesos(lista_insumos)
    escribir_csv(lista_insumos, nombre_archivo)
    imprimir_dato("Precios actualizados correctamente")