# Bucle while
# bucle con una simple condicion

contador = 0
while contador < 5:
    print("Contador es:", contador)
    contador += 1  # Incrementar el contador para evitar un bucle infinito


while True:
    print("Este bucle es infinito. Presiona Ctrl+C para detenerlo. Pero lo he detenido con break.")
    break
    

contador = 0
while True:
    print("Contador es:", contador)
    contador += 1
    if contador >= 5:
        print("Contador ha alcanzado el valor de 5, saliendo del bucle.")
        break

# bucle con continue
numero = 0
while numero < 10:
    numero += 1
    if numero % 2 == 0:
        continue  # Saltar el resto del código en este ciclo si el número es par
    print("Número impar:", numero)

# bucle con else
contador = 0
while contador < 5:
    print("Contador es:", contador)
    contador += 1
else:
    print("El bucle ha terminado normalmente, contador llegó a", contador)


numero = -1
while numero < 0:
    try:
        numero = int(input("Introduce un número positivo: "))
        if numero < 0:
          print("Número negativo, intenta de nuevo.")
    except ValueError:
        print("Entrada no válida, intenta de nuevo.")

print("¡Gracias! Has introducido el número positivo:", numero)