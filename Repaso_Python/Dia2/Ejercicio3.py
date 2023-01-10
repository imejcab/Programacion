'''Realiza un programa que solicite la fecha como tres datos numéricos (día, mes y
año) y muestre a continuación la fecha en formato largo.
Introduce el día de la fecha: 15
Introduce el mes de a fecha: 3
Introduce el año de a fecha: 2009
La fecha en formato largo es 15 de Marzo de 2009
Debe validar los datos y ejecutarse hasta que se introduzca un día negativo.'''
def imprimir_fecha_formato_largo ():
    lista_mes=[30,29,28,31,30,30,31,30,30,31,31,31]    
    mes=int(input("Dime un mes del 1 al 12"))
    while(mes<1 or mes>12):
        mes=int(input("Dime un mes del 1 al 12"))
    dia=int(input("Dime un dia del 1 al 31"))
    while(dia>lista_mes[mes]):
        dia=int(input("Dime un dia del 1 al 31"))
    año=int(input("Dime un año de 0 a 2022"))
    while(año<0 or año>2022):
        año=int(input("Dime un año de 0 a 2022"))
    return dia,mes,año
lista_meses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
dia=0
while(dia>=0):
    datos=imprimir_fecha_formato_largo ()
    dia=datos[0]
    mes=datos[1]
    año=datos[2]
    if(dia>=0):
        print(f"La fecha en formato largo es {dia} de {lista_meses[mes-1]} del {año}")
    


