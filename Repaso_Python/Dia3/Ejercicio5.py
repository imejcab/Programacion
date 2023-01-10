'''5. Realiza una función reverse que reciba una lista y devuelva una nueva lista cuyo
contenido sea igual a la original pero invertida. Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’,
‘papa’], deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’].'''
def mostrar_lista_inversa (lista):
    lista_nueva=[]
    contador=-1
    while(contador>=-len(lista)):
        lista_nueva.append(lista[contador])
        contador-=1
    return lista_nueva
lista=["Buenos","Dias","Princesa"]
lista_inversa=mostrar_lista_inversa(lista)
print(lista_inversa)
def mostrar_lista_inversaa (lista):
    lista_nueva=[]
    contador=-1
    for i in range (0,len(lista)):
        lista_nueva[contador].append(lista[i])
    return lista_nueva
lista=["hi","ho","hu"]
lista_reverse=mostrar_lista_inversa (lista)
print(lista_reverse)
        