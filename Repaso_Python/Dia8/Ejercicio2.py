'''2. Diseñe una función llamada lowCaseInString que tenga como parámetro una cadena de caracteres, la
El método debe devolver cuántos de esos caracteres son letras minúsculas.'''
def lowcaseinstring (cadena):
    contador=0
    for i in cadena:
        if (i.islower()):
            contador+=1
    return contador
cadena=str(input("Dime una cadena de caracteres"))
contar_minusculas=lowcaseinstring(cadena)
print(contar_minusculas)