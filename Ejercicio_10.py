detener = "n"
n = str(input("Para comenzar el programa presione cualquier tecla, si desea deternerlo pulse la tecla n "))
while n != detener:
    Num1 = float(input("Dame el primer numero "))
    Num2 = float(input("Dame el segundo numero "))
    suma = (Num1 + Num2)
    print(suma)
    detener = "n"
    n = str(input("Para continuar el programa presione cualquier tecla, si desea deternerlo pulse la tecla n "))

