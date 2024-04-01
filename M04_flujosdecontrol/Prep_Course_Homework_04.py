# Flujos de control

'''
1) Crear una variable que contenga un elemento del conjunto de números enteros y
luego imprimir por pantalla si es mayor o menor a cero
'''

numero = 6
if numero > 0:
    print('Es mayor a 0')
else:
    print('Es menor a 0')

'''
2 crea dos variables y compara si son del mismo tipo
'''
variable_1 = 45
variable_2 = 32

if type(variable_1) == type(variable_2):
    print('Son del mismo tipo')
else:
    print('Son distintos')

# 3 para los valores de 1 a 20 imprima si es par o impar

for i in range(1,20):
    if i % 2 == 0:
        print(f'{i}, es par')
    else:
        print(f'{i}, no es par')

# 4 en un ciclo for del 0 al 5 elevarlo a la potencia igual a 3

for i in range(0,5):
    print(i ** 3)

'''
 5 Crear una variable que contenga un número entero y realizar un ciclo for 
 la misma cantidad de ciclos
'''

n = 10
for i in range(0, n):
    print(i)

'''
6 Utilizar un ciclo while para realizar el factoreo de un número 
guardado en una variable, sólo si la variable contiene 
un número entero mayor a 0
'''

'''numero = 5

factores = []
divisor = 2

while numero > 0:
    while numero == 0:
        factores.append(divisor)
        n//= divisor

    divisor = divisor + 1

print(factores)'''

'''
7 crear un ciclo while dentro de un ciclo for
'''
for i in range(1,5):
    contador = 0
    while contador < 3:
        print(f'{contador + 1} del numero {i}')
        contador = contador + 1


# 8 crea un ciclo whil dentro del ciclo for

n = 0
while n < 5:
    n = n + 1
    for i in range(1,n):
        print(i)

# 9) Imprimir los números primos existentes entre 0 y 30

numero = 30
for i in range(2,numero):
    if numero % i == 0:
        print(f'{i}, no es primo')
    else:
        print(f'{i}, es primo')

# 10 mejorar lo anterior
numero = 30
for i in range(2,numero):
    if numero % i == 0:
        print(f'{i}, no es primo')
        break


# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

n = 100
while(n<=300):
    if (n % 6 == 0):
        print(f'El nunero es {n}')
        break
    n += 1