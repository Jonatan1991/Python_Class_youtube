nombre = input("¿Cuál es tu nombre? ")
print("Hola, " + nombre + "!")

age = int(input("¿Cuántos años tienes? "))
print(f"Tienes {age} años.")


print("Obtener multiples valores a la vez")

country, city = input("Ingresa tu país y ciudad separados por una coma: ").split(",")
print(f"País: {country.strip()}, Ciudad: {city.strip()}")