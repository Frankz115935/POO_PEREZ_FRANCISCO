Numero1 = float(input("Dame el primer numero "))
Numero2 = float(input("Dame el segundo numero "))

print("Estos son los numeros ingresados: ",Numero1,Numero2)

if Numero1 == Numero2:
    print("Los numeros ingresados son iguales ")
else:
    if Numero1 > Numero2:
        print("El primer numero es mayor al segundo ")
    if Numero1 < Numero2:
        print("El primer numero es menor que el segundo")