'''3. Diseñar una función llamada upperCaseInString que tenga como parámetro una cadena de caracteres, la
El método debe devolver cuántos de esos caracteres son letras mayúsculas.'''
def uppercaseinstring (cadena):
    contador=0
    for i in cadena:
        if(i.isupper()):
            contador+=1
    return contador
cadena=str(input("Dime una cadena de caracteres"))
contar_mayusculas=uppercaseinstring(cadena)
print(contar_mayusculas)