'''14. Escribe una función que, dada una lista de cadenas, devuelva la cadena más larga.
Si dos o más cadenas miden lo mismo y son las más largas, la función devolverá la
que tenga el mayor número de caracteres repetidos'''
def tocar_larga (lista_cadenas):
    cadena_larga=""
    valor_repetido_larga=0
    for i in lista_cadenas:
        contador=0
        contador1=1
        valor_repetido=0
        while(contador<len(i)-1):
            if(i[contador]==i[contador+contador1]):
                valor_repetido+=1
                contador1+=1
                if(contador+contador1==len(i)):
                    contador+=1
                    contador1=0
            else:
                contador1+=1
                if(contador+contador1==len(i)):
                    contador+=1
                    contador1=0
        if(contador>len(cadena_larga)):
            cadena_larga=i
            valor_repetido_larga=valor_repetido
        elif(contador==len(cadena_larga)):
            if(valor_repetido>valor_repetido_larga):
                cadena_larga=i
                valor_repetido_larga=valor_repetido
    return cadena_larga
lista_cadenas=["holaa","adios","jajajaja","queeeeee"]
cadena_grande=tocar_larga (lista_cadenas)
print(cadena_grande)
                    
                    
                    
                
                
        
        