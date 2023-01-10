'''6. Diseña una función llamada estaOrdenada que reciba una lista de elementos y
devuelva True si está ordenada o False en caso contrario.'''
def revisar_orden (lista):
    numero_anterior=-1000
    for i in range (0,len(lista)):
        if(lista[i]>=numero_anterior):
            numero_anterior=i
            if(i==len(lista)-1):
                resultado=True
        else:
            i=len(lista)
            resultado=False
    return resultado
lista=[1,2,3,4,5,6,7,3,9]
lista_revisada=revisar_orden(lista)
if(lista_revisada==True):
    print("Todo correcto y ordenado")
else:
    print("Lista desordenada")
def revisar_ordenn (lista):
    contador=0
    numero_anterior=-100
    while(contador<len(lista)):
        if(lista[contador]>=numero_anterior):
            numero_anterior=lista[contador]
            contador+=1
            if(contador==len(lista)):
                resultado=True
        else:
            contador=len(lista)
            resultado=False
    return resultado
lista=[1,2,3,4,5,6,7,6,9]
lista_revisada=revisar_ordenn(lista)
if(lista_revisada==True):
    print("Todo correcto y ordenado")
else:
    print("Lista desordenada")



