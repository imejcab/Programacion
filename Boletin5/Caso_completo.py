'''JacaGas - Aplicación para el repostaje
La gasolinera del grupo JacaGas, que está al lado del gimnasio JacaFitness, necesita
un programa para gestionar sus cuatro surtidores. Gracias a este programa, podrán
automatizar los procesos que ahora mismo llevan a cabo manualmente y que están
resultando poco eficientes.
Esta aplicación tendrá el menú siguiente:
1. Llenar tanque (diésel o gasolina)
2. Asignar coche a surtidor y repostar
3. Ver puntos de cliente
4. Comprobar histórico de ventas.
5. Consultar estado de surtidores
6. Asignar precio a la gasolina
7. Asignar precio al diésel
8. Cerrar el programa y salir.
Dos de los surtidores son de gasolina (el 1 y el 2) y dos de diésel (el 3 y el 4) y tienen
una capacidad estándar de 5000 litros (5 m3
).
● Cuando se pulse la opción 1, nos deberá preguntar qué cantidad se va añadir al
depósito del surtidor y qué surtidor se va a llenar, y añadir la nueva cantidad a la
cantidad que tiene el depósito del surtidor. No se pueden introducir cantidades
negativas porque no se puede vaciar el surtidor ni exceder la capacidad máxima
(5 m3
).
● Con la opción 2 se deberá preguntar la matrícula del coche (se deberá
comprobar que es el formato adecuado, 4 números y 3 letras), si el coche ya ha
estado en nuestra gasolinera debemos ver si es diésel o gasolina, preguntarle
cuánto dinero quiere gastar en gasolina o diesel (mínimo de 10 euros y cómo
máximo dos decimales) y asignarle el surtidor adecuado.
Al asignar el surtidor (1 o 2 para gasolina y 3 o 4 para diésel) se debe
seleccionar primero aquel que ha distribuido menos combustible.
● Si el coche no ha estado nunca en nuestra gasolinera, debemos preguntar qué
tipo de combustible utiliza (diésel o gasolina) y almacenarlo para no preguntar
más adelante, a continuación pedir la cantidad a repostar y asignar el surtidor
adecuado. Siempre almacenaremos el importe gastado ya que vamos a asignar
puntos según el consumo.
● En la opción 3 se le pedirá al cliente la matrícula de su vehículo y se le informará
de los puntos que tiene, teniendo en cuenta que se da un punto por cada 20
euros de consumo de combustible. Si la matrícula no está registrada se le dirá
que no es un cliente de nuestra gasolinera.
● En la opción 4 se deberá mostrar un listado con todos las matrículas de coches
que han repostado en nuestra gasolinera junto con su consumo.
● En la opción 5 se deberá mostrar la cantidad de gasolina o diésel distribuida por
cada surtidor.
● La opción 6 y 7 servirán para asignar el precio de la gasolina y el diésel. Este
precio es superior a 1 y tiene hasta 3 decimales. Al empezar el programa
también se deberán pedir los precios para poder trabajar con el programa.
● La opción 8 termina la ejecución del programa.'''
precio_diesel=float(input("Dime el precio por litro de diesel"))
precio_diesel=str(precio_diesel)
while(len(precio_diesel)>5 or precio_diesel[1]!="." or precio_diesel[0]=="0"):
    precio_diesel=float(input("Dime el precio por litro de diesel"))
    precio_diesel=str(precio_diesel)
precio_gasolina=float(input("Dime el precio por litro de gasolina"))
precio_gasolina=str(precio_gasolina)
while(len(precio_gasolina)>5 or precio_gasolina[1]!="." or precio_gasolina[0]=="0"):
    precio_gasolina=float(input("Dime el precio por litro de gasolina"))
    precio_gasolina=str(precio_gasolina)
