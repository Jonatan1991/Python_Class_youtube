#sentencias condicionales if, elif, else
age = 20

if age <= 18:
    print("Eres menor de edad.")
elif age <= 65:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")


# condiciones multiples
edad = 25
carnet_conducir = True

if edad >= 80 and carnet_conducir:
    print("Excelente desempeño.")
else:
    print("Condiciones no cumplidas.")
