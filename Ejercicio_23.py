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


# OBJETOS
guitarra1 = Guitarra("Les Paul", "Naranja", "Gibson")
guitarra2 = Guitarra("Superstrat","Cafe","Jackson")

# METODOS
guitarra1.descripcion()
guitarra1.afinar()
guitarra1.tocar()
