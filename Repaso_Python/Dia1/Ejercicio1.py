'''Genere 100 números de forma aleatoria y que posteriormente
ofrezca al usuario la posibilidad de:
a. Conocer el mayor
b. Conocer el menor
c. Obtener la suma de todos los números
d. Obtener la media
e. Sustituir el valor de un elemento por otro número introducido por teclado
f. Mostrar todos los números
⇒ Realiza cada una de las opciones con funciones.
⇒ Utiliza la función siguiente para generar números aleatorios (entre 0 y 1000).'''
lista=[]
from random import randint
for i in range (0,101):
    numero=randint(0,1000)
    lista.append(numero)
def escoger_mayor (lista):
    valor_mayor=0
    for i in lista:
        if(i>=valor_mayor):
            valor_mayor=i
    return valor_mayor
def escoger_menor (lista):
    valor_menor=1000
    for i in lista:
        if(i<=valor_menor):
            valor_menor=i
    return valor_menor
def realizar_suma (lista):
    valor_total=0
    for i in lista:
        valor_total+=i
    return valor_total
def realizar_media (lista):
    valor_total=0
    for i in lista:
        valor_total+=i
    valor_medio=valor_total/len(lista)
    return valor_medio
def sustituir_elemento (lista,valor_sustituido,valor_prioritario):
    lista_nueva=[]
    for i in lista:
        if(i==valor_sustituido):
            lista_nueva.append(valor_prioritario)
        else:
            lista_nueva.append(i)
    return lista_nueva
def mostrar_numeros (lista):
    return lista
numero_mayor=escoger_mayor(lista)
numero_menor=escoger_menor(lista)
media=realizar_media(lista)
suma=realizar_suma(lista)
valor_sustituido=int(input("Dime que numero deseas intercambiar"))
valor_prioritario=int(input("Dime que numero deseas para el intercambio"))
lista_sustituida=sustituir_elemento(lista,valor_sustituido,valor_prioritario)
numeros=mostrar_numeros(lista)
print(numero_mayor)
print(numero_menor)
print(suma)
print(media)
print(lista_sustituida)
print(numeros)
