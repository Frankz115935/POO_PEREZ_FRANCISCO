Edades = [1,3,32,5,5,24,90,63,18,13]
Mayores_de_edad = []
Menores_de_edad = []

for i in Edades:
    if i >= 18:
        Mayores_de_edad.insert(i,i)
    else:
        Menores_de_edad.insert(i,i)

print("Mayores de Edad ", Mayores_de_edad)
print("Menores de Edad ", Menores_de_edad)