precio_diesel=float(precio_diesel)
precio_gasolina=float(precio_gasolina)
surtidor_gasolina=[1,2]
capacidad_gasolina=[5000,5000]
surtidor_diesel=[3,4]
capacidad_diesel=[5000,5000]
lista_matriculas=[]
tipo_combustible=[]
importe_gastado=[]
gasolina_vendido_surtidor1=0
gasolina_vendido_surtidor2=0
diesel_vendido_surtidor3=0
diesel_vendido_surtidor4=0
numeros=["0","1","2","3","4","5","6","7","8","9"]
letras=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","w","x","y","z"]
opcion=0
while(opcion!=8):
    opcion=int(input("¿Dime que opcion deseas ejecutar?"))
    while(opcion!=1 and opcion!=2 and opcion!=3 and opcion!=4 and opcion!=5 and opcion!=6 and opcion!=7 and opcion!=8):
        opcion=int(input("¿Dime una opcion del 1 al 8 por favor?"))
    if(opcion==1):
        tipo_combustible=str(input("diesel o gasolina")).lower()
        while(tipo_combustible!="diesel" and tipo_combustible!="gasolina"):
            tipo_combustible=str(input("diesel o gasolina")).lower()
        surtidor_elegido=int(input("¿1,2,3 o 4?"))
        while(tipo_combustible=="diesel" and (surtidor_elegido==1 or surtidor_elegido==2)):
            surtidor_elegido=int(input("¿1,2,3 o 4?"))
        while(tipo_combustible=="gasolina" and (surtidor_elegido==3 or surtidor_elegido==4)):
            surtidor_elegido=int(input("¿1,2,3 o 4?"))
        llenar_deposito=int(input("¿Dime cuantos litros de combustible vas a insertar?"))
        if(tipo_combustible=="diesel" and surtidor_elegido==3):
            while(llenar_deposito<=0):
                llenar_deposito=int(input("¿Dime cuantos litros de combustible vas a insertar?"))
            if(llenar_deposito+capacidad_diesel[0]>5000):
                llenar_deposito_real=5000-capacidad_diesel[0]
                capacidad_diesel[0]=5000
                if(llenar_deposito_real!=llenar_deposito):
                    print(f"El deposito esta lleno y hemos insertado {llenar_deposito_real} litros")
            else:
                capacidad_diesel[0]=capacidad_diesel[0]+llenar_deposito
        elif(tipo_combustible=="diesel" and surtidor_elegido==4):
            while(llenar_deposito<=0):
                llenar_deposito=int(input("¿Dime cuantos litros de combustible vas a insertar?"))
            if(llenar_deposito+capacidad_diesel[1]>5000):
                llenar_deposito=5000-capacidad_diesel[1]
                capacidad_diesel[1]=5000
                if(llenar_deposito_real!=llenar_deposito):
                    print(f"El deposito esta lleno y hemos insertado {llenar_deposito_real} litros")
            else:
                capacidad_diesel[1]=capacidad_diesel[1]+llenar_deposito
        elif(tipo_combustible=="gasolina" and surtidor_elegido==1):
            while(llenar_deposito<=0):
                llenar_deposito=int(input("¿Dime cuantos litros de combustible vas a insertar?"))
            if(llenar_deposito+capacidad_gasolina[0]>5000):
                llenar_deposito=5000-capacidad_gasolina[0]
                capacidad_gasolina[0]=5000
                if(llenar_deposito_real!=llenar_deposito):
                    print(f"El deposito esta lleno y hemos insertado {llenar_deposito_real} litros")
            else:
                capacidad_gasolina[0]=capacidad_gasolina[0]+llenar_deposito
        else:
            while(llenar_deposito<=0):
                llenar_deposito=int(input("¿Dime cuantos litros de combustible vas a insertar?"))
            if(llenar_deposito+capacidad_gasolina[1]>5000):
                llenar_deposito=5000-capacidad_gasolina[1]
                capacidad_gasolina[1]=5000
                if(llenar_deposito_real!=llenar_deposito):
                    print(f"El deposito esta lleno y hemos insertado {llenar_deposito_real} litros")
            else:
                capacidad_gasolina[1]=capacidad_gasolina[1]+llenar_deposito
    elif (opcion==2):
        matricula=str(input("Dime la matricula de su vehiculo")).lower()
        contador=0
        contador1=0
        while(contador!=len(matricula)):
            if(len(matricula)!=7):
                matricula=str(input("Dime la matricula de su vehiculo")).lower()
            elif(contador<4):
                while(contador1!=len(numeros)):
                    if(matricula[contador]==numeros[contador1]):
                        contador+=1
                        contador1=0
                        if(contador==4):
                            contador1=len(numeros)
                    else:
                        contador1+=1
                        if(contador1==len(numeros)):
                            matricula=str(input("Dime la matricula de su vehiculo")).lower()
                            contador=0
                            contador1=0
            elif(contador>=4 and contador<=7):
                contador1=0
                while(contador1!=len(letras)):
                    if(matricula[contador]==letras[contador1]):
                        contador+=1
                        contador1=0
                        if(contador==7):
                            contador1=len(letras)
                    else:
                        contador1+=1
                        if(contador1==len(letras)):
                            matricula=str(input("Dime la matricula de su vehiculo")).lower()
                            contador=0
                            contador1=0
        contador=0
        if(len(lista_matriculas)==0):
            lista_matriculas.append(matricula)
            combustible=str(input("Dime el tipo de combustible de su coche")).lower()
            while(combustible!="diesel" and combustible!="gasolina"):
                combustible=str(input("Dime el tipo de combustible de su coche")).lower()
            tipo_combustible.append(combustible)
            dinero_combustible=float(input("Dime cuanto dinero quieres gastar"))
            while(float(dinero_combustible)<=10 or float(dinero_combustible)>=500):
                dinero_combustible=float(input("Dime cuanto dinero quieres gastar, minimo 10 euros y maximo 500 por favor.."))
            contador=0
            contador1=0
            dinero_combustible=str(dinero_combustible)
            if(len(dinero_combustible)==4 and dinero_combustible[2]=="."):
                pass
            elif(len(dinero_combustible)==5 and (dinero_combustible[2]=="." or dinero_combustible[3]==".")):
                pass
            elif(len(dinero_combustible)==6 and dinero_combustible[3]=="."):
                pass
            else:
                while(contador!=len(str(dinero_combustible))):
                    if(str(dinero_combustible)[contador]!=numeros[contador1]):
                        contador1+=1
                        if(contador1)==len(numeros):
                            dinero_combustible=float(input("Dime cuanto dinero quieres gastar"))
                            contador1=0
                            contador=0
                    else:
                        contador+=1
            importe_gastado.append(float(dinero_combustible))
            if(combustible=="diesel"):
                litros_consumo=float(dinero_combustible)/float(precio_diesel)
                if((capacidad_diesel[0]>=capacidad_diesel[1]) and (capacidad_diesel[0]>=litros_consumo)):
                    capacidad_diesel[0]-=litros_consumo
                    diesel_vendido_surtidor3+=litros_consumo
                elif((capacidad_diesel[1]>capacidad_diesel[0]) and (capacidad_diesel[1]>=litros_consumo)):
                    capacidad_diesel[1]-=litros_consumo
                    diesel_vendido_surtidor4+=litros_consumo
                else:
                    print("No es posible suministrarle dicha cantidad de combustible, lo sentimos.")
            else:
                litros_consumo=dinero_combustible//precio_gasolina
                if((capacidad_gasolina[0]>=capacidad_gasolina[1]) and (capacidad_gasolina[0]>=litros_consumo)):
                    capacidad_gasolina[0]-=litros_consumo
                    gasolina_vendido_surtidor1+=litros_consumo
                elif((capacidad_gasolina[1]>capacidad_gasolina[0]) and (capacidad_gasolina[1]>=litros_consumo)):
                    capacidad_gasolina[1]-=litros_consumo
                    gasolina_vendido_surtidor2+=litros_consumo
                else:
                    print("No es posible suministrarle dicha cantidad de combustible, lo sentimos.")
        else:
            contador=0
            while(contador!=len(lista_matriculas)):
                if(matricula==lista_matriculas[contador]):
                    dinero_combustible=float(input("Dime cuanto dinero quieres gastar"))
                    while(dinero_combustible<=10):
                        dinero_combustible=float(input("Dime cuanto dinero quieres gastar, minimo 10 euros por favor.."))
                        dinero_combustible=str(dinero_combustible)
                        while((len(dinero_combustible)>7) or (dinero_combustible[-3]!=".")):
                            dinero_combustible=float(input("Dime cuanto dinero quieres gastar"))
                    importe_gastado[contador]+=dinero_combustible
                    if(tipo_combustible[contador]=="diesel"):
                        litros_consumo=dinero_combustible//precio_diesel
                        if((capacidad_diesel[0]>=capacidad_diesel[1]) and (capacidad_diesel[0]>=litros_consumo)):
                            capacidad_diesel[0]-=litros_consumo
                            diesel_vendido_surtidor3+=litros_consumo
                        elif((capacidad_diesel[1]>capacidad_diesel[0]) and (capacidad_diesel[1]>=litros_consumo)):
                            capacidad_diesel[1]-=litros_consumo
                            diesel_vendido_surtidor4+=litros_consumo
                        else:
                            print("No es posible suministrarle dicha cantidad de combustible, lo sentimos.")
                    else:
                        litros_consumo=dinero_combustible//precio_gasolina
                        if((capacidad_gasolina[0]>=capacidad_gasolina[1]) and (capacidad_gasolina[0]>=litros_consumo)):
                            capacidad_gasolina[0]-=litros_consumo
                            gasolina_vendido_surtidor1+=litros_consumo
                        elif((capacidad_gasolina[1]>capacidad_gasolina[0]) and (capacidad_gasolina[1]>=litros_consumo)):
                            capacidad_gasolina[1]-=litros_consumo
                            gasolina_vendido_surtidor2+=litros_consumo
                        else:
                            print("No es posible suministrarle dicha cantidad de combustible, lo sentimos.")
                else:
                    contador+=1
                    if(contador==len(lista_matriculas)):
                        lista_matriculas.append(matricula)
                        combustible=str(input("Dime el tipo de combustible de su coche")).lower()
                        while(combustible!="diesel" and combustible!="gasolina"):
                            combustible=str(input("Dime el tipo de combustible de su coche")).lower()
                        tipo_combustible.append(combustible)
                        dinero_combustible=float(input("Dime cuanto dinero quieres gastar"))
                        while(dinero_combustible<=10):
                            dinero_combustible=float(input("Dime cuanto dinero quieres gastar, minimo 10 euros por favor.."))
                            dinero_combustible=str(dinero_combustible)
                            while((len(dinero_combustible)>7) or (dinero_combustible[-3]!=".")):
                                dinero_combustible=float(input("Dime cuanto dinero quieres gastar"))
                        importe_gastado.append(dinero_combustible)
                        if(combustible=="diesel"):
                            litros_consumo=dinero_combustible//precio_diesel
                            if((capacidad_diesel[0]>=capacidad_diesel[1]) and (capacidad_diesel[0]>=litros_consumo)):
                                capacidad_diesel[0]-=litros_consumo
                                diesel_vendido_surtidor3+=litros_consumo
                            elif((capacidad_diesel[1]>capacidad_diesel[0]) and (capacidad_diesel[1]>=litros_consumo)):
                                capacidad_diesel[1]-=litros_consumo
                                diesel_vendido_surtidor4+=litros_consumo
                            else:
                                print("No es posible suministrarle dicha cantidad de combustible, lo sentimos.")
                        else:
                            litros_consumo=dinero_combustible//precio_gasolina
                            if((capacidad_gasolina[0]>=capacidad_gasolina[1]) and (capacidad_gasolina[0]>=litros_consumo)):
                                capacidad_gasolina[0]-=litros_consumo
                                gasolina_vendido_surtidor1+=litros_consumo
                            elif((capacidad_gasolina[1]>capacidad_gasolina[0]) and (capacidad_gasolina[1]>=litros_consumo)):
                                capacidad_gasolina[1]-=litros_consumo
                                gasolina_vendido_surtidor2+=litros_consumo
                            else:
                                print("No es posible suministrarle dicha cantidad de combustible, lo sentimos.")
    elif(opcion==3):                        
        matricula=str(input("Dime la matricula de su vehiculo")).lower()
        contador=0
        contador1=0
        while(contador!=len(matricula)):
            if(len(matricula)!=7):
                matricula=str(input("Dime la matricula de su vehiculo")).lower()
            elif(contador<4):
                while(contador1!=len(numeros)):
                    if(matricula[contador]==numeros[contador1]):
                        contador+=1
                        contador1=0
                        if(contador==4):
                            contador1=len(numeros)
                    else:
                        contador1+=1
                        if(contador1==len(numeros)):
                            matricula=str(input("Dime la matricula de su vehiculo")).lower()
                            contador=0
                            contador1=0
            elif(contador>=4 and contador<=7):
                contador1=0
                while(contador1!=len(letras)):
                    if(matricula[contador]==letras[contador1]):
                        contador+=1
                        contador1=0
                        if(contador==7):
                            contador1=len(letras)
                    else:
                        contador1+=1
                        if(contador1==len(letras)):
                            matricula=str(input("Dime la matricula de su vehiculo")).lower()
                            contador=0
                            contador1=0                    
        contador=0
        while(contador!=len(lista_matriculas)):
            if(matricula==lista_matriculas[contador]):
                puntos=importe_gastado[contador]//20
                contador=len(lista_matriculas)
                print(f"Usted tiene acumulado {puntos} puntos")
            else:
                contador+=1
                if(contador==len(lista_matriculas)):
                    print("Error la matricula introducida no es cliente de la gasolinera")       
    elif(opcion==4):
        print(lista_matriculas)      
        print(importe_gastado)
    elif(opcion==5):
        print(f"El surtidor 1 ha vendido {gasolina_vendido_surtidor1} litros de gasolina")
        print(f"El surtidor 2 ha vendido {gasolina_vendido_surtidor2} litros de gasolina")
        print(f"El surtidor 3 ha vendido {diesel_vendido_surtidor3} litros de diesel")
        print(f"El surtidor 4 ha vendido {diesel_vendido_surtidor4} litros de diesel")
    elif(opcion==6):
        precio_diesel=float(input("Dime el precio por litro de diesel"))
        precio_diesel=str(precio_diesel)
        while(len(precio_diesel)>5 or precio_diesel[1]!="." or precio_diesel[0]=="0"):
            precio_diesel=float(input("Dime el precio por litro de diesel"))
            precio_diesel=str(precio_diesel)
        precio_diesel=float(precio_diesel)
    elif(opcion==7):
        precio_gasolina=float(input("Dime el precio por litro de gasolina"))
        precio_gasolina=str(precio_gasolina)
        while(len(precio_gasolina)>5 or precio_gasolina[1]!="." or precio_gasolina[0]=="0"):
            precio_gasolina=float(input("Dime el precio por litro de gasolina"))
            precio_gasolina=str(precio_gasolina)
        precio_gasolina=float(precio_gasolina)
    