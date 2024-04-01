#!/usr/bin/env python
# coding: utf-8

# ## Variables

'''1) Crear una variable que contenga un elemento del conjunto de números enteros y
luego imprimir por pantalla
'''

numero = 4
print(numero)

# 2) Imprimir el tipo de dato de la constante 8.5
numero2 = 8.5
print(type(numero2))

# 3) Imprimir el tipo de dato de la variable creada en el punto 1
print(type(numero))

# 4) Crear una variable que contenga tu nombre
nombre = 'Tatiana'
print(nombre)

# 5) Crear una variable que contenga un número complejo
numero_complejo = 5 + 4j

# 6) Mostrar el tipo de dato de la variable crada en el punto 5
print(type(numero_complejo))

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
cadena = 'True'

logica = True


# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8
print(type(cadena))
print(type(logica))

# 10) Asignar a una variable, la suma de un número entero y otro decimal

numero_entero = 34
numero_decimal = 24.654

print(numero_entero + int(numero_decimal))

# 11) Realizar una operación de suma de números complejos
numero_1 = 4 +5j
numero_2 = 5 + 3j

suma = numero_1 + numero_2
print(suma)

# 12) Realizar una operación de suma de un número real y otro complejo
numero_real = 45
numero_complejo = 3 +5j

suma = numero_real + numero_complejo
print(suma)

# 13) Realizar una operación de multiplicación
multiplicacion = 6 * 4
print(multiplicacion)

# 14) Mostrar el resultado de elevar 2 a la octava potencia
potencia = 2 ** 8
print(potencia)

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
cociente = 27/4
print(cociente)

# 16) De la división anterior solamente mostrar la parte entera
print(int(cociente))

# 17) De la división de 27 entre 4 mostrar solamente el resto
resto = 27 % 4
print(resto)

# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

operacion = 6 * 4 + 3
print(operacion)

# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

variable_1 = 'holi'
variable_2 = 'mundo'

concatenacion = variable_1 + variable_2
print(concatenacion)

# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

igualdad = '2' == 2
print(igualdad)

# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

nueva_igualdad = 2 == 2
print(nueva_igualdad)

# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# porque solo se puede pasar a flotantes numero no strings





# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

variable_3 = 3
variable_3 = variable_3 - 1
print(variable_3)

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

bitss = 1 << 2
print(bitss)

# da 4 porque se desplazan 2 espacios hacia la izquierda y los espacios vacios quedan 0


# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# da error porque no se pueden sumar numeros con strings

# 26) Realizar una operación válida entre valores de tipo entero y string

concatenacion = 34 + int('43')
print(concatenacion)








