'''1. Escriba un programa en Python para calcular la suma de los dígitos de un número.
2. Escriba un programa en Python para calcular el máximo común divisor (MCD) de dos
enteros positivos
3. Escriba un programa en Python para obtener el mínimo común múltiplo (MCM) de dos
números enteros
4. Escriba un programa en Python que acepte dos números enteros (n e i) y calcule el valor
de n+nn+nnn+....'''
def sumar_digitos (numero):
    numeros=["1","2","3","4","5","6","7","8","9"]
    suma_digitos=0
    for i in numero:
        contador=0
        while(contador<len(numeros)):
            if(i==numeros[contador]):
                suma_digitos+=int(i)
                contador=len(numeros)
            else:
                contador+=1
    return suma_digitos
numero=str(input("Dime un numero"))
suma=sumar_digitos (numero)
print(suma)
def calcular_maximo_comun_divisor (numero1,numero2):
    contador=0
    divisor=numero1-1
    while(contador<numero1):
        if(numero1%divisor==0 and numero2%divisor==0):
            contador=numero1
        else:
            divisor-=1
            contador+=1
    return divisor
numero1=20
numero2=40
maximo_divisor=calcular_maximo_comun_divisor (numero1,numero2)
print(maximo_divisor)
def calcular_minimo_comun_multiplo (numero1,numero2):
    multiplo=numero1-1
    lista_multiplo1=[]
    while(numero1>1):
        if(numero1%multiplo==0):
            numero1=numero1/multiplo
            lista_multiplo1.append(multiplo)
        else:
            multiplo-=1
    multiplo=numero2-1
    lista_multiplo2=[]
    while(numero2>1):
        if(numero2%multiplo==0):
            lista_multiplo2.append(multiplo)
            numero2=numero2/multiplo
        else:
            multiplo-=1
    for i in lista_multiplo1:
        contador=0
        while(contador<len(lista_multiplo2)):
            if(i==lista_multiplo2[contador]):
                minimo_multiplo=i
                contador=len(lista_multiplo2)
            else:
                contador+=1
                if(contador==len(lista_multiplo2)):
                    minimo_multiplo="No tienen multiplos en comun"
    return minimo_multiplo
numero1=50
numero2=15
minimo_comun_multiplo=calcular_minimo_comun_multiplo (numero1,numero2)   
print(minimo_comun_multiplo) 
def sumar_n_por_i (n,i):
    suma_n=0
    valor_inicial=n
    for i in range (1,i):
        n2=n*10+valor_inicial
        suma_n+=n2
        n=n2
    return suma_n
n=6
i=4
calculo_suma=sumar_n_por_i (n,i)
print(calculo_suma)
        
    
        