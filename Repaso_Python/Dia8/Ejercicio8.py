'''8. Diseñar una función que determine la cantidad de vocales diferentes, que tiene una palabra
o frase introducida por teclado. Por ejemplo, la cadena “Abaco”, devolvería 2.'''
def contar_vocal (palabra):
    vocal=["a","e","i","o","u"]
    contador_vocal=0
    for i in vocal:
        contador=0
        while(contador<len(palabra)):
            if(i==palabra[contador]):
                contador_vocal+=1
                contador=len(palabra)
            else:
                contador+=1
    return contador_vocal
palabra="velociraptor"
numero_vocales=contar_vocal(palabra)
print(numero_vocales)
                
                
                
        