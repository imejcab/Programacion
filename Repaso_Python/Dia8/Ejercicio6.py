'''6. Realizar una función que busque una palabra escondida dentro de un texto. Por ejemplo, si
la cadena es “shybaoxlna” y la palabra que queremos buscar es “hola”, entonces si se
encontrará y deberá devolver True, en caso contrario deberá devolver False.'''
def encontrar_palabra (cadena,palabra):
    recorrido_palabra=0
    for i in palabra:
        contador=0
        while(contador<len(cadena)):
            if(i!=cadena[contador]):
                contador+=1
                if(contador==len(cadena)):
                    palabra_encontrada=False
            else:
                recorrido_palabra+=1
                contador=len(cadena)
                if(recorrido_palabra==len(palabra)):
                    palabra_encontrada=True
                    contador=len(cadena)
    return palabra_encontrada
cadena="Hola wenos dias"
palabra="lewass"
palabra_en_cadena=encontrar_palabra(cadena,palabra)
print(palabra_en_cadena)
