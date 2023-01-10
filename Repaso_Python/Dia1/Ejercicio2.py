'''Realiza un programa que lea 10 números, los imprima separados por coma y a
continuación los desplace una posición (y los muestre por pantalla desplazados), de
tal forma que el último pase a la primera posición, el primero a la segunda, el
segundo a la tercera, y así sucesivamente.
Opcional: Añade un parámetro (D/I) a la función para que el controle el sentido del
desplazamiento (a derechas/izquierdas) y otro que indique el número de posiciones
a desplazar (0: quedaría igual, 1: desplaza una posición, etc.).'''
def desplazar_posicion (lista):
    contador=len(lista)-1
    contador1=lista[-1]
    while(contador!=-1):
        if(contador==0):
            lista[contador]=contador1
            contador-=1
        else:
            lista[contador]=lista[contador-1]
            contador-=1
    return lista
lista=[0,2,4,1,5,6,7,6,4,2]
lista_desplazada=desplazar_posicion(lista)
print(lista_desplazada)
def desplazar_posiciones (lista, direccion, numero_desplazamientos):
    lista_nueva=["","","","","","","","","",""]
    contador=0
    while(contador<len(lista)):
        if(direccion=="Derecha"):
            lista_nueva[(contador+numero_desplazamientos)%10]=lista[contador]
            contador+=1
        else:
            lista_nueva[(contador+numero_desplazamientos)%10]=lista[contador]
            contador+=1
    return lista_nueva
lista=[0,2,4,1,5,6,7,6,4,2]
direccion=str(input("Dime derecha o izquierda"))
while(direccion!="derecha" and direccion!="izquierda"):
    direccion=str(input("Dime derecha o izquierda"))
numero_desplazamientos=int(input("Dime cuantos desplazamientos quieres"))
while(numero_desplazamientos<0 or numero_desplazamientos>5):
    numero_desplazamientos=int(input("Dime cuantos desplazamientos quieres"))
lista_desplazada=desplazar_posiciones (lista, direccion, numero_desplazamientos)
print(lista_desplazada)
    
            

            
        
    