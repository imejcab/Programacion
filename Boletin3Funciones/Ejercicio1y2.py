'''1. Diseñe una función llamada caracteresEnCadena que tenga una cadena de caracteres y un carácter como
parámetros de entrada y devuelve cuántas veces aparece ese carácter en la cadena. Debería
hacer si la cadena y el carácter son minúsculas o mayúsculas.'''
def caracteresencadena (a,b):
    contador=0
    acumulador=0
    while(contador!=len(a)):
        if(b==a[contador]):
            contador+=1
            acumulador+=1
        else:
            contador+=1
    return acumulador
a="hvtyfyiug444".lower()
b="Y".lower()
contador_numero=caracteresencadena (a,b)
print(contador_numero)
'''2. Diseñe una función llamada lowCaseInString que tenga como parámetro una cadena de caracteres, la
El método debe devolver cuántos de esos caracteres son letras minúsculas.'''
def LOWcaseinstring (a):
    contador=0
    minusculas=0
    while(contador!=len(a)):
        if(a[contador].islower()):
            minusculas+=1
            contador+=1
        else:
            contador+=1
    return minusculas
a="HGVguvtGVg65VFCf"
contador_mayusculas=LOWcaseinstring (a)
print(contador_mayusculas)
#OPCION 2
def lowcaseinstring (a,lista):
    contador=0
    acumulador=0
    while(contador!=len(a)):
        if(a[contador]) in lista:
            contador+=1
            acumulador+=1
        else:
            contador+=1
    return acumulador
a="HY7TVhyttttttttvYvY74"
lista=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
contador_minusculas=lowcaseinstring(a,lista)
print (contador_minusculas)    
            