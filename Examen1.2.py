import math

def main():
    print("Que figura que deseas calcular")
    print("1. Circulo")
    print("2. Triangulo")
    print("3. Rectangulo")
    print("4. Salir")

    opcion = int(input("Introduce el numero de opcion "))

    if opcion == 1:
        Area_Circulo()
    elif opcion == 2:
        Area_Triangulo()
    elif opcion == 3:
        Area_rectangulo()
    elif opcion == 4:
        exit() 
    else:
        print("Introduzca una opcion valida")


def Area_Triangulo():
    print("Dime la altura del triangulo")
    altura = float(input())
    print("Dime la base del triangulo")
    base = float(input())
    print("El area del circulo es:")
    print(base * altura)
    Area_Triangulo()

def Area_Circulo():
    print("Dame el diametro del circulo")   
    diametro = float(input())
    radio = diametro/2
    area = math.pi*(radio *radio)
    print("El area es:", area)
    Area_Circulo()

def Area_rectangulo():

    print("Dime la base del rectangulo:")
    base = float(input())
    print("Dime la altura del rectangulo:")
    altura = float(input())
    print("El area del rectangulo es:")
    resultado = base * altura
    print(resultado)
    Area_rectangulo()


main()
  

    