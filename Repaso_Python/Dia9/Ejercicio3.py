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
def leer_fraccion (numerador,denominador):
    for i in range (1,numerador):
        if(numerador%i==0 and denominador%i==0):
            numerador=numerador/i
            denominador=denominador/i
    fraccion=str(numerador)+"/"+str(denominador)
    return fraccion
numerador=50
denominador=15
f1=leer_fraccion (numerador,denominador)
print(f1)
def escribir_fraccion (numerador,denominador):
    if(denominador==1):
        fraccion=numerador
    else:
        fraccion=str(numerador)+"/"+ str(denominador)
    return fraccion
f2=escribir_fraccion (numerador,denominador)
print(f2)
def calcular_mcd (numerador,denominador):
    contador=numerador
    while(contador>1):
        if(numerador%contador==0 and denominador%contador==0):
            maximo_comun_divisor=contador
            contador=1
        else:
            contador-=1
    return maximo_comun_divisor
f3=calcular_mcd (numerador,denominador)
print(f3)
def simplificar_fraccion (numerador,denominador):
    mcd=calcular_mcd (numerador,denominador)
    numerador=numerador/mcd
    denominador=denominador/mcd
    fraccion=str(numerador)+"/"+str(denominador)
    return fraccion
f4=simplificar_fraccion (numerador,denominador)
print(f4)