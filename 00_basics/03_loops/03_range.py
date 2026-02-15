# Range

nums = range(10)
print("Números del 0 al 9:", list(nums))

# Range con inicio y fin
for num in range(5, 15):
    print("Número:", num)

# Range con paso (inicio, fin, paso)
for num in range(0, 20, 2):
    print("Número par:", num)

# Range inverso
for num in range(10, 0, -1):
    print("Cuenta regresiva:", num)

for _ in range(3):
    print("¡Esto 3 veces!")