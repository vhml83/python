# Usando los [] y dando valores para inicializar las listas

dias_laborales = ["lunes", "martes", "miercoles", "jueves", "viernes"]
print ('\nLista de dias laborales:', dias_laborales)
print ('\nPrimer elemento dias laborales:', dias_laborales[0])
print ('\nÚltimo elemento dias laborales:', dias_laborales[-1])

fin_semana = ['sabado', 'domingo']
semana = dias_laborales + fin_semana
print ('\nSemana completa:', semana)

dias_laborales.append('sabado')
print ('\nSemana laboral más día extra:', dias_laborales)
print (f"\nEl lunes aparece = {dias_laborales.count('lunes')} vez (veces).")
dias_laborales.remove('sabado')
print ('\nSemana laboral sin sábado:', dias_laborales)

# Genera una nueva lista ordenada, sin alterar la lista original.
lista_ordenada = sorted(dias_laborales)
list_ord_long = sorted(dias_laborales, key=len)
print ('\nDias Laborales sin alterar:', dias_laborales)
print ('\nDias Laborales ordenados:', lista_ordenada)
print ('\nDias Laborales ordenados por longitud:', list_ord_long)

# Quitar el último elemento de la lista
rescatado = dias_laborales.pop() #sin posición, quita el último
print ('\nSe rescató para el fin de semana:', rescatado)


colores_primarios = ['rojo', 'verde', 'azul']
print ('\nLista de colores:', colores_primarios)
colores_repetidos = colores_primarios * 2
print ('\nColores repetidos:', colores_repetidos)
colores_primarios.insert(0, 'blanco')
colores_primarios.insert(10, 'amarillo')
print ('\nLista de colores con un nuevo elemento:', colores_primarios)
# Regresa posición de rojo dentro de la lista
print ('\nPosición del color rojo:', colores_primarios.index('rojo'))
# Regresa la posición del segundo azul
print ('\nPosición del segundo color azul:', colores_repetidos.index('azul', 3))
# Ordena los elementos de la lista de mayor a menor
colores_repetidos.sort(reverse=True)
print ('\nPrecios ordenados de mayor a menor:', colores_repetidos)
# Quita y regresa el elemento de la posición 0
quitado = colores_primarios.pop(0)
print ('\nEl elemento quitado es:', quitado)
print ('\nLa lista quedo:', colores_primarios)



precios = [205.30, 107.18, 25, 450, 310.89, 170.23, 340]
print ('\nLista de precios:', precios)
print ('\nEl tipo es:', type(precios))
print ('\nTotal de precios =', len(precios))
# Ordena los elementos de la lista de menor a mayor
precios.sort()
print ('\nPrecios ordenados de menor a mayor:', precios)

mescolanza = [12, 'octubre', 1492, 'llegó Cristobal Colon']
print ('\nLista con diferentes tipos de datos:', mescolanza)

vacia1 = []
print ('\nLista vacia:', vacia1)

# Se genera una lista vacía usando el constructor list() sin parámetros
vacia2 = list()
print ('\nLista vacía 2:', vacia2)

# Se genera una lista a partir de un rango
pares = list(range(0, 32, 2))
print ('\nPares menores a 30:', pares)

# Se genera una lista a partir de un rango
impares = list(range(29, 0, -2))
print ('\nImpares menores a 30:', impares)

# Invierte el orden de los elementos en la lista
impares.reverse()
print ('\nImpares en orden inverso:', impares)

# Se genera una lista con los caracteres de una cadena de caracteres.
caracteres = list('2020 es año bisiesto')
print('\nLista de caracteres:', caracteres)

# Se genera una lista con subcadenas de una cadena de caracteres.
frase = "La emigración no solo se hace para huir de la opresión de la casa, sino también para llegar a lo más hondo de nuestra alma."
palabras = frase.split()
print('\nLista de palabras:', palabras)

# Se genera una lista con los elementos de una tupla.
con_tuplas = list((6, 3, 8, 12, 15))
print('\nLista con los elementos de la tupla:', con_tuplas)

# Se genera una lista con los elementos de otra lista.
otra_lista = list(precios)
print('\nLa otra lista:', otra_lista)

# Se pueden generar sublistas a partir de una lista por medio de la partición o slicing
# sublista = lista[inicio:fin:n]

# Se crea una lista de números enteros
lista1 = [1,2,3,4,5,6]
print ("\nLista:", lista1)

# Sublista formada con los elementos de las posiciones 0 a la 2 inclusive
L1 = lista1[0:3]
print ("\nDel primero al tercero:", L1)

# Sublista formada con los elementos de las posiciones 3 a la 5 inclusive
L2 = lista1[3:]
print ("\nDel cuarto al último:", L2)

# Sublista formada con los elementos desde el inicio hasta el final con un salto de 2
L3 = lista1[::2]
print ("\nSalto de 2:", L3)

# Sublista formada con los elementos desde el final hasta el inicio con un salto de 3
L4 = lista1[-1::-3]
print ("\nOrden inverso; Salto de 3:", L4)

# Quita los elementos de la posición 0 a la última inclusive
del lista1[:]
print ("\nLuego de quitar todos los elementos de la lista:", lista1)

# Se crea una lista de cadena de caracteres
lista2 = list('abcdefghij')
print ("\nLista de caracteres:", lista2)

# Reemplaza los elementos de las posiciones 0 y 1 por los valores dados.
lista2[0:2] = ['rojo', 'verde']
print ("\nSe reemplazaron los primeros 2 valores:", lista2)

# Quita los elementos de las posiciones 4 a la 8 inclusive.
lista2[4:9] = []
print ("\nSe quitaron del 5to al 9no dato:", lista2)

# Agrega los valores de la lista en la posición 0, reemplazando el valor de esa posición
# y desplazando hacia la deracha todos los demás.
lista2[0:1] = ['azul','gris','blanco']
print ("\nLuego de agregar 3 colores a la lista:", lista2)

# Agrega todos sus elementos al inicio.
lista2[:0] = lista2
print ("\nLuego de agregar sus propios elementos:", lista2)

# Vacía la lista
lista2[:] = []
print ("\nLuego de vaciar la lista:", lista2)
