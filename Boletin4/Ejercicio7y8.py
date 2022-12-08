'''Figuras:
1. Define una función que calcule el área de un círculo dado su radio.
2. Defina una función que dado el radio de un círculo devuelva su longitud.
3. Función tal que dadas las coordenadas de dos puntos en el plano devuelve su
distancia euclídea. Un punto en el plano tiene dos coordenadas (abscisa y
ordenada), por lo tanto, la entrada a esta función son cuatro valores reales.
4. Función tal que dadas las coordenadas de un triángulo en el plano, nos devuelve
su perímetro.
5. Haciendo uso de la función anterior diseña otra que calcule su área.'''
def area_circulo (radio):
    pi=3.1416
    area=pi*(radio**2)
    return area
radio=4
calcular_area=area_circulo(radio)
print(calcular_area)
def longitud_circulo(radio):
    pi=3.1416
    longitud=2*pi*radio
    return longitud
radio=4
calcular_longitud=longitud_circulo(radio)
print(calcular_longitud)
def distancia_euclidea (abscisa_punto1, abscisa_punto2, ordenada_punto1, ordenada_punto2):
    distancia=(((abscisa_punto1-abscisa_punto2)**2)+((ordenada_punto1-ordenada_punto2))**2)**0.5
    return distancia
abscisa_punto1=2
abscisa_punto2=4
ordenada_punto1=5
ordenada_punto2=1
calcular_distancia=distancia_euclidea(abscisa_punto1, abscisa_punto2, ordenada_punto1, ordenada_punto2)
print(calcular_distancia)
def perimetro_triangulo (lista_coordenadas):
    distancia_punto1a2=(((lista_coordenadas[0]-lista_coordenadas[1])**2)+((lista_coordenadas[3]-lista_coordenadas[4])**2))**0.5
    distancia_punto1a3=(((lista_coordenadas[0]-lista_coordenadas[2])**2)+((lista_coordenadas[3]-lista_coordenadas[5])**2))**0.5
    distancia_punto2a3=(((lista_coordenadas[1]-lista_coordenadas[2])**2)+((lista_coordenadas[4]-lista_coordenadas[5])**2))**0.5
    perimetro=distancia_punto1a2+distancia_punto1a3+distancia_punto2a3
    perimetro=int(perimetro)
    return perimetro
abscisa_punto1=2
abscisa_punto2=4
abscisa_punto3=30
ordenada_punto1=5
ordenada_punto2=1
ordenada_punto3=10
lista_coordenadas=[abscisa_punto1, abscisa_punto2, abscisa_punto3, ordenada_punto1, ordenada_punto2, ordenada_punto3]
calcular_perimetro=perimetro_triangulo(lista_coordenadas)
print(calcular_perimetro)
def area_triangulo (lista_coordenadas):
    distancia_punto2a3=(((lista_coordenadas[1]-lista_coordenadas[2])**2)+((lista_coordenadas[4]-lista_coordenadas[5])**2))**0.5
    perimetro=perimetro_triangulo(lista_coordenadas)
    area=(perimetro-distancia_punto2a3)/2
    return area
calcular_area=area_triangulo(lista_coordenadas)
print(calcular_area)
'''Fechas:
Fechas:
1. Función que dado un instante (horas, minutos y segundos) devuelva el número
de segundos transcurridos desde el inicio de un día hasta ese instante.
2. Crea una función que devuelva la diferencia en segundos entre dos instantes de
tiempo del mismo día. Recibirá como parámetros seis valores, hora, minuto y
segundo de cada uno de los instantes.
3. Escriba un programa Python para convertir segundos a día, hora, minutos y segundos.
4. Escriba un programa Python para calcular el número de días entre dos fechas.'''
def contar_segundos (hora,minuto,segundo):
    numero_segundos=3600*hora+60*minuto+segundo
    return numero_segundos
hora=4
minuto=30
segundo=50
segundos_totales=contar_segundos(hora,minuto,segundo)
print(f"Dicho instante suma {segundos_totales} segundos")
def diferenciar_instantes (lista_instante1,lista_instante2):
    diferencia_segundos=3600*(lista_instante1[0]-lista_instante2[0])+60*(lista_instante1[1]-lista_instante2[1])+(lista_instante1[2]-lista_instante2[2])
    if(diferencia_segundos<0):
        diferencia_segundos=diferencia_segundos*-1
    return diferencia_segundos
