def main():    
        print("Introduzca el numero de la operacion que desee realizar.")
        print("[1] para suma.")
        print("[2] para resta.")
        print("[3] para multiplicacion.")
        print("[4] para division.")

        opcion = int(input())

        match opcion:
            case 1:
                sumar()
            case 2:
                restar()
            case 3:
                multiplicar()
            case 4:
                dividir()
            case _:
                print("Introduzca un numero valido")
        

        
def sumar():
    numero1 = float(input("Ingresa el primer numero "))
    numero2 = float(input("Ingresa el segundo numero "))
    suma = numero1 + numero2
    print("El resutado de la suma es: ", suma)
    
def restar():
    numero1 = float(input("Ingresa el primer numero "))
    numero2 = float(input("Ingresa el segundo numero "))
    resta = numero1 - numero2
    print("El resutado de la resta es: ", resta)

def multiplicar():
    numero1 = float(input("Ingresa el primer numero "))
    numero2 = float(input("Ingresa el segundo numero "))
    multiplicacion = numero1 * numero2
    print("El resutado de la multiplicacion es: ", multiplicacion)

def dividir():
    numero1 = float(input("Ingresa el primer numero "))
    numero2 = float(input("Ingresa el segundo numero "))
    division = numero1 / numero2
    print("El resutado de la division es: ", division)

main()