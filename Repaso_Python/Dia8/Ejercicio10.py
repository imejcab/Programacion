'''10. Escribir una función que, devuelva el número de palabras que hay en una cadena que recibe
como parámetro. Ten en cuenta que entre dos palabras puede haber más de un blanco.
También al principio y al final de la frase puede haber blancos redundantes.
Por ejemplo, si la cadena es “He estudiado mucho”, debe devolver 3'''
def contar_palabras (frase):
    contador_palabra=0
    contador=0
    while(contador<len(frase)):
        if(frase[contador]!=" " and frase[contador+1]==" "):
            contador_palabra+=1
            contador+=1
        else:
            contador+=1
    return contador_palabra
frase="wenos dias como estais "
numero_palabras=contar_palabras(frase)
print(numero_palabras)
            
            
          
            
            
            