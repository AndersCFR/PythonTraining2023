# Solicitar a un usuario que ingrese el número de elementos que requiere para crear una lista
# Llenar cada uno de los valores con los datos solicitados al usario

# Paso 1
numeroElementos = int(input('Ingrese el numero de elementos: '))

# Paso 2 declarar una lista vacia
valores = []

# Paso 3 solicitar los elementos 
for posicion in range(0, numeroElementos):
    valorIngresado = input(f'Ingrese el valor para la posicion {posicion}: ')
    valores.append(valorIngresado)

print(f'Valores ingresados: {valores}')

