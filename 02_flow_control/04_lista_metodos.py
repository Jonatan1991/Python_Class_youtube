# metodos con listas
lista_numeros = [1, 2, 3, 4, 5]
print("Lista original:", lista_numeros)

# agregar un elemento al final
lista_numeros.append(6)
print("Después de append(6):", lista_numeros)

# insertar un elemento en una posición específica
lista_numeros.insert(2, 2.5)
print("Después de insert(2, 2.5):", lista_numeros)

# eliminar un elemento por valor
lista_numeros.remove(4)
print("Después de remove(4):", lista_numeros)

# eliminar un elemento por índice y obtener su valor
elemento_eliminado = lista_numeros.pop(3)
print("Después de pop(3):", lista_numeros)
print("Elemento eliminado con pop(3):", elemento_eliminado)

# ordenar listas
lista_numeros = [3, 1, 4, 5, 2]
print("Lista desordenada:", lista_numeros)
lista_numeros.sort()
print("Después de sort():", lista_numeros)

# ordenar una lista creando una nueva lista
lista_desordenada = [3, 1, 4, 5, 2]
lista_ordenada = sorted(lista_desordenada)  
print("Lista desordenada original:", lista_desordenada)
print("Nueva lista ordenada con sorted():", lista_ordenada)

# invertir el orden de la lista
lista_numeros.reverse()
print("Después de reverse():", lista_numeros)