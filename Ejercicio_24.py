class Guitarra:

    def __init__(self, tipo, color, marca):
        self.tipo = tipo
        self.color = color
        self.marca = marca
    
    def descripcion(self):
        print("Soy una guitarra de tipo ", self.tipo,", de color ", self.color,"y de la marca ", self.marca)
    
    def afinar(self):
        print("afinando...")

    def tocar(self):
        print("wiruriruiu")

#AGREGACION
class Dueno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.guitarras = []
        
    def anadir_guitarra(self, guitarra):
        self.guitarras.append(guitarra)
        print(guitarra.marca, "añadido a la lista de guitarras")

    def listar_guitarras(self):
        print(self.nombre, "tiene las siguientes guitarras: ")
        for guitarra in self.guitarras:
            print(guitarra.marca)
    
    def tocar_guitarras(self):
        print(self.nombre, "está tocando guitarra: ")
        for guitarra in self.guitarras:
            guitarra.tocar()

# OBJETOS
guitarra1 = Guitarra("Les Paul", "Naranja", "Gibson")
guitarra2 = Guitarra("Superstrat","Cafe","Jackson")
dueno1 = Dueno("fran")

# METODOS
dueno1.anadir_guitarra(guitarra1)
dueno1.anadir_guitarra(guitarra2)
dueno1.listar_guitarras()
dueno1.tocar_guitarras()