hora1=4
hora2=10
minuto1=29
minuto2=30
segundo1=20
segundo2=59
lista_instante1=[hora1,minuto1,segundo1]
lista_instante2=[hora2,minuto2,segundo2]
segundos_diferencia=diferenciar_instantes(lista_instante1,lista_instante2)
print(segundos_diferencia)
def transformar_segundos(segundos_totales):
    if(segundos_totales>=60):
        segundos=segundos_totales%60
        minutos_totales=segundos_totales//60
        if(minutos_totales>=60):
            minutos=minutos_totales%60
            horas=minutos_totales//60
        else:
            horas=0
            minutos=0        
    else:
        horas=0
        minutos=0
        segundos=segundos_totales  
    return horas, minutos, segundos
segundos_totales=20000
datos=transformar_segundos(segundos_totales)
horas_total=datos[0]
minutos_total=datos[1]
segundos_total=datos[2]     
print(f"Si han pasado {segundos_totales} segundos tenemos: \n {horas_total} horas \n {minutos_total} minutos \n {segundos_total} segundos")
def diferenciar_dias (fecha1,fecha2):
    contador=0
    dias_totales_fecha1=0
    while(contador!=len(mes)):
        if(fecha1[1]==mes[contador]):
            dias_totales_fecha1+=fecha1[2]
            contador=len(mes)
        else:
            dias_totales_fecha1+=dias_mes[contador]
            contador+=1
    dias_totales_fecha2=0
    contador=0
    while(contador!=len(mes)):
        if(fecha2[1]==mes[contador]):
            dias_totales_fecha2+=fecha2[2]
            contador=len(mes)
        else:
            dias_totales_fecha2+=dias_mes[contador]
            contador+=1
    diferencia_años=fecha1[0]-fecha2[0]
    diferencia_dias=diferencia_años*360+(dias_totales_fecha1-dias_totales_fecha2)
    if(diferencia_años<0):
        diferencia_años=fecha2[0]-fecha1[0]
        diferencia_dias=diferencia_años*360+(dias_totales_fecha2-dias_totales_fecha1)
    return diferencia_dias
mes=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]   
dias_mes=[31,28,31,30,31,30,31,31,30,31,30,31]
fecha1=[] 
fecha2=[]
año1=int(input("Dime un año"))
while(año1<0 or año1>2030):
    año1=int(input("Dime un año"))
fecha1.append(año1)
año2=int(input("Dime un año"))
while(año2<0 or año2>2030):
    año2=int(input("Dime un año"))
fecha2.append(año2)
mes1=str(input("Dime un mes")).lower()
contador=0
while(contador!=len(mes)):
    if(mes1==mes[contador]):
        contador=len(mes)
    else:
        contador+=1
        if(contador==len(mes)):
            mes1=str(input("Dime un mes")).lower()
            contador=0
fecha1.append(mes1)   
mes2=str(input("Dime un mes")).lower()
contador=0
while(contador!=len(mes)):
    if(mes2==mes[contador]):
        contador=len(mes)
    else:
        contador+=1
        if(contador==len(mes)):
            mes2=str(input("Dime un mes")).lower()
            contador=0
fecha2.append(mes2)        
dia1=int(input("Dime un numero del 1 al 31"))
contador=0
while(contador!=len(dias_mes)):
    if(mes1==mes[contador]):
        if(dia1<=dias_mes[contador] and dia1>0):
            contador=len(dias_mes)
        else:
            dia1=int(input("Dime un numero del 1 al 31"))
            contador=0
    else:
        contador+=1
fecha1.append(dia1)
dia2=int(input("Dime un numero del 1 al 31"))
contador=0
while(contador!=len(dias_mes)):
    if(mes2==mes[contador]):
        if(dia2<=dias_mes[contador] and dia2>0):
            contador=len(dias_mes)
        else:
            dia2=int(input("Dime un numero del 1 al 31"))
            contador=0
    else:
        contador+=1
fecha2.append(dia2)
dias_entrefechas=diferenciar_dias (fecha1,fecha2)
print(f"La diferencia de dias entre {fecha1} y {fecha2} son {dias_entrefechas} dias")
    



