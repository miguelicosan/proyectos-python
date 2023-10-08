from random import randint

print('######################### ADIVINA EL NÚMERO #############################')

numero_secreto = randint(0, 101)
print(numero_secreto)

nombre = input('Ingresa tu nombre: ')

n_intentos = 1
total_intentos = 8

print(f'Hola, "{nombre}", he pensado un número entre 1 y 100\n'
      f',tienes { total_intentos } para adivinarlo.')

forzar_cierre = False

while n_intentos < 8:
    print('\n\n###########################################################################')
    numero = int(input('Ingresa un número entre (0 - 100): '))

    if numero not in range(1,100):
        print('El número no se encuentra entre 1-100.')
        continue
    elif numero == numero_secreto:
        print('\n\n######################### ¡¡¡ HAS GANADO !!! #############################')
        print(f'Has acertado el número { numero } en { n_intentos } intentos.')
        break
    elif numero_secreto > numero:
        print('\n\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print(f'El numero secreto es "MAYOR" que { numero }.')
        print(f'Te quedan { total_intentos - n_intentos }.')
    elif numero_secreto < numero:
        print('\n\nVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV')
        print(f'El numero secreto es "MENOR" que { numero }.')
        if n_intentos < 8:
            print(f'Te quedan { total_intentos - n_intentos } intentos.')
    else:
        print('Has ingresado algo que no es un número.')
        continue

    n_intentos += 1
else:
    print(':( :( :( :( :( :( :( :( :( :( :(  HAS PERDIDO  :( :( :( :( :( :( :( :( :( :( :( ')
    print(f'Has llegado a los { total_intentos } intentos.')
    print(f'El número secreto era el: { numero_secreto }.')
