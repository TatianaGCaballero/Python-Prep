#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
numero = 6

if numero > 0:
    print('ES mayor a 0')
else:
    print('Es menor a 0 ')

# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

variable_1 = 5
variable_2 = 4
if type(variable_1) == type(variable_2):
    print('Son del mismo tipo')
else:
    print('Son diferentes')

# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
for i in range(1,20):
    if i % 2 == 0:
        print('Es par')
    else:
        print('Es impar')

# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

for i in range(0,5):
    print(i**3)


# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

variable_3 = 6

for i in range(0, variable_3):
    print(i)

# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0
numero = 4
while numero > 0:
     cuadrado = numero **2
     numero = numero - 1
     print(cuadrado)

# 7) Crear un ciclo for dentro de un ciclo while

n = 0
while(n < 5):
    n += 1
    for i in range(1,n):
        print(i)

# 8) Crear un ciclo while dentro de un ciclo for

n = 5
for i in range(1, n):
    while(n < 5):
        n -= 1
        print('Ciclo while nro ' + str(n))
        print('Ciclo for nro ' + str(i))




# 9) Imprimir los números primos existentes entre 0 y 30
num = 31
for i in range(0,num):
    if i % num == 0:
        print('No es primo')
    else:
        print(i)

# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

num = 31
for i in range(0,num):
    if i % num == 1:
        print(i)
    break

# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?



# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300



# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente






# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:
#22

