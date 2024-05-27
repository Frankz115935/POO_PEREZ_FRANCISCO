import sys
Terminar = str(input("Si desea empezar el programa teclea 'si', de lo contrario teclea 'no'. "))

while Terminar == "si":
    TipoTemp = int(input("Ingrese el numero de la conversion que desee realizar    " 
                     "1. Celcius a Fahrenheit. "
                     "2. Fahrenheit a Celcius. "
                     "3. Salir. "))

    if TipoTemp == 1:
        celsius =  float(input("Ingresa los grados que deseas convertir a Fahrenheit: "))
        Celsius_Fahrenheit = celsius * (9/5) + 32
        print("El resultado es ", Celsius_Fahrenheit, "°F" )
    elif TipoTemp == 2:
        Fahrenheit = float(input("Ingresa los grados que deseas convertir a Celsius: "))
        Fahrenheit_Celsius =  (Fahrenheit - 32) * (5/9)
        print("El resultado es ", Fahrenheit_Celsius,"°C" )
    elif TipoTemp == 3:
        sys.exit()
    else:
        print("Ingrese un numero valido")