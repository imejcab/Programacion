'''11. Escribe una función intersect que reciba dos listas y devuelva otra lista con los
elementos que son comunes a ambas, sin repetir ninguno'''
def intersect (lista1,lista2):
    lista_comunes=[]
    contador1=0
    contador_comunes=0
    while(contador1<len(lista1)):
        for i in lista2:
            if(lista1[contador1]==i):
                if(len(lista_comunes)==0):
                    lista_comunes.append(i)
                    contador1+=1
                else:
                    while(contador_comunes<len(lista_comunes)):
                        if(i!=lista_comunes[contador_comunes]):
                            contador_comunes+=1
                            if(contador_comunes==len(lista_comunes)):
                                lista_comunes.append(i)
                                contador1+=1
                        else:
                            contador_comunes=len(lista_comunes)
                            contador1+=1
            else:
                contador_comunes+=1
        contador_comunes=0
    return lista_comunes
lista1=[2,4,68,3,2,2]
lista2=[2,4,68,7,3,9]
lista_repetidos=intersect(lista1,lista2)
print(lista_repetidos)
                
                
        
        
