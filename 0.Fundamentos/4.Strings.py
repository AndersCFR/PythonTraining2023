# String -> str
# Es un dato indexable
# String es un tipo de dato inmutable

x = 'Estoy aprendiendo python'
print(type(x))

# Convertir a string
y = str(23)
print(type(y))

str_largo = '''La biblioteca de babel
Borges
Había una biblioteca ...
'''
print(str_largo)
texto2 = '''Este es otro
texto \tmuy grande
de python
'''
print(texto2)


# Operaciones
cadena1 = 'Python '
cadena2 = 'es un lenguaje de programación'

cadena3 = cadena1 + cadena2
print(cadena3)

print(cadena1 + cadena2 + ' muy importante en el año', 2023)
print(cadena1 + cadena2 + ' muy importante en el año' + '2023')
#print(cadena1 + cadena2 + ' muy importante en el año' + 2023) # error
print(cadena1 + cadena2 + ' muy importante en el año' + str(2023))

# Clases
# atributos
# métodos

# 1. Formated strings
nombre = 'Anderson'
edad = 23
estatura = 1.69
universidad = 'EPN'

formated_string = f'1. Hola mi nombres es {nombre} mi edad es {edad} mi estatura es {estatura} y estudié en {universidad}'
print(formated_string)

print('2. Hola mi nombre es {} mi edad es {} mi estatura es {}'.format(nombre, edad, estatura))
print('3. Hola mi nombre es {0} mi edad es {1} mi estaura es {2}'.format(nombre, edad, estatura))
print('4. Hola mi nombre es {variableNombre} y mi edad es {varEdad}'.format(variableNombre='Fernando', varEdad=edad))

# Indexación
palabras = 'ala enano iguana oso uva'
vocales = 'a e i o u'
numeros = '1 2 3 4 5'
vocales_separadas = vocales.split()
numeros_separados = numeros.split()
palabras_separadas = palabras.split()
print(vocales_separadas)
print(numeros_separados)
# Formated string in columns
print(f'{palabras_separadas[0]:{10}} {vocales_separadas[0]:{3}} {numeros_separados[0]}')
print(f'{palabras_separadas[1]:{10}} {vocales_separadas[1]:{3}} {numeros_separados[1]}')
print(f'{palabras_separadas[2]:{10}} {vocales_separadas[2]:{3}} {numeros_separados[2]}')


# Indexación
# [valorIncluido, valorExcluido]
# [0,2] ==> [0,2)

text_x = 'Esta es una cadena de ejemplo'
print(text_x[0:4])
print(text_x[5:12])
print(text_x[6:18])

# Indíce hasta el final
print(text_x[:6])
print(text_x[6:])

# Todo el contenido
print(text_x[:])

# Ejercicio avanzado
print(text_x[-4:])
cadenaInvertida = text_x[::-1]
print(cadenaInvertida)

# Métodos
texto5 = 'esta es la prueba de los métodos de los string'
print(texto5.upper())
print(texto5.capitalize())


