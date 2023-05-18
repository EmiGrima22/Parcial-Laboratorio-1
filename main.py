from menu import *

with open("insumos.csv","r", encoding='utf-8') as file:
    
    lista = []
    lista_sin_elementos_vacios = []
    lista_insumos = []
    
    for line in file:
        line = line.replace("\n","")
        line = line.split(",")
        lista.append(line)

    for elemento in lista:
        if elemento != [""]:
            lista_sin_elementos_vacios.append(elemento)
            
    claves = lista_sin_elementos_vacios.pop(0)
    
    for elemento in lista_sin_elementos_vacios:
        insumo = {}
        insumo[claves[0]] = elemento[0]
        insumo[claves[1]] = elemento[1]
        insumo[claves[2]] = elemento[2]
        insumo[claves[3]] = elemento[3]
        insumo[claves[4]] = elemento[4]
        lista_insumos.append(insumo)
    
def mostrar_insumo(insumo:dict):
    print(f" {insumo['ID']:5s} {insumo['NOMBRE']:35s} {insumo['MARCA']:25s} {insumo['PRECIO']:10s} {insumo['CARACTERISTICAS']}")

def mostrar_insumos(lista:list):
    for insumo in lista:
        mostrar_insumo(insumo)


mostrar_insumos(lista_insumos)

""" 
2. Listar cantidad por marca: Muestra todas las marcas y la cantidad de insumos correspondientes a cada una.
"""

marcas_insumos = list(map(lambda insumo: insumo['MARCA'] ,lista_insumos))

marca_cantidad = {}
for marca in marcas_insumos:
    
    if marca in marca_cantidad:
        marca_cantidad[marca] += 1
    else:
        marca_cantidad[marca] = 1

# for marca, cantidad in marca_cantidad.items():
#     print(f"{marca:25} {cantidad}")

"""
3. Listar insumos por marca: Muestra, para cada marca, el nombre y precio de los insumos correspondientes.
"""

lista_precios_nombre = []

for insumo in lista_insumos:
    for marca in marcas_insumos:
        if insumo["MARCA"] == marca:
            nombre_precio = (f"Marca: {marca:25s} | Nombre: {insumo['NOMBRE']:35s} | Precio: {insumo['PRECIO']}")
            lista_precios_nombre.append(nombre_precio)

# for elemento in lista_precios_nombre:
#     print(elemento)
        