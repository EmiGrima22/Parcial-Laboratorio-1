import os
import json
from validaciones import *
from funciones_insumos import *


def imprimir_menu_insumos()->None:
    """Imprime el menu de opciones
    """
    print("####             ADMINISTRACION DE INSUMOS             ####\n")
    print("-----------------------------------------------------------\n")
    print(" 1 --> Cargar datos desde archivo\n 2 --> Listar cantidad por marca\n 3 --> Listar insumos por marca\n 4 --> Buscar insumo por característica\n 5 --> Listar insumos ordenados\n 6 --> Realizar compras\n 7 --> Guardar en formato JSON\n 8 --> Leer desde formato JSON\n 9 --> Actualizar precios\n10 --> Salir del programa\n\n")
    
def insumos_menu_principal()->int:
    """Muestra el menu, pide una opcion y la castea a entero

    Returns:
        int: La opcion casteada a int(entero) o -1 si algo sale mal
    """
    imprimir_menu_insumos()
    opcion = input("Ingrese una opcion\n")
    if validar_entero(opcion):
        opcion = int(opcion)
        return opcion
    else:
        return -1
    
def insumos_app() -> None:
    
    
    while True:
        os.system("cls")
        while True:
            opcion = insumos_menu_principal()
            if opcion >= 1 and opcion <= 10:
                break
            else:
                print("Opcion incorrecta")
            
        match opcion:
            case 1:
                lista_insumos = cargar_datos_desde_archivo("insumos.csv") 
            case 2:
                listar_cantidad_por_marca(lista_insumos)
            case 3:
                listar_insumos_por_marca(lista_insumos)
            case 4:
                caracteristica_buscar = input("Ingrese caracteristica a buscar\n").capitalize()
                if not validar_string_vacio(caracteristica_buscar) and len(caracteristica_buscar) > 0:
                    buscar_insumo_por_característica(lista_insumos, caracteristica_buscar)
                else:
                    print("No debe ser una cadena vacia")
            case 5:
                listar_insumos_ordenados(lista_insumos)
            case 6:
                realizar_compras(lista_insumos)  
            case 7:
                
                productos_filtrados = []
                
                insumos_filtrados_alimento = list(filter(lambda ins: "Alimento" in ins["nombre"],lista_insumos))

                # for insumo in lista_insumos:
                #     if "Alimento" in insumo["nombre"]:
                #         productos_filtrados.append(insumo)

                with open("insumos_alimento.json", "w", encoding='utf-8') as archivo:
                    json.dump(insumos_filtrados_alimento, archivo, indent=4, separators=(", ", " : "), ensure_ascii=False)

            case 8:
                with open("insumos_alimento.json", "w") as archivo:
                    pass
            case 9:
                pass
            case 10:
                while True:
                    confirmacion = input("¿Seguro desea salir? s/n\n").lower()
                    if confirmacion == "s" or confirmacion == "n": 
                        break
                if confirmacion == "s":
                    break
        os.system("pause")