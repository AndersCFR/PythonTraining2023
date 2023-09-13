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

