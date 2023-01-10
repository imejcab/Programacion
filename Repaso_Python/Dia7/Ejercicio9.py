'''9. Diseñe un método llamado getPrimeDivisors que reciba un número positivo como
parámetro y devuelve una lista que contiene sus divisores primos. Si el parámetro no es válido
el método debe devolver Ninguno.'''
def get_prime_divisors (numero):
    lista=[]
    if(numero>=0):
        for i in range (1,numero):
            if(numero%i==0):
                numero_primo=True
                for x in range (2,i):
                    if(i%x==0):
                        numero_primo=False
                if(numero_primo==True):
                    lista.append(i)
    else:
        lista="Ninguno"
    return lista
numero=25
divisores_primos=get_prime_divisors (numero)
print(divisores_primos)