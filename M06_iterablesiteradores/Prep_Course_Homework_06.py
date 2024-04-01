# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1
lista = []

numero = -15

while numero <= -1:
    lista.append(numero)
    numero = numero + 1
print(lista)

# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?
n = 0
while n < len(lista):
    if lista[n] % 2 == 0:
        print(lista[n])
    n = n + 1


# 3) Resolver el punto anterior sin utilizar un ciclo while

for n in lista:
    if n % 2 == 0:
        print(n)
    else:
        break





# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos
for i in lista[:3]:
    print(i)





# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

for i, indice in enumerate(lista):
    print(i, indice)





# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

lista = [1,2,5,7,8,10,13,14,15,17,20]
numero = 1
while numero <= 20:
    if not(n in lista):
        lista.insert((n-1), n)
    n += 1
print(lista)


# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

fibonacci = [0,1]
n = 2
while(n < 30):
    fibonacci.append(fibonacci[n-1]+fibonacci[n-2])
    n = n + 1
print(fibonacci)



# 8) Realizar la suma de todos elementos de la lista del punto anterior


lista = [1,2,5,7,8,10,13,14,15,17,20]

suma = 0

for i in lista:
    suma = suma + i
print(suma)




# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>
#  

# In[38]:




# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

cadena = '  Hola mundo'

print(cadena.index(n))

# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

diccionario = {'nombre': ['tati', 'yei', 'sofi'],
               'educacion': ['biologa', 'ing','biologa']
               }

for clave in diccionario:
    print(clave)


# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

cadena = 'Hola mundo'
lista = cadena.split()
print(lista)

for i in lista:
    print(i)
# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

lista1 = [1,2,3,4]
lista2 = [5,6,7,8]

combinacion = zip(lista1, lista2)
print(combinacion)




# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

lista = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
lista = []

for i in lista:
    if i % 7 == 0:
        lista.append(i)
    

# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

cantidad = 0
for i in lis:
     if (type(i) == list):
        cantidad += len(i)
     else:
        cantidad += 1
print(cantidad)


# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

for indice, elemento in enumerate(lis):
    if (type(elemento) != list):
        lis[indice]=[elemento]
print(lis)



