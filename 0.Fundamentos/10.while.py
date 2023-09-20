# While
# mientras

#x = True
#while x:
#    print('Hola')


y = 0
while y < 5:
    y = y + 1
    print(y)

# Introducción  a las funciones

def menu():
    print('\tHola')
    print('Ingresa las opciones:')
    opcion = input('Opción: ')
    return opcion

#var1 = menu()
#var2 =  menu()
#var3 = menu()


def main():
    terminarJuego = False
    while terminarJuego == False:
        opcionMenu = menu()
        if opcionMenu == '4':
            terminarJuego=True

main()
