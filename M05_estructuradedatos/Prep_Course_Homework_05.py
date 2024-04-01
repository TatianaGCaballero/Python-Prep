# Estrucura de datos

# Crea una lista de ciudades que tenga 5 elementos e imprime

ciudades = ['cali', 'bogota', 'medellin', 'armenia', 'villavicencio']
print(ciudades)

# imprima el segundo elemento
print(ciudades[1])

# imprima del segundo al cuarto elemento
print(ciudades[1:5])

# ver el tipo de dato de la lista
print('El tipo de dato de la lista es una', type(ciudades))

# ver los elelemtos de la lista a partir del tercer elelemto
print(ciudades[2:])

# ver los primeros 4 elelemtos

print(ciudades[:4])

# agrega una ciudad que ya exista y otra nueva

# si agrego los dos elementos con append si me da error
ciudades.append('popayan')
ciudades.append('cali')
print(ciudades)

# agrega otra ciudad en la 4 posicion

ciudades.insert(3, 'ibague')
print(ciudades)

# concatenar otra lista a la ya creada

departamentos = ['valle', 'cundinamarca','antioquia','tolima','quindio','meta','cauca']
concatenacion = ciudades + departamentos
print(concatenacion)

# que pasa si busco un elemento no existente: DA ERROR

# elimina un elemento de la lista
concatenacion.pop(0)
print(concatenacion)

# que pasa si el elemento que elimine no existe: DA ERROR PORQUE ME SALI DEL RANGO

# extraer el ultimo elemento de la lista y guardarlo en variable

resultado = departamentos.pop()
print(resultado)

# mostrar la lista multiplicada por 4

multiplicacion = ciudades * 4
print(multiplicacion)

# Crear una tupla del 1 al 20

tupla = tuple(range(1, 20))
print(tupla)

# imprime desde el 10 al 15

print(tupla[9:15])

# Evalua si los numeros 20 y 30 estan en la tupla

resultado = 20 in tupla
resultado1 = 30 in tupla

print(resultado)
print(resultado1)

# en la lista de ciudades buscar si esta paris si no esta añadalo
resultado = 'paris' in ciudades
print(resultado)

ciudades.append('paris')
print(ciudades)

# mostrar cuantas veces se encuentra un elemento especifico

print(tupla.count(3))
print(ciudades.count('bogota'))

# convertir tupla en lista

lista = list(tupla)
print(lista)

# desempaquetar los 3 primeros elementos de la tupla

tupla1 = (1,2,3)
a,b,c = tupla1
print(a,b,c)

# crea un diccionario
diccionario = {'Ciudad': 'paris',
               'continente': 'Europa',
               'pais': 'francia'}

print(diccionario)

# imprima las claves

claves = diccionario.keys()
print(claves)

# imprima la ciudad a travez de su clave

print(diccionario['Ciudad'])




