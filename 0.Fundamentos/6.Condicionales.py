# Palabras que permiten definir el flujo de código

es_mayor_edad = True
esta_afiliado = False
tiene_trabajo = True

# Comparión explícita
if es_mayor_edad and tiene_trabajo == True:
    print('Es una persona independiente')
else:
    print('No es una persona independiente')

# Comparaciones implícitas

# Es posible usar el if not para esperar por defecto un valor falso

texto = 'Anderson'
if texto.startswith('A'):
    print('Tu nombre empieza con A')
elif texto.startswith('B'):
    print('Tu nombre empieza con B')
else:
    print('Tu nombre no empieza ni con A ni con B')
    
saldo_cuenta_bancaria = 40000

if saldo_cuenta_bancaria >= 20000:
    print('La persona puede dar la entrada de una casa')
else:
    print('La persona no puede comprar una casa aún')


print(10>=10)
print(20<30)
print(100==100.5)
print(200!=200) # son distintos
print(200!=201)


x = 800
print(0 < x <100)

# a, b, c, d , 
print('Ala' < 'Oso')
print('Ab' < 'Ac')