PesoPaquete = float(input("Dime el peso en kg "))

if PesoPaquete <= 1:
    print("La tarifa es igual a $50 ")
elif PesoPaquete <= 5:
    print("La tarifa es igual a $100 ")
elif PesoPaquete <= 10:
    print("La tarifa es igual a $200 ")
elif PesoPaquete >= 10:
    print("La tarifa es igual a $500 ")
