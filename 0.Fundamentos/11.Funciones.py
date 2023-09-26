# Funciones -> def
# entrada -> salida

# 1. Función sin parámetros
def saludar():
    print('Hola!')

saludar()

# 2. Funciones con parámetros

def saludar2(nombre):
    print(f'Hola {nombre}')

saludar2('Luis')
saludar2('Anderson')
auxNombre = 'Anita'
saludar2(auxNombre)

# 3. Varias parámetros
def saludar3(nombre, edad):
    print(f'Hola, {nombre} y mi edad es {edad}')

saludar3('Luis', 35)

def saludar4(nombre: str, edad: int):
    print(f'Hola, {nombre} en 10 años tendrás {edad+10} años')

saludar4('Luis', 35)

# Es posible llamar a una función dentro de otra

def saludar_dos_veces(nombre: str, edad: int):
    saludar3(nombre, edad)
    saludar4(nombre, edad)

saludar_dos_veces('Luis', 35)

# 4. Funciones con retorno
def elevarCubo(numero: int):
    return numero**3

n2 = elevarCubo(3)
print(n2)

# Función q no devuelve nada
saludo = saludar_dos_veces('Luis', 35)
print(saludo)



