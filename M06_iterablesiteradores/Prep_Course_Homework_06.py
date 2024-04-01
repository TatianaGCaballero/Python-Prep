# iterables
'''
A partir de una lista vacia, utiliza un ciclo while para cargar alli
numeros negativos de -15 a -1
'''

lista = []
numero = -15
while numero <= -1:
    lista.append(numero)
    numero = numero + 1
print(lista)

# con un while es posible recorrer la lista para imprimir los numeros pares

n = 0
while n < len(lista):
    if lista[n] %2 == 0:
        print(lista[n])
    n = n + 1

# resolver el anterior sin el while

for i in lista:
    if i % 2 == 0:
        print(i)

# utilizar el iterable para recorrer los primeros 3 elementos

for i in lista[:3]:
    print(i)

# usar enumerate para iterar y mostrar el indice

for i, indice in enumerate(lista):
    print(i,indice)

# dada la siguiente lista crea un ciclo dpnde esten los valores faltantes

lista = [1,2,5,7,8,10,13,14,15,17,20]
numero = 1
while numero <= 20:
    if not(numero in lista):
        lista.insert((numero-1), numero)
    numero += 1
print(lista)

# sucesion de Fibonacci

fibonnaci = [0,1]
n = 2
while(n < 30):
    fibonnaci.append(fibonnaci[n-1] + fibonnaci[n-2])
    n = n + 1
print(fibonnaci)

# realizar la suma de la lista
lista = [1,2,5,7,8,10,13,14,15,17,20]

suma = 0

for i in lista:
    suma = suma + i
print(suma)

# A partir de la cadena busca la posicion n

cadena = '  Hola mundo'

print(cadena.index('n'))

# Crear un diccionario e imprimir sus claves utilizando un iterador

diccionario = {'nombre': ['tati', 'yei', 'sofi'],
               'educacion': ['biologa', 'ing','biologa']
               }

for clave in diccionario:
    print(clave)

# Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador

cadena = 'Hola mundo'
lista = cadena.split()
print(lista)

for i in lista:
    print(i)

# Crear dos listas y unirlas en una tupla utilizando la función zip

lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]

combinacion = zip(lista1, lista2)
print(combinacion)

# A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

lista = [18, 21, 29, 32, 35, 42, 56, 60, 63, 71, 84, 90, 91, 100]
lista2 = []

for i in lista:
    if i % 7 == 0:
        lista2.append(i)
print(lista2)

# Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

lista = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

for indice, elemento in enumerate(lista):
    if (type(elemento) != list):
        lista[indice]=[elemento]
print(lista)


