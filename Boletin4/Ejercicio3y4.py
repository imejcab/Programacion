'''2. Escriba un programa en Python para calcular el máximo común divisor (MCD) de dos
enteros positivos
3. Escriba un programa en Python para obtener el mínimo común múltiplo (MCM) de dos
números enteros'''
def maxdivisor (numero1,numero2):
    contador=1
    lista_divisores=[]
    while((contador<=numero1) and (contador<=numero2)):
        if(numero1%contador==0 and numero2%contador==0):
            lista_divisores.append(contador)
            contador+=1
        else:
            contador+=1
    return lista_divisores[-1]
def min_multiplo (numero1,numero2):
    contador=1
    contador1=1
    contador2=0
    lista_acumulador1=[]
    acumulador1=numero1*contador
    lista_acumulador1.append(acumulador1)
    contador+=1
    acumulador2=numero2*contador1
    contador1+=1
    if(acumulador1<numero2):
        contador1=1
    while(contador2!=len(lista_acumulador1)):
        if(acumulador2==lista_acumulador1[contador2]):
            contador2=len(lista_acumulador1)
            contador1=len(lista_acumulador1)
        else:
            contador2+=1
            if(contador2==len(lista_acumulador1)):
                acumulador1=numero1*contador
                lista_acumulador1.append(acumulador1)
                contador+=1
                acumulador2=numero2*contador1
                contador1+=1
                if(acumulador1<numero2):
                    contador1=1
                contador2=0
    return acumulador2
numero1=45
numero2=12
max_comun_divisor=maxdivisor(numero1,numero2)    
print(max_comun_divisor)   
min_comun_multiplo=min_multiplo(numero1,numero2)
print(min_comun_multiplo)