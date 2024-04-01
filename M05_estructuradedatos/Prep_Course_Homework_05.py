#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

ciudades = ['cali', 'medellin', 'Bogota', 'popayan', 'santa marta', 'neiva']
print(ciudades)




# 2) Imprimir por pantalla el segundo elemento de la lista

print(ciudades[1])
# 3) Imprimir por pantalla del segundo al cuarto elemento
print(ciudades[1:4])

# 4) Visualizar el tipo de dato de la lista

print(type(ciudades))


# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

print(ciudades[2:])


# 6) Visualizar los primeros 4 elementos de la lista

print(ciudades[0:4])

# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

ciudades.append('New york')
print(ciudades)
ciudades.append('Bogota')
print(ciudades)

# 8) Agregar otra ciudad, pero en la cuarta posición

ciudades.insert(3, 'Cali')
print(ciudades)

# 9) Concatenar otra lista a la ya creada

lista_2 = ['popayan', 'meta', 'villavicencio']
concatenacion = ciudades + lista_2
print(concatenacion)

# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

ciudad = ciudades.index('Bogota')
print(ciudad)

# 11) ¿Qué pasa si se busca un elemento que no existe?
# me aparece un value error

# 12) Eliminar un elemento de la lista

eliminado = ciudades.pop(0)
print(ciudades)




# 13) ¿Qué pasa si el elemento a eliminar no existe?
# me aparece que me sali del rango






# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

eliminado = ciudades.pop()
print(eliminado)

# 15) Mostrar la lista multiplicada por 4

multiplicacion = ciudades * 4

# 16) Crear una tupla que contenga los números enteros del 1 al 20
tupla = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

# 17) Imprimir desde el índice 10 al 15 de la tupla

print(tupla[9:15])

# 18) Evaluar si los números 20 y 30 están dentro de la tupla

resultado = 20 in tupla
print(resultado)

resultado = 30 in tupla
print(resultado)

# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.


resultado = 'paris' in ciudades
print(resultado)


ciudades.append('Paris')
print(ciudades)

# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

print(tupla.count(10))
print(ciudades.count('Bogota'))

# 21) Convertir la tupla en una lista

lista = list(tupla)
print(lista)

# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
tupla2 = 1,2,3
a,b,c = tupla2
print(a,b,c)

# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

diccionario = {'Ciudad': 'paris',
               'continente': 'Europa',
               'pais': 'francia'}

print(diccionario)

# 24) Imprimir las claves del diccionario

print(diccionario.keys)

# 25) Imprimir las ciudades a través de su clave

print(diccionario['Ciudad'])




