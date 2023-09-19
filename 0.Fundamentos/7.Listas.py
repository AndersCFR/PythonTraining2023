# Listas 
# list()
# Inicialización []
# Mutable


lista_numeros = [1,2,3,4,5,6,7,8,9]
print(type(lista_numeros))

# Lista de varios tipos de datos
listas_variada = [1,2, 3, 4, 5, 'a', 'b', 'c', True, 34.6]
print(listas_variada)

# Métodos y operaciones

# Size
print(len(listas_variada))

# Indexación
print(lista_numeros[0:2])
print(lista_numeros[4])

# Mutable
listas_variada[0] = 0
print(listas_variada)

print(listas_variada[::-1])

lista2 = listas_variada[3:6]
print(lista2)

# Métodos

listaAlumnos = ['Anderson', 'Luis', 'Anita']

# Append, agregar datos al final
listaAlumnos.append('Pepito')
print(listaAlumnos)

#Insert, agregar un dato auna posición específica
listaAlumnos.insert(3, 'Juanita')
print(listaAlumnos)

# Extend
listaAlumnos.extend(['Pablito', 'María'])
print(listaAlumnos)

# Retirar valores al final de la lista
listaAlumnos.pop()
print(listaAlumnos)

# Retirar con pop en un índice específico
listaAlumnos.pop(1)
print(listaAlumnos)

# Retira un valor de la lista
listaAlumnos.remove('Pablito')
print(listaAlumnos)

listaAlumnos.extend(['Alejandro', 'Alejandro'])
print(listaAlumnos)

# Remove con dos elementos iguales
listaAlumnos.remove('Alejandro')
print(listaAlumnos)

# Métodos y operadores de las listas
print('Anita' in listaAlumnos)
print('Fabian' in listaAlumnos)

# Hacer una copia de una lista
copiaLista = listaAlumnos[::]
print(copiaLista)
copiaLista2 = listaAlumnos.copy()
print(copiaLista2)

# Encontrar el índice de un elemento en la lista
print(listaAlumnos.index('Pepito'))

# Solicito el índice de un valor que no se encuentra en la lista, genera un error
#print(listaAlumnos.index('Maria'))

# ¿Qué pasaría si solicita un índice de un elemento que aparece más de una vez?
listaAlumnos.append('Pepito')
print(listaAlumnos)
print(listaAlumnos.index('Pepito'))

# Ordenar una lista
listaAlumnos.sort()
print(listaAlumnos)

listaNumeros = [2, 6, 9, 1, -4, 3.14]
listaNumeros.sort()
print(listaNumeros)

listaNumeros.sort(reverse=True)
print(listaNumeros)

# Contar elementos en una lista
print(listaAlumnos.count('Anita'))

# Crear una lista vacía
listaVacia = []
print(listaVacia)

# Limpiar una lista
temp = listaAlumnos.copy()
print(f'Lista: {temp}')
temp.clear()
print(f'Lista limpiada: {temp}')

# Desempaquetado/empaquetado
nombre1, nombre2, nombre3 = listaAlumnos[0:3]
print(nombre1)
print(nombre2)
print(nombre3)

# Empaquetado de variables en lista
numero1 = 45.6798
lista_empaqueta = [nombre1, nombre2, numero1]
print(lista_empaqueta)

# desempaqueta 2
nombre1, *nombres = listaAlumnos
print(nombre1)
print(nombres)

# desempaquetaddo 3
*nombres2, antepenultimoNombre, ultimoNombre = listaAlumnos
print(nombres2)
print(antepenultimoNombre)
print(ultimoNombre)

# Lista de lista
matriz = [
    [0,1,2],
    [1,1,3],
    [0,9,8]
]
print(matriz)

print(matriz[1][1])