import pandas as pd

naranjas = pd.Series([4, 9, 2, 6, 10, 200])
manzanas = pd.Series([60, 22, 1, 79, 2, 8])
print(naranjas)
print(manzanas)

colores = pd.Series(["rojo", "azul", "amarillo", "verde", "morado" ])
print(colores)

print(colores.index)
print(colores.size)
print(colores.dtype)
print(colores[2:4])

print(naranjas.sum())
print(naranjas.max())
print(naranjas.min())

print(naranjas.std())
print(naranjas.describe())

materias = pd.Series({'Matematica': 6, 'Fisica': 1, 'Quimica': 7, 'Programacion': 10})

print(materias[materias > 6])
print(materias.sort_values())
print(materias.sort_index(ascending=True))