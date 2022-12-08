'''4. Escriba un programa en Python que acepte dos números enteros (n e i) y calcule el valor
de n+nn+nnn+....
n = 2, i = 3
resultado = 2 + 22 + 222 = 246
n = 1, i = 5
resultado = 1 + 11 + 111 + 1111+ 11111 = 12345'''
def calcular_formula (n,i):
    contador=1
    acumulador=1
    n_new=0
    n_total=n
    resultado=n
    while(contador!=i):
        acumulador=acumulador*10
        n_new=n*acumulador
        n_total+=n_new
        resultado+=n_total
        contador+=1
    return resultado
n=1
i=5
valor=calcular_formula (n,i)
print(valor)
'''5. Queremos crear un programa que trabaje con fracciones de la forma a/b. Para
representar una fracción vamos a utilizar dos enteros: numerador y denominador,
creando las siguientes funciones para trabajar con ellas:
i. leer_fracción: La tarea de esta función es leer por teclado el numerador y el
denominador y la devuelve simplificada (Por ejemplo, si recibe 16/6 ⇒ 8/3)
ii. escribir_fracción: muestra por pantalla la fracción; si el denominador es 1, se
muestra sólo el numerador.
iii. calcular_mcd: Esta función recibe dos números y devuelve su máximo común
divisor.
iv. simplificar_fracción: simplifica una fracción. Para ello hay que dividir el
numerador y denominador por su MCD.
v. sumar_fracciones: recibe dos funciones n1/d1 y n2/d2 y calcula su suma. La
suma de dos fracciones es otra fracción cuyo numerador n=n1*d2+d1*n2 y
denominador d=d1*d2, simplificando la fracción resultado.
vi. restar_fracciones: resta dos fracciones, siendo el numerador de la resta
n=n1*d2-d1*n2 y el denominador d=d1*d2, simplificando el resultado.
vii. multiplicar_fracciones: recibe dos fracciones y calcula su producto, siendo el
numerador del producto n=n1*n2 y el denominador d=d1*d2 (simplificando).
viii. dividir_fracciones: calcula el cociente de dos fracciones, siendo el numerador
n=n1*d2 y denominador d=d1*n2 (simplificando el resultado)'''
def leer_fraccion (a,b):
    contador=2
    while(contador<=a and contador<=b):
        if(a%contador==0 and b%contador==0):
            a=a/contador
            b=b/contador
            contador=2
        else:
            contador+=1
    a=str(a)
    b=str(b)
    c=a+"/"+b
    return c
a=16
b=6
fraccion_simpl=leer_fraccion(a,b)
print(fraccion_simpl)
def escribir_fraccion (a,b):
    if(b==1):
        c=a
    else:
        a=str(a)
        b=str(b)
        c=a+"/"+b
    return c
a=23
b=4
mostrar_fracc=escribir_fraccion(a,b)
print(mostrar_fracc)
def calcular_mcd (a,b):
    if(a>=b):
        contador=b
    else:
        contador=a
    while(contador>=1):
        if(a%contador==0 and b%contador==0):
            mcd=contador
            contador=0
        else:
            contador-=1
    return mcd
a=30
b=2
valor_mcd=calcular_mcd(a,b)
print(valor_mcd)    
def simplificar_fraccion (a,b): 
    if(a%valor_mcd==0 and b%valor_mcd==0):
        a=a/valor_mcd
        b=b/valor_mcd
        a=str(a)
        b=str(b)
        c=a+"/"+b
    else:
        a=str(a)
        b=str(b)
        c=a+"/"+b
    return c
a=20
b=16
simpli_fracc_mcd=simplificar_fraccion(a,b)
print(simpli_fracc_mcd)
def suma_fracciones (a1,a2,b1,b2):
    a1=int(a1)
    a2=int(a2)
    b1=int(b1)
    b2=int(b2)
    numerador=(a1*b2)+(a2*b1)
    denominador=(a2*b2)
    contador=2
    while(contador<=numerador and contador<=denominador):
        if(numerador%contador==0 and denominador%contador==0):
            numerador=numerador/contador
            denominador=denominador/contador
            contador=2
        else:
            contador+=1
    numerador=str(numerador)
    denominador=str(denominador)
    fraccion=numerador+"/"+denominador
    return fraccion
