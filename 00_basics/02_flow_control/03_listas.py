#creacion de listas
lista_vacia = []
lista_numeros = [1, 2, 3, 4, 5]
lista_mixta = [1, "dos", 3.0, True]
lista_anidada = [1, [2, 3], [4, [5, 6]]]

print("Lista vacía:", lista_vacia)
print("Lista de números:", lista_numeros)
print("Lista mixta:", lista_mixta)
print("Lista anidada:", lista_anidada)

#acceder a elementos por indice
print("Primer elemento de lista_numeros:", lista_numeros[0])
print("Segundo elemento de lista_mixta:", lista_mixta[1])
print("Elemento anidado en lista_anidada:", lista_anidada[2][1][0])

#slicing de listas
print("Primeros tres elementos de lista_numeros:", lista_numeros[0:3])
print("Elementos desde el segundo hasta el final de lista_mixta:", lista_mixta[1:])
print("Ultimos dos elementos de lista_numeros:", lista_numeros[-2:])
print("Paso de 2 en lista_numeros:", lista_numeros[::2])

#modificar elementos de una lista
lista_numeros[0] = 10
print("Lista de números después de modificar el primer elemento:", lista_numeros)

#agregar elementos a una lista concatenando
lista_numeros = lista_numeros + [6, 7, 8]