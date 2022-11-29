'''7. Diseñar una función que reciba como parámetro tres cadenas, la primera será una frase y
deberá buscar si existe la palabra que recibe como segundo parámetro y reemplazarla por la
tercera'''
def reemplazopalabra (a,b,c):
    contador=0
    contadorb=0
    while(contador!=len(a)):
        if(a[contador]==b[contadorb]):
            contador+=1
            contadorb+=1
            if(contadorb==len(b)):
                a=a.replace(b,c)
                contador+=1
                contadorb=0
        else:
            contador+=1
            contadorb=0
    return a        
a="Hola,Buenas Jose dias Jose"
b="Jose"
c="Señor"
reemplazar=reemplazopalabra(a,b,c)
print(reemplazar)
'''8. Diseñar una función que determine la cantidad de vocales diferentes, que tiene una palabra
o frase introducida por teclado. Por ejemplo, la cadena “Abaco”, devolvería 2.'''
def countvocal (frase):
    contador=0
    contador1=0
    lista=[]
    vocal=["a","e","i","o","u"]
    while(contador!=len(frase)):
        if(vocal[contador1])==frase[contador]:
            if(frase[contador] not in lista):
                lista.append(frase[contador])
                contador1+=1
            else:
                contador1+=1        
        else:
            contador1+=1
        if(contador1==len(vocal)):
                    contador+=1
                    contador1=0
    resultado=len(lista)
    return resultado
frase="HOLA mundo".lower()
contar_vocal=countvocal(frase)
print(f"Tenemos {contar_vocal} vocales diferentes")
            
            
        
        
        