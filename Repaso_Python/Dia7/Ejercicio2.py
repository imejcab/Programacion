'''2. Diseñe un método llamado esAñoBisiesto que reciba un número y devuelva Falso para
años comunes y True para años bisiestos. Usted puede saber que un año se considera
ser un año bisiesto si es divisible por 4, a menos que también sea divisible por 100. Un año no es un
año bisiesto si es divisible por 100 a menos que también sea divisible por 400.'''
def año_bisiesto (numero):
    if((numero%4==0 and numero%100!=0) or (numero%4==0 and numero%100==0 and numero%400==0)):
        año_bisiesto=True
    else:
        año_bisiesto=False
    return año_bisiesto
numero=400
verificar_bisiesto=año_bisiesto(numero)
print(verificar_bisiesto)