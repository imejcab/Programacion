'''10. Diseñe un método llamado isFriendNumber que reciba dos números positivos y
devuelve True si los números son amigos, False en caso contrario. dos numeros son
considerados amigos si la suma de sus divisores, excepto el número dado, es igual
al segundo y viceversa.'''
def isfriendnumber (numero1,numero2):
    suma_divisores=0
    es_amigo=False
    for i in range (1,numero1+1):
        if(numero1%i==0):
            suma_divisores+=i
    if(suma_divisores==numero2):
        es_amigo=True
    return es_amigo
numero1=6
numero2=12
numero_amigo=isfriendnumber(numero1,numero2)
print(numero_amigo)

            
