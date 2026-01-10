"""
Defincion de una función

def nombre_de_la_funcion(parametro1, parametro2, ...):
    bloque de instrucciones

    return valor_de_retorno #opcional

"""

#Ejemplo de funcion, la mas basica
def saludar():
    print("Hola, bienvenido a Python!")


saludar()  #Llamada a la funcion

#Funcion con parametros
def saludar_a(nombre):
    print(f"Hola, {nombre}, bienvenido a Python!")

saludar_a("Carlos")  #Llamada a la funcion con argumento
saludar_a("Ana")     #Otra llamada a la funcion con diferente argumento
saludar_a("Luis")    #Otra llamada a la funcion con diferente argumento

#Funcion con varios parametros
def sumar(a, b):
    resultado = a + b
    return resultado

suma1 = sumar(5, 3)  #Llamada a la funcion con argumentos
print(f"La suma de 5 y 3 es: {suma1}")

# Documentar la funcion con docstring
def restar(a, b):
    """
    Resta dos numeros y devuelve el resultado.

    Parametros:
    a (int, float): El minuendo.
    b (int, float): El sustraendo.

    Retorna:
    int, float: La diferencia entre a y b.
    """
    return a - b

diferencia = restar(10, 4)
print(restar.__doc__)  #Imprime la documentacion de la funcion
print(f"La resta de 10 y 4 es: {diferencia}")

# Funcion con valor por defecto
def multiplicar(a, b=2):
    return a * b

print(f"Multiplicar 5 por 2 (valor por defecto): {multiplicar(5)}")
print(f"Multiplicar 5 por 3: {multiplicar(5, 3)}")

# Funcion con argumentos por posicion
def describir_persona(nombre, edad, ciudad):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")

# Parametros por posicion   
describir_persona("Laura", 28, "Madrid")

# Parametros por nombre y clave
describir_persona(ciudad="Barcelona", nombre="Miguel", edad=35)
# Mezcla de ambos
describir_persona("Sofia", ciudad="Valencia", edad=22)

# Funcion con argumentod de longitud de variable (*args)
def sumar_todos(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(f"La suma de 1, 2, 3 es: {sumar_todos(1, 2, 3)}")
print(f"La suma de 5, 10, 15, 20 es: {sumar_todos(5, 10, 15, 20)}")

# Funcion con argumentos de longitud variable por clave (**kwargs)
def mostrar_info(**info):
    for clave, valor in info.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=30, ciudad="Sevilla")
mostrar_info(marca="Toyota", modelo="Corolla", año=2020)
mostrar_info(pais="España", capital="Madrid", poblacion=47000000)