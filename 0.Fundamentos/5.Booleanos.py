# Bool
# bool()
# Dos valores True o Flase
# True == 1, False == 0

variable1 = True
variable2 = False

print(type(variable1))

# Truly/Falsy
print(bool(1))
print(bool(0))
print(bool(34))
print(bool(''))
print(bool('Aló'))

# Operadores
print('Operaciones con booleanos')

# Negación
print(not variable1)
print(not variable2)

# Conjunción, and, 
print(variable1 and variable2)
print(variable1 and True)

# Disyunción, or
print(variable1 or variable2)
print(False or variable2)

# Operadores bit a bit
# print(True & True)
# OR |, >>, <<
