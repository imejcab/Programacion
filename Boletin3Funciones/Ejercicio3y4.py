'''3. Diseñar una función llamada upperCaseInString que tenga como parámetro una cadena de caracteres, la
El método debe devolver cuántos de esos caracteres son letras mayúsculas.'''
def uppercaseinstring (a):
    contador=0
    mayusculas=0
    while(contador!=len(a)):
        if(a[contador].isupper()):
            mayusculas+=1
            contador+=1
        else:
            contador+=1
    return mayusculas
a="HGVguvtGVg65VFCf"
contador_mayusculas=uppercaseinstring (a)
print(contador_mayusculas)
'''4. Diseñar una función llamada numeroEnCadena que tenga como parámetro una cadena de caracteres, la
El método debe devolver cuántos de esos caracteres son números.'''
def numeroencadena (a):
    contador=0
    numeros=0
    while(contador!=len(a)):
        if(a[contador].isnumeric()):
            numeros+=1
            contador+=1
        else:
            contador+=1
    return numeros
a="g2g82GG2744428"
contar_numeros=numeroencadena(a)
print(contar_numeros)
        