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

#ASOCIACION
class Lutier:
    def __init__(self, nombre):
        self.nombre = nombre
        self.guitarras_reparadas = []

    def reparar_guitarra(self,guitarra):
        if guitarra not in self.guitarras_reparadas:
            self.guitarras_reparadas.append(guitarra) 
            print(self.nombre, "está reparando la guitarra ", guitarra.marca)
        else:
            print(self.nombre, "ya reparo la guitarra ", guitarra.marca)

    def lista_de_guitarras_reparadas(self):
        print(self.nombre, "ha reparado a las siguientes guitarras:")
        for guitarra in self.lista_de_guitarras_reparadas:
            print(guitarra.marca)

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

#COMPOSICION
class Cuerda:
    
    def __init__(self, material, marca):
        self.material = material
        self.marca = marca

    def descripcion(self):
        print("Estas cuerdas son de la marca ",self.marca, "y son de material", self.material)

#HERENCIA
class Guitarra_electrica(Guitarra):

    def __init__(self, tipo, color, marca, tipo_de_pastillas):
        super().__init__(tipo, color, marca)
        self.tipo_de_pastillas = tipo_de_pastillas
        
    
    def descripcion(self):
        super().descripcion()
        print("Soy una guitarra con pastillas ", self.tipo_de_pastillas)

    
    def solo(self):
        print(" el dueno de la guitarra ",", esta tocando un solo con pastillas", self.tipo_de_pastillas)

#DEPENDENCIA
class Afinador:

    def __init__(self, tipo):
        self.tipo = tipo 
    
    def descripcion(self):
        print("Afinador de tipo ", self.tipo )

#OBJETOS
guitarra1 = Guitarra("Les Paul", "Naranja", "Gibson")
guitarra2 = Guitarra("Superstrat","Cafe","Jackson")
Lutier1 = Lutier("Gabriel")
Lutier2 = Lutier("Paolo")
dueno1 = Dueno("Lolito")
dueno2 = Dueno("Alan")
Cuerdas1 = Cuerda("Acero","Ernie ball")
Cuerdas2 = Cuerda("Nylon","Ernie ball")
Electrica1 = Guitarra_electrica("Les paul", "Rojo", "Gibson","Single-coil")
Electrica2 = Guitarra_electrica("Stratocaser", "Negra", "fender", "Single-coil")
Afinador1 = Afinador("De clip")
Afinador2 = Afinador("De pedal")

#METODOS DE LOS OBJETOS
guitarra1.descripcion()
guitarra1.afinar()
guitarra1.tocar()
Lutier1.reparar_guitarra(guitarra1)
dueno1.anadir_guitarra(guitarra1)
dueno2.anadir_guitarra(guitarra2)
dueno1.anadir_guitarra(Electrica1)
dueno1.listar_guitarras()
dueno1.tocar_guitarras()
