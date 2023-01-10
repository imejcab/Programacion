'''3. Diseñe un método llamado computeDaysInMonth que devuelva el número de días para
el mes y el año que se reciben como argumentos. Puede utilizar el método
año bisiesto anterior. Si los valores no son válidos, el método debería devolver -1.'''
from Dia7.Ejercicio2 import año_bisiesto
def computedaysinmonth (año,mes):
    verificar_bisiesto=año_bisiesto(año)
    if(verificar_bisiesto==True):
        dias_mes[1]=29
    contador=0
    while(contador<len(mes_año)):
        if(mes_año[contador]==mes):
            dias=dias_mes[contador]
            contador=len(mes_año)
        else:
            contador+=1
            if(contador==len(mes_año)):
                dias=-1
    return dias
mes_año=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
dias_mes=[31,28,31,30,31,30,31,31,30,31,30,31]
año=int(input("¿Dime un año?"))
while(año<0 or año>2023):
    año=int(input("¿Dime un año?"))
mes=str(input("Dime un mes")).lower()
dias_por_mes=computedaysinmonth(año,mes)
print(dias_por_mes)