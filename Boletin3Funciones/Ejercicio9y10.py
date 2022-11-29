'''9. Crear una función que, tomando una cadena de texto como entrada, construya y devuelva
otra cadena formada de la siguiente manera: el método debe colocar todas las consonantes
al principio y todas las vocales al final de la misma, eliminando los blancos.
Por ejemplo, pasándole la cadena "curso de programacion", una posible solución sería
"crsdprgrmcnuoeoaaio'''
def consovocal (frase):
    vocal=["a","e","i","o","u"]
    lista=[]
    contador=0
    while(contador!=len(frase)):
        if(frase[contador] not in vocal and frase[contador]!=" "):
            lista.append(frase[contador])
            contador+=1
        else:
            contador+=1
    contador=0
    while(contador!=len(frase)):
        if(frase[contador]) in vocal:
            lista.append(frase[contador])
            contador+=1
        else:
            contador+=1
    return lista
frase="curso de programacion"
cadenaconsovocal=consovocal(frase)
print(cadenaconsovocal)
cadena=""
for i in cadenaconsovocal:
    cadena+=i
print(cadena)
'''10. Escribir una función que, devuelva el número de palabras que hay en una cadena que recibe
como parámetro. Ten en cuenta que entre dos palabras puede haber más de un blanco.
También al principio y al final de la frase puede haber blancos redundantes.
Por ejemplo, si la cadena es “He estudiado mucho”, debe devolver 3'''
def countword (frase):
    contador=0
    acumulador=0
    while(contador!=len(frase)):
        if(frase[contador]!=" "):
            contador+=1
            if(contador==len(frase)and (frase[contador-1]!=" ")):
                contador-=1
            if (contador==len(frase)-1) and (frase[contador]!=" "):
                acumulador+=1
                contador+=1
            elif(frase[contador]==" "):
                acumulador+=1
        else:
            contador+=1
    return acumulador
frase="  Deseando superar  el siguiente boletin "
palabras=countword(frase)
print(f"Esta frase tiene {palabras} palabras")
        
            
        