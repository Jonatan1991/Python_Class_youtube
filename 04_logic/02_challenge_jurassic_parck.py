"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. 
Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los 
huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).

"""

def count_carnivorous_eggs(egg_list) -> int:
    """
    Esta funcion recibe una lista de números enteros que representan la cantidad de huevos puestos por dinosaurios.
    Devuelve la suma total de los huevos puestos por dinosaurios carnívoros (n
    """
    total_eggs = 0

    for count in egg_list:
        if count % 2 == 0:  # Verifica si el número es par
            total_eggs += count

    return total_eggs

# Ejemplo de uso
egg_list = [3, 4, 2, 7, 8, 10, 5]
print(count_carnivorous_eggs(egg_list))  # Salida esperada: 24 (4 + 2 + 8 + 10)