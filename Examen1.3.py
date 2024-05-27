Edades = [6,18,56,34,22,9,11,13,77,45,21,8]
Infancia = []
Adolescentes = []
Jovenes = []
Adultos = []
basura = []


for i in Edades:
    if i >= 6:
        Infancia.insert(i,i)
    elif i :
        basura.insert(i,i)
        
for i in Edades:
    if i >= 12:
        Adolescentes.insert(i,i)
    else:
        basura.insert(i,i)
    
for i in Edades:
    if i >= 18:
        Jovenes.insert(i,i)
    elif i >= 27:
        basura.insert(i,i)
for i in Edades:
    if i >= 27:
        Adultos.insert(i,i)
    elif i < 27:
        basura.insert(i,i)
        

print("Infantes ", Infancia)
print("Adolescentes ", Adolescentes)
print("Jovenes ", Jovenes)
print("Adultos ", Adultos)
