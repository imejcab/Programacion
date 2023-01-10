'''12. Escribe una función unionListas que reciba dos listas y devuelva los elementos que
pertenecen a una, o bien, a la otra, pero sin repetir ninguno (unión de conjuntos).'''
def unir_listas (lista1,lista2):
    lista_union=lista2
    for i in lista1:
        contador=0
        while(contador<len(lista_union)):
            if(lista_union[contador]==i):
                contador=len(lista_union)
            else:
                contador+=1
                if(contador==len(lista_union)):
                    lista_union.append(i)
    return lista_union
lista1=[2,3,4,5,6,7,8,1]
lista2=[20,5,2,1,6,78,8]
lista_unida=unir_listas (lista1,lista2)
print(lista_unida)
                
            
