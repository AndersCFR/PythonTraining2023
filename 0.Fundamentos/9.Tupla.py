# Tupla -> tuple()
# Inmutable

tupla1 = (3,4,5,6,7)
print(type(tupla1))
print(tupla1)

# accediendo a datos de una tupla
print(tupla1[0])

# Tupla con diferentes tipos de datos
tupla2 = (True, 25, 'Hola', True)
print(tupla2)

# Averiguar si un elemento está o no en una lista
print(100 in tupla1)

print('Hola' in tupla2)

# Comprobar q no está en la tupla
print('Chao' not in tupla2)

# Métodos de la tupla
# 1. index
print(tupla1.index(3))
print(tupla2.index('Hola'))

# Si el elemento no está en al tupla muestar error
# print(tupla2.index('Adios'))

# 2. Count
print(tupla2.count(True))

# Descompresión tupla
dimensiones = (500, 600)
dimensionX, dimensionY = dimensiones
print(dimensionX + 400)

# Convertir una lista a un tupla
lista1 = [85, 12, 356, 45]

miTupla = tuple(lista1)
print(miTupla)


