# bucle for

frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Fruta:", fruta)

# BREAK
animales = ("perro", "gato", "conejo", "hamster", "pez", "loro", "tortuga", "serpiente", "iguana", "cobaya")
for indice, animal in enumerate(animales):
    print("Animal:", animal)
    if animal == "pez":
        print("¡Encontré un pez, deteniendo el bucle!")
        break

# CONTINUE
animales = ("perro", "gato", "conejo", "hamster", "pez", "loro", "tortuga", "serpiente", "iguana", "cobaya")
for indice, animal in enumerate(animales):
    if animal == "pez":
        print("Saltando el pez...")
        continue
    print("Animal:", animal)

# comprension de listas

animales = ("perro", "gato", "conejo", "hamster", "pez", "loro", "tortuga", "serpiente", "iguana", "cobaya")
animales_mayusculas = [animal.upper() for animal in animales]
print("Animales en mayúsculas:", animales_mayusculas)


animales = ("perro", "gato", "conejo", "hamster", "pez", "loro", "tortuga", "serpiente", "iguana", "cobaya")
animales_con_s = [animal for animal in animales if 's' in animal]
print("Animales con 's':", animales_con_s)

pares = [num for num in [1,2,3,4,5,6,7,8,9,10] if num % 2 == 0]

pares = [num for num in range(20) if num % 2 == 0]