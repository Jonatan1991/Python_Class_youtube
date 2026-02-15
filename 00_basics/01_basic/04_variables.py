# Variables in Python

# Assigning values to variables
name = "Alice"
age = 30
height = 5.5

# Printing variable values
print("Name:", name)
print("Age:", age)
print("Height:", height)


# tipado dinamico
variable = 10          # variable is an integer
print("Variable initially:", variable, "Type:", type(variable))
variable = "Now I'm a string"  # variable is now a string
print("Variable now:", variable, "Type:", type(variable))

#tipado fuerte
num = 5
print("Num as integer:", num, "Type:", type(num))
# The following line would raise an error if uncommented
# num = num + " is a string"  # Uncommenting this will raise a TypeError
# Correct way to concatenate different types
num_str = str(num) + " is a string"
print("Concatenated string:", num_str)
print("Num as string:", num_str, "Type:", type(num_str))

# Convenciones de nombres de variables
my_variable = 10          # snake_case
myVariable = 20          # camelCase
MY_CONSTANT = 30         # UPPER_SNAKE_CASE


# Buenas prácticas
# Usar nombres descriptivos
user_age = 25

# Evitar nombres reservados
# def = 10  # This would raise a SyntaxError
# Evitar caracteres especiales
#user-name = "Bob"  # This would raise a SyntaxError
user_name = "Bob"  # Correct way

# Evitar espacios en blanco
#user age = 25  # This would raise a SyntaxError
user_age = 25  # Correct way

# Comentarios
# This is a single-line comment

"""
This is a multi-line comment

that spans multiple lines.
"""

# Palabras reservadas
import keyword
print("Palabras reservadas en Python:")
print(keyword.kwlist)

#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 
# 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
# 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 
# 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
