'''6. Diseñe un método llamado getNumberOfDigits que reciba un número (puede ser
real, entero, positivo o negativo) y debe devolver el número de dígitos que contiene. Si
el parámetro no es válido, el método debería devolver Ninguno. Extender esta función a
otros sistemas numéricos (hexadecimal, decimal, binario, octal).'''
def getnumberofdigits (numero):
    numeros=["0","1","2","3","4","5","6","7","8","9"]
    digitos=0
    for i in numero:
        contador=0
        while(contador<len(numeros)):
            if(i==numeros[contador]):
                contador=len(numeros)
                digitos+=1
            else:
                contador+=1
    return digitos
numero="23.455666"
numero_digitos=getnumberofdigits(numero)
print(f"El numero de digitos de {numero} es {numero_digitos}")
                    
                    
                