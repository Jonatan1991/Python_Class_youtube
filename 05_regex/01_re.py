##
# 01 - Expresiones regulares
# 

""" Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda.
    Se utilizan para la búsqueda de cadenas de texto, validación de datos, etc. """


""" ¿Por qué aprender Regex?

- Búsqueda avanzada: Encontrar patrones específicos en textos grandes de forma rápida y precisa. (un editor de Markdown sólo usando Regex)

- Validación de datos: Asegurarte que los datos que ingresa un usuario como el email, teléfono, etc. son correctos.

- Manipulación del texto: Extraer, reemplazar y modificar partes de la cadena de texto fácilmente
"""

import re

# Ejemplo básico: Buscar una palabra en un texto
text = "Hola, mi nombre es midudev y me gusta programar en Python. midudev es mi alias."

pattern = "midudev"

result = re.search(pattern, text)

if result:
    print(f"Encontrado: {result.group()} en la posición {result.start()}-{result.end()}")
else:
    print("No encontrado")

# .group() devuelve la coincidencia completa
print(result.group())  # midudev

# .start() devuelve la posición inicial de la coincidencia
print(result.start())  # 18

# .end() devuelve la posición final de la coincidencia
print(result.end())    # 25

# Buscar todas las ocurrencias de una palabra
texto = "midudev es genial. midudev crea contenido. midudev enseña programación."
patron = "midudev"
resultados = re.findall(patron, texto)
print(resultados)  # ['midudev', 'midudev', 'midudev']

# iter() para obtener todas las coincidencias con más detalles
resultados_iter = re.finditer(patron, texto)
for match in resultados_iter:
    print(f"Encontrado: {match.group()} en la posición {match.start()}-{match.end()}")


### Modificadores
# LOs modificadores son banderas que cambian el comportamiento de la búsqueda.

texto = "Hola Mundo. hola mundo. HOLA MUNDO."

patron = "hola"

found = re.findall(patron, texto, re.IGNORECASE)  # Ignorar mayúsculas y minúsculas

if found:
    print(found)  # ['Hola', 'hola', 'HOLA']

## Reemplazar texto
texto = "El clima es soleado. El clima es cálido."

patron = "clima"
reemplazo = "tiempo"
nuevo_texto = re.sub(patron, reemplazo, texto)
print(nuevo_texto)  # El tiempo es soleado. El tiempo es cálido