'''1. Crea un programa que genere 100 números de forma aleatoria y que posteriormente
ofrezca al usuario la posibilidad de:
a. Conocer el mayor
b. Conocer el menor
c. Obtener la suma de todos los números
d. Obtener la media
e. Sustituir el valor de un elemento por otro número introducido por teclado
f. Mostrar todos los números
⇒ Realiza cada una de las opciones con funciones.
⇒ Utiliza la función siguiente para generar números aleatorios (entre 0 y 1000)'''
def mayor (lista_numeros):
    mayor=0
    for i in lista_numeros:
        if(i>mayor):
            mayor=i
    return mayor
def menor (lista_numeros):
    menor=1000
    for i in lista_numeros:
        if(i<menor):
            menor=i
    return menor
def suma (lista_numeros):
    suma=0
    for i in lista_numeros:
        suma+=i
    return suma
def media (lista_numeros):
    suma=0
    cantidad_numeros=len(lista_numeros)
    for i in lista_numeros:
        suma+=i
        media=suma/cantidad_numeros
    return media
def sustituir_elemento (lista_numeros,elemento,numero_elegido):
    lista_nueva=[]
    for i in lista_numeros:
        if(i==elemento):
            i=numero_elegido
        lista_nueva.append(i)
    return lista_nueva
def mostrar_numeros (lista_numeros):
    return lista_numeros
lista_numeros=[]
from random import randint
for i in range (0,100):
    numero=randint(0,1001)
    lista_numeros.append(numero)
elemento=int(input("Dime un numero del 0 al 1000"))
while(elemento<0 or elemento>1000):
    elemento=int(input("Dime un numero_valido"))
numero_elegido=int(input("Dime un numero del 0 al 1000"))
while(numero_elegido<0 or numero_elegido>1000):
    numero_elegido=int(input("Dime un numero valido"))
numero_mayor=mayor(lista_numeros)
print(numero_mayor)
numero_menor=menor(lista_numeros)
print(numero_menor)
suma_numeros=suma(lista_numeros)
print(suma_numeros)
media_numeros=media(lista_numeros)
print(media_numeros)
lista_sustituida=sustituir_elemento(lista_numeros,elemento,numero_elegido)
print(lista_sustituida)
numeros_mostrados=mostrar_numeros(lista_numeros)
print(numeros_mostrados)