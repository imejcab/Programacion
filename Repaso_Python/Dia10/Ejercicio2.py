'''2. Realiza un programa que lea 10 números, los imprima separados por coma y a
continuación los desplace una posición (y los muestre por pantalla desplazados), de
tal forma que el último pase a la primera posición, el primero a la segunda, el
segundo a la tercera, y así sucesivamente.
Opcional: Añade un parámetro (D/I) a la función para que el controle el sentido del
desplazamiento (a derechas/izquierdas) y otro que indique el número de posiciones
a desplazar (0: quedaría igual, 1: desplaza una posición, etc.).'''
def desplazar (lista):
    movimiento=-1
    for i in range (0,len(lista)):
        lista[-i]=lista[-i+movimiento]
    return lista
from random import randint
lista=[]
for i in range (0,10):
    numero=randint(0,1000)
    lista.append(i)
lista_desplazada=desplazar(lista)
print(lista_desplazada)

    