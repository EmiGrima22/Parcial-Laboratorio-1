from funciones_archivos import *
from functools import reduce

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

def mostrar_insumo(insumo:dict, formato = True):
    if formato:
        print(f"\n ID: {insumo['id']}\n NOMBRE: {insumo['nombre']}\n MARCA: {insumo['marca']}\n PRECIO: {insumo['precio']}\n CARACTERISTICAS: {insumo['caracteristicas']}\n")
    else:
        print(f"  {insumo['id']:5s} {insumo['nombre']:35s} {insumo['marca']:25s} {insumo['precio']:10} {insumo['caracteristicas']}")

def mostrar_insumos(lista:list, formato = True)->None:
    if not formato:
        encabezado_insumos()  

    for insumo in lista:
        mostrar_insumo(insumo,formato) 

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

def obtener_insumo_por_tipo(lista_insumos:list, lista_sin_repetidos:list, key_evaluar:str)-> dict:
    
    dic_tipo_nombres_precios = {}

    for item in lista_sin_repetidos:
        for insumo in lista_insumos:
            if insumo[key_evaluar] == item:
                if item not in dic_tipo_nombres_precios:
                    dic_tipo_nombres_precios[item] = []
                     
                dic_tipo_nombres_precios[item].append(f'{insumo["nombre"]:35s} {insumo["precio"]}')
                
    return dic_tipo_nombres_precios

def mostrar_marca_nombre_precio(dic_tipos:dict):
    print("\n MARCA                        NOMBRE                          PRECIO\n")
    for clave,valores in dic_tipos.items():
        for valor in valores:
            print(f"{clave:25s} {valor}")

def listar_insumos_por_marca(lista_insumos:list)->None:

    marcas = quitar_repetidos(filtrar_categoria(lista_insumos,"marca"))
    dic_marcas_nombres_precios = obtener_insumo_por_tipo(lista_insumos, marcas, "marca")
    mostrar_marca_nombre_precio(dic_marcas_nombres_precios)

def buscar_coincidencias_caracteristicas(lista_insumos:list, elemento_buscar:str):
    insumo_con_esas_caracteristicas = []
    
    for insumo in lista_insumos:
        if elemento_buscar in insumo["caracteristicas"]:
            insumo_con_esas_caracteristicas.append(insumo)
    
    return insumo_con_esas_caracteristicas

def buscar_insumo_por_característica(lista_insumos:list, caracteristica_buscada:str):
    insumos_con_esa_caracteristica = buscar_coincidencias_caracteristicas(lista_insumos,caracteristica_buscada)  
    mostrar_insumos(insumos_con_esa_caracteristica, formato=False) 
    
    
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
    
    return flag

def ordenar_por_doble_criterio(lista:list, key_principal:str, key_secundaria:str)->None:
    tam = len(lista)

    for i in range(tam-1):
        for j in range(i+1, tam):
            if (lista[i][key_principal] > lista[j][key_principal]) or (lista[i][key_principal] == lista[j][key_principal] and lista[i][key_secundaria] < lista[j][key_secundaria]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    
def quitar_repetidos(lista:list)->list:

    lista_sin_repetidos = []

    for item in lista:
        if item not in lista_sin_repetidos:
            lista_sin_repetidos.append(item)

    return lista
 
def convertir_en_pesos(lista:list):
    for item in lista:
        item["precio"] = f"${item['precio']}"
    
def listar_insumos_ordenados(lista_insumos):
    reemplazar_caracter(lista_insumos, "precio", "$", "")
    if convertir_str_flotante(lista_insumos,"precio"):
        ordenar_por_doble_criterio(lista_insumos, "marca", "precio")
        convertir_en_pesos(lista_insumos)
        mostrar_insumos(lista_insumos, formato=False)

def buscar_por_key(lista:list, buscado:str):

    flag = False

    for item in lista:
        if item == buscado:
            flag = True
    
    return flag

def calcular_subtotal(operando_a:int | float, operando_b:int | float)-> int | float:
    subtotal  =  operando_a * operando_b
    return subtotal

def buscar_insumos_por_key(lista_insumos, marca_buscar, key):
    
    if len(lista_insumos) > 0:
        lista_filtrada = list(filter(lambda ins: ins[key] == marca_buscar, lista_insumos))
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
    marcas = quitar_repetidos((filtrar_categoria(lista_insumos, "marca")))
    mostrar_dato(marcas,"MARCAS DISPONIBLES")

    return marcas

def imprimir_dato(dato:str)->None:
    print(dato)

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