'''1. Diseñe una función llamada caracteresEnCadena que tenga una cadena de caracteres y un carácter como
parámetros de entrada y devuelve cuántas veces aparece ese carácter en la cadena. Debería
hacer si la cadena y el carácter son minúsculas o mayúsculas.'''
def caracteresencadena (cadena,caracter):
    contador=0
    for i in cadena:
        if(i==caracter):
            contador+=1
    return contador
cadena=str(input("Dime una cadena de caracteres")).lower()
caracter=str(input("Dime un caracter")).lower()
while(len(caracter)!=1):
    caracter=str(input("Dime un caracter")).lower()
cuenta_caracter=caracteresencadena(cadena,caracter)
print(cuenta_caracter)