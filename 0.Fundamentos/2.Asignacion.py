# Operador de asignación

x = 5
print('El valor de x es:', x)

# Asignación sin valor
variable1 = None
print(type(variable1))
print('El valor es:', variable1)

# Sobreescitura de variables
y = 'Luis'
print(y)

y = 20
print(y)

y = y*2 # 40
print(y)

print(y*2)

print(y)

# Multiples asignaciones

x1 = 2
y1 = 3

x1, y1, z1 = 2, 3, 'Hola'

print(x1)
print(y1)
print(z1)

# Asignación del valor de una variable hacia otra variable
saludo = 'Buenas noches'
print(saludo)

saludo2 = saludo
print(saludo2)

saludo = 'Buenos días'
print(saludo2)
print(saludo)

# Ejercicio

x2, y2 = 10,11
z2 = x2
y2 = z2 + 2
print(x2, ' ', y2, ' ', z2)

