# Solicitar al usuario 5 números y calcular la media de esos números
# Para ello crear una función llamada media()

# 1. La función solicitarNumeros me devuelve una lista con valores
def solicitarNumeros():
    listaNumeros = []
    for numero in range(0, 5):
        auxNumero = int(input(f'Ingresa el número {numero}: '))
        listaNumeros.append(auxNumero)
    return listaNumeros

numeros = solicitarNumeros()
print(numeros)

# (n1 + n2 + n3 + n4 +n5) / 5

# 2. Calcula media a partir de una lista
def calcularMedia(listaNumeros: list):
    acumulado = 0
    # 1. Sumar los 5 valores
    for numero in listaNumeros:
        acumulado = acumulado + numero
    # 2. Divide para 5 
    media = acumulado/5
    return media

mediaCalculada = calcularMedia(numeros)

print(f'La media de {numeros} es {mediaCalculada}')