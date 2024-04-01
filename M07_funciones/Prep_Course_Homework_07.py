# Funciones
# Crea una funcion que reciba un numero si es primo es True si no es False

def numero2(num):
    if num % 2 == 0:
        return 'no primo'
    else:
        return 'primo'


resultado = numero2(3)
print(resultado)

# pase como parametro una lista y decir si es primo o no
lista = [1,2,3,4,5,6]

def numeros_primos(lista):
    for i in lista:
        if i % 2 == 0:
            print('no primo')
        else:
            print('primo')
numeros_primos(lista)

# crea una funcion que devuelva el nunero que mas se repite y cuantas veces
lista = [1,2,2,3,4,4,4,5,5,5,6,6,6,6]
frecuencia = {}

for i in lista:
    if i in frecuencia:
        frecuencia[i] = frecuencia[i] + 1
    else:
        frecuencia[i] = 1

numero_repetido = None
repeticion = 0
for i, frecuencia in frecuencia.items():
    if frecuencia > repeticion:
        numero_repetido = i
        repeticion = frecuencia

print(numero_repetido, repeticion)

# crear una funcion que convierta entre grados

def conversion(celsius, farenheit):
    celsiu_a_fa= celsius * 9/5
    fah_a_cel = farenheit * 6
    return celsiu_a_fa, fah_a_cel

resultado = conversion(34,65)
print(resultado)