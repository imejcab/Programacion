'''10. Diseña una función conversor que convierta un número de binario a decimal o de
decimal a binario. Esta función recibirá un número en formato de cadena de texto
cuya última posición indica el sistema numérico utilizado (D-decimal, B-binario).
Debe validar la información, así, por ejemplo, el número ‘1020101B’ no sería válido
puesto que los valores en binario son 0 y 1.'''
def conversor (cadena_texto):
    sistema_numerico=cadena_texto[-1]
    numeros=int(cadena_texto[0:-1])
    numero_conversor=[]
    contador=-1
    if(cadena_texto[-1]=="B"):
        while(numeros>=2):
            numeros=numeros/2
            if(numeros%2==0):
                numero_conversor[contador].append("0")
                contador-=1
            else:
                numero_conversor[contador].append("1")
                contador-=1
    else:
        contador=-1
        numero_conversor=0
        str(numeros)
        for i in (0,len(numeros)):
            numero_conversor+=int(numeros[contador])**i
            contador-=1
    return numero_conversor
numeros=str(input("Dime un numero de 1 a 10 cifras")
while((len(numeros)<1) or (len(numeros)>10)):
    numeros=int(input("Dime un numero de 1 a 10 cifras")
sistema_numerico=str(input("Dime B o D")).lower()
while(sistema_numerico!="B" and sistema_numerico!="D"):
    sistema_numerico=str(input("Dime B o D")).lower()
cadena_texto=(numeros)+sistema_numerico
if(sistema_numerico=="B"):
    contador=0
    while(contador<len(cadena_texto)-1):
        if(cadena_texto[contador]!=0 and cadena_texto[contador]!=1):
            numeros=int(input("Dime un numero de 1 a 10 cifras")
            while(len(numeros)>0 or len(numeros)<11):
                numeros=int(input("Dime un numero de 1 a 10 cifras")
            sistema_numerico=str(input("Dime B o D")).lower()
            while(sistema_numerico!="B" and sistema_numerico!="D"):
                sistema_numerico=str(input("Dime B o D")).lower()
            cadena_texto=str(numeros)+sistema_numerico
        else:
            contador+=1

                
    
