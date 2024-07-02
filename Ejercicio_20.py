conjunto1 = {1, 5, 47}
conjunto2 = {141, 24, 8, 2}
conjunto3 = {25, 13, 18}

union = conjunto1.union(conjunto2, conjunto3)

print("Union de los conjuntos: ",union)

pares = set()

for i in union:
    if i % 2 == 0:
        pares.add(i)

print("Numeros pares en la union: ", pares)