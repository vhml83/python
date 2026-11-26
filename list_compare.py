import copy

precios = [205.30, 107.18, 25, 450, 310.89, 170.23, 340]
vacia = []
colores_primarios = ['rojo', 'verde', 'azul']
colores = ['verde', 'azul', 'amarillo', 'blanco']

if precios:
    print('Lista precios: no vacía')
else:
    print('Lista precios: vacía')

if not vacia:
    print('Lista vacía: vacía')
else:
    print('Lista vacía: no vacía')

# Operadores relacionales.
otra_lista = precios #Asigna la lista a otra variable.
if precios == otra_lista:
    print('Las listas son iguales')
else:
    print('Las listas no son iguales')

if precios == colores_primarios:
    print('precios y colores son iguales')
else:
    print('precios y colores no son iguales')

if colores_primarios != colores:
    print('Listas colores y colores_primarios son distintas')

if colores_primarios < colores:
    print('Listas colores_primarios es menor que lista colores')

# Operadores de identidad
if precios is otra_lista:
    print('precios y otra lista son la misma lista')
else:
    print('no son la misma lista')

copia = copy.copy(precios) #Hace una copia de la lista. Es otro objeto
if precios is copia:
    print('son la misma lista')
else:
    print('precios y copia no son la misma lista')

if colores is not colores_primarios:
    print('colores y colores primarios no son la misma lista')

# Operadores de membresía
if 'rojo' in colores_primarios:
    print('El rojo es un color primario')

if 'dorado' not in colores_primarios:
    print('El dorado no es un color primario')