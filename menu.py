import os
from validaciones import *
from funciones_insumos import *


def imprimir_menu_insumos()->None:
    """Imprime el menu de opciones con encabezado
    """
    print("####             ADMINISTRACION DE INSUMOS             ####\n")
    print("-----------------------------------------------------------\n")
    print(" 1 --> Cargar datos desde archivo\n 2 --> Listar cantidad por marca\n 3 --> Listar insumos por marca\n 4 --> Buscar insumo por característica\n 5 --> Listar insumos ordenados\n 6 --> Realizar compras\n 7 --> Guardar en formato JSON\n 8 --> Leer desde formato JSON\n 9 --> Actualizar precios\n10 --> Salir del programa\n\n")
    
def insumos_menu_principal()->int:
    """Muestra el menu, pide una opcion y la parsea a entero

    Returns:
        int: La opcion parseada a int(entero) o -1 si sale mal
    """
    imprimir_menu_insumos()
    opcion = input("Ingrese una opcion\n")
    if validar_entero(opcion):
        opcion = int(opcion)
        return opcion
    else:
        return -1
    
def insumos_app() -> None:
    """Muestra el menu principal con toda la funcionalidad del programa
    """
    
    flag_cargar_csv = False
    flag_json = False

    while True:
        os.system("cls")
        while True:
            opcion = insumos_menu_principal()
            if opcion >= 1 and opcion <= 10:
                break
            else:
                imprimir_dato("Opcion incorrecta")
            
        match opcion:
            case 1:
                if not flag_cargar_csv:
                    if cargar_datos_desde_archivo("insumos.csv") != -1:
                        lista_insumos = cargar_datos_desde_archivo("insumos.csv")
                        flag_cargar_csv = True
                        imprimir_dato("Insumos csv leido correctamente")
                else:
                    imprimir_dato("El archivo csv ya fue cargado") 
            case 2:
                if flag_cargar_csv:
                    listar_cantidad_por_marca(lista_insumos)
                else:
                    imprimir_dato("Primero debe leer el archivo csv")
            case 3:
                if flag_cargar_csv:
                    listar_marca_nombre_precio(lista_insumos)
                else:
                    imprimir_dato("Primero debe leer el archivo csv")
            case 4:
                if flag_cargar_csv:
                    caracteristica_buscada = input("Ingrese caracteristica a buscar\n").capitalize()

                    if not validar_string_vacio(caracteristica_buscada) and len(caracteristica_buscada) > 0:
                        buscar_insumo_por_característica(lista_insumos, caracteristica_buscada)
                    else:
                        imprimir_dato("No debe ser una cadena vacia")
                else:
                    imprimir_dato("Primero debe leer el archivo csv")
            case 5:
                if flag_cargar_csv:
                    lista_nueva_insumos_ordenar = []
                    copiar_lista(lista_insumos, lista_nueva_insumos_ordenar)
                    listar_insumos_ordenados(lista_nueva_insumos_ordenar)
                else:
                    imprimir_dato("Primero debe leer el archivo csv")
            case 6:
                if flag_cargar_csv:
                    realizar_compras(lista_insumos)  
                else:
                    imprimir_dato("Primero debe leer el archivo csv")
            case 7:
                if flag_cargar_csv:
                    nombre_archivo = "insumos_alimentos.json"
                    filtrar_escribir_json(lista_insumos, nombre_archivo, "Alimento")
                    flag_json = True
                    imprimir_dato("JSON creado correctamente")
                else:
                    imprimir_dato("Primero debe leer el archivo csv")
            case 8:
                if flag_json:
                    leer_mostrar_json(nombre_archivo)
                else:
                    imprimir_dato("No existe archivo json para leer")
            case 9:
                if flag_cargar_csv:
                    calcular_aumento_aplicar_guardar_archivo(lista_insumos, "insumos.csv")
                else:
                    imprimir_dato("Primero debe leer el archivo csv")
            case 10:
                while True:
                    confirmacion = input("¿Seguro desea salir? s/n\n").lower()
                    if confirmacion == "s" or confirmacion == "n": 
                        break
                if confirmacion == "s":
                    break
        os.system("pause")