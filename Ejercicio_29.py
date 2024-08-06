import sys

def abstraccion():
     print("La abstracción es el proceso de identificar y destacar las características esenciales de un objeto, mientras se omiten los detalles innecesarios. Se enfoca en la idea de simplificar sistemas complejos mediante la modelización de las partes importantes, ocultando las complejidades subyacentes.")

def encapsulamiento():
     print("Es el proceso de almacenar en una misma sección los elementos de una abstracción que constituyen su estructura y su comportamiento; sirve para separar el interfaz contractual de una abstracción y su implantación.")

def herencia():
     print("Herencia es un concepto de la programación orientada a objetos. El cual es un mecanismo que permite derivar una clase a otra clase. En otras palabras, tendremos unas clases que serán hijos, y otras clases que serán padres.")

def polimorfismo():
     print("El polimorfismo es una relajación del sistema de tipos, de tal manera que una referencia a una clase (atributo, parámetro o declaración local o elemento de un vector) acepta direcciones de objetos de dicha clase y de sus clases derivadas (hijas, nietas, ...).")

def main():
     
    print("1. Abstraccion")
    print("2. Encapsulamiento")
    print("3. Herencia")
    print("4. Polimorfismo")
    print("5. Salir")

    opcion = int(input(("Eliga una opcion: ")))

    match opcion:
         
        case 1:
            abstraccion()
        case 2:
              encapsulamiento()
        case 3:
            herencia()
        case 4:
            polimorfismo()
        case 5:
            sys.exit()
        case _:
            print("Introduzca una opcion valida.")
        
main()
