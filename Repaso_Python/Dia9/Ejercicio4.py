'''6. Crear un programa que utilizando las funciones anteriores muestre el siguiente
menú:
a. Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el
resultado.
b. Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la
resta.
c. Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra el
producto.
d. Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra la
cociente.
e. Salir

v. sumar_fracciones: recibe dos funciones n1/d1 y n2/d2 y calcula su suma. La
suma de dos fracciones es otra fracción cuyo numerador n=n1*d2+d1*n2 y
denominador d=d1*d2, simplificando la fracción resultado.
vi. restar_fracciones: resta dos fracciones, siendo el numerador de la resta
n=n1*d2-d1*n2 y el denominador d=d1*d2, simplificando el resultado.
vii. multiplicar_fracciones: recibe dos fracciones y calcula su producto, siendo el
numerador del producto n=n1*n2 y el denominador d=d1*d2 (simplificando).
viii. dividir_fracciones: calcula el cociente de dos fracciones, siendo el numerador
n=n1*d2 y denominador d=d1*n2 (simplificando el resultado)
'''
def sumar_fracciones (n1,n2,d1,d2):
    n=n1*d2+d1*n2
    d=d1*d2
    contador=n
    while(contador>1):
        if(n%contador==0 and d%contador==0):
            n=n/contador
            d=d/contador
            contador=n
        else:
            contador-=1
    fraccion=str(n)+"/"+str(d)
    return fraccion
def restar_fracciones (n1,n2,d1,d2):
    n=n1*d2-d1*n2
    d=d1*d2
    contador=n
    while(contador>1):
        if(n%contador==0 and d%contador==0):
            n=n/contador
            d=d/contador
            contador=n
        else:
            contador-=1
    fraccion=str(n)+"/"+str(d)
    return fraccion
def multiplicar_fracciones (n1,n2,d1,d2):
    n=n1*n2
    d=d1*d2
    contador=n
    while(contador>1):
        if(n%contador==0 and d%contador==0):
            n=n/contador
            d=d/contador
            contador=n
        else:
            contador-=1
    fraccion=str(n)+"/"+str(d)
    return fraccion
def dividir_fracciones (n1,n2,d1,d2):
    n=n1*d2
    d=d1*n2
    contador=n
    while(contador>1):
        if(n%contador==0 and d%contador==0):
            n=n/contador
            d=d/contador
            contador=n
        else:
            contador-=1
    fraccion=str(n)+"/"+str(d)
    return fraccion
n1=2
n2=12
d1=6
d2=3
print("*************MENU*************\nOpcion 1:Sumar fracciones\nOpcion 2: Restar fracciones\nOpcion 3:Multiplicar fracciones\nOpcion 4:Dividir fracciones\nOpcion 5:Salir")
opcion=0
while(opcion!=5):
    opcion=int(input("Dime un numero del 1 al 5 referente a la opcion elegida y mostrada en el menu anterior"))
    while(opcion<1 or opcion>5):
        opcion=int(input("Dime una opcion valida"))
    if(opcion==1):
        suma=sumar_fracciones (n1,n2,d1,d2)
        print(suma)
    elif(opcion==2):
        resta=restar_fracciones (n1,n2,d1,d2)
        print(resta)
    elif(opcion==3):
        multiplicar=multiplicar_fracciones (n1,n2,d1,d2)
        print(multiplicar)
    elif(opcion==4):
        dividir=dividir_fracciones (n1,n2,d1,d2)
        print(dividir)
        