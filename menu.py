import os
from validaciones import *
from funciones_insumos import *
from functools import reduce

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
                buscar_insumo_por_característica(lista_insumos, caracteristica_buscar)
            case 5:
                listar_insumos_ordenados(lista_insumos)
            case 6:
                reemplazar_caracter(lista_insumos,"precio","$","")
                convertir_str_flotante(lista_insumos, "precio")
                total_compra = []
                registro_compra = []

                while True:
                    marca_buscar = input("Ingrese marca a buscar\n")
                    marcas_disponibles = list(filter(lambda ins:ins["marca"] == marca_buscar,lista_insumos))

                    if len(marcas_disponibles) > 0:
                        while True:
                            while True:
                                mostrar_insumos(marcas_disponibles)
                                producto = input("\n¿Ingrese el ID del producto que desee?\n")

                                if buscar_producto_esta(marcas_disponibles, "id", producto):
                                    producto_nombre = marcas_disponibles["nombre"]
                                    producto_precio = marcas_disponibles["precio"]
                                    break
                                else:
                                    print("El producto no se encontro")

                            try:
                                while True:
                                    cantidad = int(input("\n¿Cuantos queres?\n"))
                                    if cantidad > 0:
                                        subtotal = cantidad * producto_precio
                                        break
                            except ValueError:
                                print("Error! No ingresaste un entero")
                            
                            total_compra.append(subtotal)
                            registro_compra.append(f"Cantidad: {cantidad} - Producto: {producto_nombre} - Subtotal:    ${subtotal}")
                            while True:
                                continuar = input("¿Quiere continuar comprando? s/n\n").lower()
                                if continuar == "s" or continuar == "n": 
                                    break

                            if continuar == "s" or continuar == "n":
                                break

                        if continuar == "n":
                                break
                    else:
                        print("No existe ese producto")
                total_final = reduce(lambda act, ant: ant + act, total_compra)
                registro_compra.append(f"                                             - Total: ${total_final}")

                print(f"El total de la compra fue {total_final}")
                
                with open("Factura_compra.txt","w") as archivo:
                    archivo.writelines("\n".join(registro_compra))
            case 7:
                pass
            case 8:
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