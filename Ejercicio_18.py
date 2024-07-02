diccionario = {
    "cheetos": 18,
    "huevo": 5,
    "leche": 35,
    "coca-cola": 18,
}

print(diccionario)

descuento = .15

print("El descuento que se aplicara a los productos es de: ", "15%")

print("////////////////////////////////////////////////////////////")

for clave, valor in diccionario.items():
    operacion = valor * descuento
    print("El precio con descuento del producto ", clave, " es de: ", "$", valor - operacion)
