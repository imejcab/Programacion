'''7. Diseñar una función que reciba como parámetro tres cadenas, la primera será una frase y
deberá buscar si existe la palabra que recibe como segundo parámetro y reemplazarla por la
tercera.'''
def sustituir_palabra (frase,palabra1,palabra2):
    contador=0
    contador1=0
    while(contador<len(frase)):
        for i in palabra1[contador1]:
            if(i==frase[contador]):
                contador+=1
                contador1+=1
                if(contador1==len(palabra1)):
                    frase=frase.replace(palabra1,palabra2)
                    contador1=0
            else:
                contador+=1
                contador1=0
    return frase
frase="la vida es bella solo si piensas en positivo"
palabra1="la"
palabra2="ti"
frase_reemplazada=sustituir_palabra(frase,palabra1,palabra2)
print(frase_reemplazada)