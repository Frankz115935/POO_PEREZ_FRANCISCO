numero = float(input("Inserte un numero "))

if numero <= -0.1:
    print("El numero es negativo")
elif numero >= 0.1:
    print("El numero es positivo")
elif numero == 0:
    print("El numero es 0")
else:
    print("Inserte un numero valido")