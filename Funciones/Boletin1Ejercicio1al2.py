#Ejercicio 1
'''Crea un programa que genere 100 números de forma aleatoria y que posteriormente
ofrezca al usuario la posibilidad de:
a. Conocer el mayor
b. Conocer el menor
c. Obtener la suma de todos los números
d. Obtener la media
e. Sustituir el valor de un elemento por otro número introducido por teclado
f. Mostrar todos los números
⇒ Realiza cada una de las opciones con funciones.
⇒ Utiliza la función siguiente para generar números aleatorios (entre 0 y 1000).'''
numero=0
def mayor(numero):
    contador=0
    contador1=100
    numero2=0
    while(contador!=contador1):
        contador+=1
        from random import randint
        numero=randint (0,1000)
        if(numero>numero2):
            numero2=numero
    return(numero2)
def menor(numero):
    contador=0
    contador1=100
    numero1=999
    while(contador!=contador1):
        contador+=1
        from random import randint
        numero=randint (0,1000)
        if(numero<numero1):
            numero1=numero
    return(numero1)
def sumar(numero):
    contador=0
    contador1=100
    numero1=0
    while(contador!=contador1):
        contador+=1
        from random import randint
        numero=randint (0,1000)
        numero1+=numero
    return numero1
def media(numero):
    contador=0
    contador1=100
    numero1=0
    numero2=0
    while(contador!=contador1):
        contador+=1
        from random import randint
        numero=randint (0,1000)
        numero1+=numero
        numero2=numero1/contador
    return numero2
def sustituir(numero):
    contador=0
    contador1=100
    numero1=int(input("Dime un numero"))
    while not(numero>=0 or numero<=1000):
        numero1=int(input("Dime un numero"))
    while(contador!=contador1):
        contador+=1
        from random import randint
        numero=randint (0,1000)
        if(contador==10):
            numero=numero1
            print(numero)
        else:
            print(numero)
def mostrar(numero):
    contador=0
    contador1=100
    while(contador!=contador1):
        contador+=1
        from random import randint
        numero=randint (0,1000)
    return(numero)
valor= mayor(numero)
print(valor)
valor1= menor(numero)
print(valor1)
valor2= sumar(numero)
print(valor2)
valor3= media(numero)
print(valor3)
valor4= sustituir(numero)
print(valor4)
valor5=mostrar(numero)
print(valor5)
#EJERCICIO 2
'''Realiza un programa que lea 10 números, los imprima separados por coma y a
continuación los desplace una posición (y los muestre por pantalla desplazados), de
tal forma que el último pase a la primera posición, el primero a la segunda, el
segundo a la tercera, y así sucesivamente.
Opcional: Añade un parámetro (D/I) a la función para que el controle el sentido del
desplazamiento (a derechas/izquierdas) y otro que indique el número de posiciones
a desplazar (0: quedaría igual, 1: desplaza una posición, etc.).'''
lista=[]
for i in range (1,11):
    lista.append(i)
print(lista)
numero=1
contador1=1
contador=1
lista[0]=10
while(contador1!=10):
    lista[contador1]=contador
    contador1+=1
    contador+=1
print(lista)
def dirigir(lista):
    parametro=str(input("Derecha o Izquierda"))
    while(parametro!="Derecha" and parametro!="Izquierda"):
        parametro=str(input("Derecha o izquierda"))
    return parametro
def desplazar(lista):
    posiciones=int(input("Dime cuantos desplazamientos"))
    while(posiciones<0 and posiciones>5):
        posiciones=int(input("Dime cuantos desplazamientos"))
    return posiciones
parametro=(dirigir(lista))
posiciones=(desplazar(lista))
lista2=[]
contador=0
while(contador!=10):
    contador+=1
    lista2.append(contador)
print(lista2)
contador=1
contador1=0
while(contador!=11):
    if(parametro=="Derecha"):
        if(i>=1 and i<=10):
            lista2[(contador1+posiciones)%10]=contador
            contador+=1
            contador1+=1
    else:
        if(i>=1 and i<=10):
            lista2[(contador1-posiciones)%10]=contador 
            contador+=1
            contador1+=1
print(lista2)  
    

    

