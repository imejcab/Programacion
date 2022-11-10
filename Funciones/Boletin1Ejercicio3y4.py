'''Realiza un programa que solicite la fecha como tres datos numéricos (día, mes y
año) y muestre a continuación la fecha en formato largo.
Introduce el día de la fecha: 15
Introduce el mes de a fecha: 3
Introduce el año de a fecha: 2009
La fecha en formato largo es 15 de Marzo de 2009
Debe validar los datos y ejecutarse hasta que se introduzca un día negativo.'''
dia=int(input("¿dime un dia?"))
while(dia>0):
    while(dia>31):
        dia=int(input("¿dime un dia?"))
    mes=str(input("¿Dime un mes?"))
    while(mes!="Enero" and mes!="Febrero" and mes!="Marzo" and mes!="Abril" and mes!="Mayo" and mes!="Junio" and mes!="Julio" and mes!="Agosto" and mes!="Septiembre" and mes!="Octubre" and mes!="Noviembre" and mes!="Diciembre"):
        mes=str(input("¿Dime un mes?"))
    año=int(input("¿dime un año?"))
    while(año<0 or año>2023):
        año=int(input("¿dime un año?"))
    while((mes=="Abril" and dia==31) or (mes=="Junio" and dia==31) or (mes=="Mayo" and (dia>28 and dia<=31)) or (mes=="Septiembre" and dia==31) or (mes=="Noviembre" and dia==31)):
        dia=int(input("¿dime un dia?"))
        while(dia>31):
            dia=int(input("¿dime un dia?"))
        mes=str(input("¿Dime un mes?"))
        while(mes!="Enero" and mes!="Febrero" and mes!="Marzo" and mes!="Abril" and mes!="Mayo" and mes!="Junio" and mes!="Julio" and mes!="Agosto" and mes!="Septiembre" and mes!="Octubre" and mes!="Noviembre" and mes!="Diciembre"):
            mes=str(input("¿Dime un mes?"))
        año=int(input("¿dime un año?"))
        while(año<0 or año>2023):
            año=int(input("¿dime un año?"))
    print(f"La fecha en formato largo es {dia} de {mes} de {año}")
    dia=int(input("¿dime un dia?"))
#EJERCICIO 4
'''Crea un programa que lea por teclado números de forma sucesiva y los guarde en
una lista; el proceso de lectura y guardado finalizará cuando metamos un número
negativo. En ese momento se mostrará el elemento mayor y los números pares.'''
def elementomayor (i):
    i1=0
    if(i>i1):
        i1=i
    return i1
def contarpares (i):
    if(i%2==0):
        return i
lista=[]
numero=0
while(numero>=0):
    numero=int(input("¿Dime un numero?"))
    if(numero>=0):
        lista.append(numero)
print(lista)
for i in lista:
    mayor=elementomayor(i)
    pares=contarpares(i)
    print(f"El numero {mayor} es el mayor")
    print(f"El numero {pares} es par")

        
        

            