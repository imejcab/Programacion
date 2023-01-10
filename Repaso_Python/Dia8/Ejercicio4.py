'''4. Diseñar una función llamada numeroEnCadena que tenga como parámetro una cadena de caracteres, la
El método debe devolver cuántos de esos caracteres son números.'''
def numeroencadena (cadena):
    contador=0
    for i in cadena:
        if(i.isnumeric()):
            contador+=1
    return contador
cadena="ngrjn434635j"
contar_numeros=numeroencadena(cadena)
print(contar_numeros)
