'''8. Realiza un programa que añada números enteros a una lista hasta que se
introduzca un número negativo. Haciendo uso de esta lista, elabora funciones que
devuelvan:
a. una lista con todos los que sean primos.
b. el sumatorio
c. el promedio de los valores.
d. una lista con el factorial de cada uno de esos números.'''
def escoger_primos (lista):
    lista_primos=[]
    contador=0
    for i in lista:
        for x in range (2,i):
            if(i%x==0):
                contador+=1
            else:
                if(x==len(lista)-1 and contador==0):
                    lista_primos.append(i)
    return lista_primos
def hacer_suma_lista (lista):
    suma=0
    for i in lista:
        suma+=i
    return suma
def hacer_promedio_lista (lista):
    suma=0
    for i in lista:
        suma+=i
    media=suma/len(lista)
    return media
def hacer_factorial_lista (lista):
    lista_factorial=[]
    contador=0
    factorial=1
    while(contador<len(lista)):
        for i in range(1,lista[contador]+1):
            factorial=factorial*i
        lista_factorial.append(factorial)
        factorial=1
        contador+=1
    return lista_factorial
numero=0
lista=[]
while(numero>=0):
    numero=int(input("Dime numeros hasta que introduzcas negativo"))
    if(numero>=0):
        lista.append(numero)
lista_primos=escoger_primos(lista)
print(lista_primos)
sumatorio_lista=hacer_suma_lista(lista)
print(sumatorio_lista)
promedio_lista=hacer_promedio_lista(lista)
print(promedio_lista)
lista_factorizada=hacer_factorial_lista(lista)
print(lista_factorizada)
            
        
        
                
