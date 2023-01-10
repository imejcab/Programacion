'''1. Diseñe un método llamado computaFactorial que reciba un entero positivo y
devuelve el factorial para ese número. Si el número es negativo, el método debe
devuelve Ninguno.'''
def computa_factorial (numero):
    contador=numero
    factorial=1
    if(numero<0):
        factorial="Ninguno"
    else:
        while(contador>0):
            factorial=factorial*contador
            contador-=1
    return factorial
numero=-2
numero_factorizado=computa_factorial(numero)
print(numero_factorizado)
