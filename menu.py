import os
from validaciones import *

def imprimir_menu_insumos()->None:
    """Imprime el menu de opciones
    """
    print("####             ADMINISTRACION DE INSUMOS             ####\n")
    print("-----------------------------------------------------------\n")
    print(" 1 --> Cargar datos desde archivo\n 2 --> Listar cantidad por marca\n 3 --> Listar insumos ordenados\n 4 --> Realizar compras\n 5 --> Guardar en formato JSON\n 6 --> Leer desde formato JSON\n 7 --> Actualizar precios\n 8 --> Salir del programa\n\n")
    
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
    
def insumos_app(lista_insumos:list) -> None:
    
    if len(lista_insumos) > 0:
        while True:
            os.system("cls")
            while True:
                opcion = insumos_menu_principal()
                if opcion >= 1 and opcion <= 8:
                    break
                else:
                    print("Opcion incorrecta")
                
            match opcion:
                case 1:
                   pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass
                case 8:
                    while True:
                        confirmacion = input("¿Seguro desea salir? s/n\n").lower()
                        if confirmacion == "s" or confirmacion == "n": 
                            break
                    if confirmacion == "s":
                        break
            os.system("pause")
    else:
        print("Error! Lista vacia")