'''4. Diseñe un método llamado getDayOfWeek que reciba una lista que contenga tres números enteros
(día, mes y año) y devuelve el día de la semana para esa fecha (lunes,
Martes Miércoles Jueves Viernes Sábado Domingo).
Puede usar el siguiente algoritmo para obtener un número entre 0 (domingo) y 6
(sábado) correspondiente al día de la semana para una fecha dada:
a = (14 - mes) / 12
y = año – un
m = mes + 12 * a – 2
d = (día + y + y/4 - y/100 + y/400 + (31*m)/12) módulo 7'''
def getdayofweek (lista_fecha):
    dias_semana=["Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]
    a = (14 - lista_fecha[1]) / 12
    y = lista_fecha[0] - a
    m = lista_fecha[1] + 12 * a-2
    d = (lista_fecha[2] + y + y/4 - y/100 + y/400 + (31*m)/12) %7
    d=int(d)
    return dias_semana[d]
lista_fecha=[]
dias_mes=[31,28,31,30,31,30,31,31,30,31,30,31]
año=int(input("Dime un año"))
while(año<0 or año>2023):
    año=int(input("Dime un año"))
lista_fecha.append(año)
mes=int(input("Dime un mes"))
while(mes<1 or mes>12):
    mes=int(input("Dime un mes"))
lista_fecha.append(mes)
contador=mes-1
dia=int(input("dime un dia"))
while(dia<0 or dia>dias_mes[contador]):
    dia=int(input("dime un dia"))
lista_fecha.append(dia)
dia_de_la_semana=getdayofweek(lista_fecha)
print(dia_de_la_semana)