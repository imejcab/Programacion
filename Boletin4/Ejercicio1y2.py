#USUARIOS
'''1. Diseña un programa que permite guardar el nombre de usuario y contraseña de
hasta 10 usuarios diferentes. Si el usuario ya existe en el sistema, puede hacer
login tras incluir un usuario y contraseña válidas hasta un máximo de tres
intentos, momento en el que se bloquea su cuenta.
Si el usuario no existe, puede crear una cuenta siempre que haya espacio
(máximo 10), para lo que se le pedirá usuario y contraseña, así como la
confirmación de ésta última.
El menú de este programa permitirá identificarse y crear cuentas nuevas, así
como mostrar todos los nombres de usuario existentes sin sus contraseñas.'''
#lista_reg_usuarios=[[" "," ","0"]],[[" "," ","0"]],[[" "," ","0"]],[[" "," ","0"]],[[" "," ","0"]],[[" "," ","0"]],[[" "," ","0"]],[[" "," ","0"]],[[" "," ","0"]],[[" "," ","0"]]
lista_reg_usuarios=[]
lista_contraseñas=[]
intentos_fallidos=["0","0","0","0","0","0","0","0","0","0"]
def registrar_sistema (usuario,contraseña):
    contador=0
    if(len(lista_reg_usuarios)<10) and (len(lista_reg_usuarios)>0):
            while(contador!=len(lista_reg_usuarios)):
                if(usuario!=lista_reg_usuarios[contador]):
                    contador+=1
                    if(contador==len(lista_reg_usuarios)):
                        lista_reg_usuarios.append(usuario)
                        lista_contraseñas.append(contraseña)
                        contador=len(lista_reg_usuarios)
                else:
                    contador=len(lista_reg_usuarios)
    elif(len(lista_reg_usuarios)==0):
        lista_reg_usuarios.append(usuario)
        lista_contraseñas.append(contraseña)
    return lista_reg_usuarios
def entrada_sistema ():
    contador=0
    contador_error=0
    bloqueo=0
    usuario=str(input("¿Dime un usuario?"))
    contraseña=str(input("¿Dime una contraseña?"))
    if(len(lista_reg_usuarios)>0) and (len(lista_reg_usuarios)<=10):
        while(contador!=len(lista_reg_usuarios)):
            if(usuario!=lista_reg_usuarios[contador]):
                contador+=1
                if(contador==len(lista_reg_usuarios)):
                    contraseña_verificar=str(input("¿Dime de nuevo tu contraseña?"))
                    while(contraseña_verificar!=contraseña):
                        contraseña_verificar=str(input("¿Dime de nuevo tu contraseña?"))
            else:
                if(intentos_fallidos[contador]=="0"):
                    if(contraseña==lista_contraseñas[contador]):
                        contador=len(lista_reg_usuarios)
                    else:
                        while(contraseña!=lista_contraseñas[contador]):
                            contador_error+=1
                            if(contador_error==3):
                                bloqueo+=1
                                intentos_fallidos[contador].replace("0","1")
                                contraseña=lista_contraseñas[contador]
                            else:
                                contraseña=str(input("¿Dime una contraseña?"))
                else:
                    print("Cuenta bloqueada")
    elif(len(lista_reg_usuarios)==0):
        contraseña_verificar=str(input("¿Dime de nuevo tu contraseña?"))
        while(contraseña_verificar!=contraseña):
            contraseña_verificar=str(input("¿Dime de nuevo tu contraseña?"))
    return usuario,contraseña
opcion=0
while(opcion!=1): 
    datos=entrada_sistema()
    usuario=datos[0]   
    contraseña=datos[1]
    resultado=registrar_sistema(usuario,contraseña)
    print(resultado)
    opcion=int(input("Dime 1 si quieres parar de insertar usuarios o cualquier otro numero para seguir"))
'''Cálculo:
1. Escriba un programa en Python para calcular la suma de los dígitos de un número.
'''
#1
def sumadigitos (numero):    
    acumulador_suma=0
    contador=0
    contador1=0
    contador_digitos=0
    numeros=["0","1","2","3","4","5","6","7","8","9"]
    numeross=[0,1,2,3,4,5,6,7,8,9]
    while(contador!=len(numero)):
        while(contador1!=len(numeros)):
            if(numeros[contador1]==numero[contador]):
                acumulador_suma+=(numeross[contador1])
                contador_digitos+=1
                contador+=1
                contador1=0
                if(contador==len(numero)):
                    contador1=len(numeros)
            else:
                contador1+=1
                if(contador1==len(numeros)):
                    contador+=1
                    contador1=0
                    if(contador==len(numero)):
                        contador1=len(numeros)
                    
    return contador_digitos,acumulador_suma
numero=" 3,333"
datos=sumadigitos(numero)
digitos=datos[0]
suma=datos[1]
print(f"El numero tiene {digitos} digitos")
print(f"La suma de los digitos da {suma}")
        
        
        
        
    
                    
           
            
        
        
        