import sys

class Member:

    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
    
    def descripcion(self):
        print("Name: ", self.name)
        print("Instrument: ", self.instrument)
    
class Guitar(Member): #Herencia

    def __init__(self, model, brand, color, name, instrument):
        super().__init__(name, instrument)
        self.model = model 
        self.brand = brand
        self.color = color
        
        
    def welcome_to_the_band(self):
        print("Hey", self.name, ", welcome to the band. You're going to play the guitar!")

    def play_guitar(self):
            print("Wiririrui")


class Bass(Member): #Herencia

    def __init__(self, model, brand, color, name, instrument):
        super().__init__(name, instrument)
        self.modelo = model
        self.marca = brand
        self.color = color
    
    def welcome_to_the_band(self):
        print("Hey", self.name, ", welcome to the band. You're going to play the bass.")
    
    def play_bass(self):
        print("bumbumbumbaaam")


class Drums(Member): #Herencia
    
    def __init__(self, brand, name, instrument):
        super().__init__(name, instrument)
    
    def welcome_to_the_band(self):
        print("Hey", self.name, ", welcome to the band. You're going to play the drums.")

    def play_drums(self):
        print("TUCUTATUCUTATUCUTATATA")

class Vocals(Member): #Herencia
    def __init__(self, type, name, instrument):
        super().__init__(name, instrument)
        self.type = type
        self.name = name
        self.instrument = instrument
    
    def welcome_to_the_band(self):
        print("Hey", self.name, ", welcome to the band. You're going to be the vocalist.")
    
    def sing(self):

        if self.type == "clean":
            print(self.name, "is singing with", self.type, "vocals.")
        elif self.type == "guturals":
            print(self.name, "is using", self.type, "in the song.")
        else:
            print(self.name, "is trying to sing.")
    

class Studio: #Asociacion

    def __init__(self, name):
        self.name = name

    def band_practice(self):
        print("The band is practicing at ", self.name)

    def record_a_song(self):
        print("The band is recording a new song at ", self.name)

class Employee: #Composicion
    def __init__(self, name):
        self.name = name

    def description(self):
        print(self.name, "works in the studio.")

class Tuner: #Dependencia
    def __init__(self, type, brand):
        self.type = type
        self.brand = brand

    def tune(self):
        print("The guitar is being tunned by a", self.type, "tuner.")


class Collection: #Agregacion
    def __init__(self, name):
        self.name = name
        self.guitars = []

    def add_guitar(self, guitar):
        self.guitars.append(guitar)
    
    def show_guitars(self):
        print("Collection:", self.name)
        for guitar in self.guitars:
            print("Model:", guitar.model, "Brand:", guitar.brand, "Color:", guitar.color)
            
def main():
    name = str(input("Hello, What's your name? "))
    print("Welcome,", name, "Which of the following instruments do you wanna play in our band? ")
    print("[1] Guitar.")
    print("[2] Bass.")
    print("[3] Drums.")
    print("[4] Vocals.")
    print("[5] Exit.")
    instrument = int(input("")) 

    #Instancias
    default_guitar1 = Guitar("Les Paul", "Gibson", "Orange", name, instrument)
    default_guitar2 = Guitar("Superstrat", "Jackson", "Brown", name, instrument)
    default_vocals1 = Vocals("clean", name, instrument)
    default_vocals2 = Vocals("guturals", name, instrument)
    default_tuner1 = Tuner("Clip", "Alpina")
    default_tuner2 = Tuner("Pedal", "Alpina")
    default_drums1 = Drums("Mapex", name, instrument)
    default_drums2 = Drums("Yamaha", name, instrument)
    default_bass1 = Bass("Hurricane", "fender", "brown", name, instrument)
    default_bass2 = Bass("Stormbird", "fender", "cyan", name, instrument)
    default_studio1 = Studio("Pastorius")         
    default_studio2 = Studio("Yourself")
    collection = Collection("Your guitar Collection")
    collection1 = Collection("Your bass Collection")
    employee1 = Employee("Pablo")
    employee2 = Employee("Pepe")

    match instrument:

        case 1:
            default_guitar1.welcome_to_the_band()
            while True:
                try:
                    collection.add_guitar(default_guitar1)
                    collection.add_guitar(default_guitar2)
                    collection.show_guitars()
                    tune = int(input("First, your guitar it's probably out of tune. Press [1] to tune your guitar or [2] to exit "))
                    if tune == 1:
                        
                        default_tuner1.tune()
                        employee1.description()
                        numero = int(tune)
                        studio = str(input("Now, what do you want to do? Press [x] to practice with the band, [z] to record a song with the band  or [y] to exit."))
                        
                        if studio == "x":
                            default_studio1.band_practice()
                        elif studio == "z":
                            default_studio1.record_a_song()
                        elif studio == "y":
                            main()
                        return numero
                    
                    if tune == 2:
                        main()    
                    else:
                        print("Introuce a valid number ")
                    break

                except ValueError:
                    pass               
        case 2:
            default_bass1.welcome_to_the_band()

            play_bass = int(input("Press [1] to play the bass or [2] to exit. "))
            if play_bass == 1:
                default_bass1.play_bass()
                numero = int(play_bass)
                return numero
            else:
                    print("Introuce a valid number ")
        case 3:
            default_drums1.welcome_to_the_band()

            play_drums= int(input("Press [1] to play the drums or [2] to exit. "))
            if play_drums == 1:
                default_drums1.play_drums()
                numero = int(play_drums)
                return numero
            else:
                    print("Introuce a valid number ")
        case 4:
            default_vocals1.welcome_to_the_band()

            while True:
                sing = int(input("Press [1] to sing or [2] to exit. "))
                if sing == 1:
                    default_vocals1.sing()
                    numero = int(sing)
                    return numero
                else:
                    print("Introuce a valid number ")
        case 5:
            sys.exit()
        case _:
            print("Introduce a valid number ")
            
            
        
main()