def resta_fracciones (a1,a2,b1,b2):
    a1=int(a1)
    a2=int(a2)
    b1=int(b1)
    b2=int(b2)
    numerador=(a1*b2)-(a2*b1)
    denominador=(a2*b2)
    contador=2
    while(contador<=numerador and contador<=denominador):
        if(numerador%contador==0 and denominador%contador==0):
            numerador=numerador/contador
            denominador=denominador/contador
            contador=2
        else:
            contador+=1
    numerador=str(numerador)
    denominador=str(denominador)
    fraccion=numerador+"/"+denominador
    return fraccion
def multiplicar_fracciones (a1,a2,b1,b2):
    a1=int(a1)
    a2=int(a2)
    b1=int(b1)
    b2=int(b2)
    numerador=a1*b1
    denominador=a2*b2
    contador=2
    while(contador<=numerador and contador<=denominador):
        if(numerador%contador==0 and denominador%contador==0):
            numerador=numerador/contador
            denominador=denominador/contador
            contador=2
        else:
            contador+=1
    numerador=str(numerador)
    denominador=str(denominador)
    fraccion=numerador+"/"+denominador
    return fraccion
def dividir_fracciones (a1,a2,b1,b2):
    a1=int(a1)
    a2=int(a2)
    b1=int(b1)
    b2=int(b2)
    numerador=a1*b2
    denominador=a2*b1
    contador=2
    while(contador<=numerador and contador<=denominador):
        if(numerador%contador==0 and denominador%contador==0):
            numerador=numerador/contador
            denominador=denominador/contador
            contador=2
        else:
            contador+=1
    numerador=str(numerador)
    denominador=str(denominador)
    fraccion=numerador+"/"+denominador
    return fraccion
a1="4"
a2="6"
b1="2"
b2="5"
suma=suma_fracciones(a1,a2,b1,b2)
print(suma)
resta=resta_fracciones(a1,a2,b1,b2)
print(resta)
multiplicar=multiplicar_fracciones(a1,a2,b1,b2)
print(multiplicar)
dividir=dividir_fracciones(a1,a2,b1,b2)
print(dividir)
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
e. Salir'''
def calculo_fraccion (a1,a2,b1,b2):
    contador=0
    while(contador!=1):
        if(opcion=="a"):
            resultado=suma_fracciones(a1,a2,b1,b2)
            contador=1
        elif(opcion=="b"):
            resultado=resta_fracciones(a1,a2,b1,b2)
            contador=1
        elif(opcion=="c"):
            resultado=multiplicar_fracciones(a1,a2,b1,b2)
            contador=1
        elif(opcion=="d"):
            resultado=dividir_fracciones(a1,a2,b1,b2)
            contador=1
    return resultado
opcion=str(input("Dime la letra a,b,c,d,o e segun su interes"))
while(opcion!="a" and opcion!="b" and opcion!="c" and opcion!="d" and opcion!="e"):
        opcion=str(input("Dime de nuevo una letra a,b,c,d,o e segun su interes"))
a1="8"
a2="3"
b1="5"
b2="10"
valor=calculo_fraccion(a1,a2,b1,b2)
print(valor)
while(opcion!="e"):
    opcion=str(input("Dime la letra a,b,c,d,o e segun su interes"))
    while(opcion!="a" and opcion!="b" and opcion!="c" and opcion!="d" and opcion!="e"):
        opcion=str(input("Dime de nuevo una letra a,b,c,d,o e segun su interes"))
    valor=calculo_fraccion(a1,a2,b1,b2)
    print(valor)
#PREGUNTAR A JOSE PORQUE LA LLAMADA A UNA FUNCION DESDE OTRO MODULO NO FUNCIONA

    
    