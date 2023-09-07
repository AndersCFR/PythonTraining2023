import math

# int()
# float()

num1 = int(input('Ingresa un número:'))
print(type(num1))

print(num1 + 10)

num2 = int(True)
print(num2)

num3 = int(False)
print(num3)

# Error
#num4 = int('Hola')
#print(num4)

a, b = 2,3

print('Suma', a+b)
print('Resta', a-b)
print('Multiplicacion', a*b)
print('División', a/b)
print('Potencia', a**b)
print('Raiz cuadrada', math.sqrt(16))

c,d = 2.5, 1.8
print('Suma', c+d)
print('Módulo', 10%3)
print('División entera', 10//3)


float_1 = float(input('Ingresa un número flotante:'))
print(float_1)

float2 = float('10.4556')
print(type(float2))
