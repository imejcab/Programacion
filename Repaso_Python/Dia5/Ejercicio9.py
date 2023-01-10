'''9. Desarrolla un programa que a partir de una lista de números y un entero k, realice la
llamada a tres funciones: a) para devolver una lista de números con los menores de
k, b) otra con los mayores y c) otra con aquellos que son múltiplos de k.'''
def nombrar_menor (lista,k):
    lista_menor=[]
    for i in lista:
        if(i<k):
            lista_menor.append(i)
    return lista_menor
def nombrar_mayor (lista,k):
    lista_mayor=[]
    for i in lista:
        if(i>k):
            lista_mayor.append(i)
    return lista_mayor
def multiplos_k (lista,k):
    lista_multiplos=[]
    for i in lista:
        if(i%k==0):
            lista_multiplos.append(i)
    return lista_multiplos
lista=[2,6,8,99,4,45,3]
k=3
menor=nombrar_menor(lista,k)
print(menor)
mayor=nombrar_mayor(lista,k)
print(mayor)
multiplo=multiplos_k(lista,k)
print(multiplo)