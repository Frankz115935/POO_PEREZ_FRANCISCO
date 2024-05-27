promedio1 = float(input("Ingresa el primer promedio: "))
promedio2 = float(input("Ingresa el segundo promedio: "))
promedio3 = float(input("Ingresa el tercero promedio: "))

mayor = promedio1

if promedio2 > mayor:
    mayor = promedio2
if promedio3 > mayor:
    mayor = promedio3

print("El promedio mayor es: ", mayor)

