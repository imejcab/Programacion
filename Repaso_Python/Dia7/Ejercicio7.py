'''7. Diseñe un método llamado isPrime que reciba un número entero positivo mayor
que 0 como parámetro. El método debe devolver True si el número es primo o False si
no primo Si el parámetro no es válido, el método debe devolver Ninguno.'''
def isprime (numero):
    es_primo=True
    '''for i in range (2,numero):
        if(numero%i==0):
            es_primo=False'''
    contador=2
    while(contador<numero):
        if(numero%contador==0):
            es_primo=False
            contador=numero
    return es_primo
numero=int(input("Dime un numero positivo"))
while(numero<=0):
    numero=int(input("Dime un numero positivo"))
numero_primo=isprime(numero)
print(numero_primo)
