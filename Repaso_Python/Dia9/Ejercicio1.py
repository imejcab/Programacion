'''1. Diseña un programa que permite guardar el nombre de usuario y contraseña de
hasta 10 usuarios diferentes. Si el usuario ya existe en el sistema, puede hacer
login tras incluir un usuario y contraseña válidas hasta un máximo de tres
intentos, momento en el que se bloquea su cuenta.
Si el usuario no existe, puede crear una cuenta siempre que haya espacio
(máximo 10), para lo que se le pedirá usuario y contraseña, así como la
confirmación de ésta última.
El menú de este programa permitirá identificarse y crear cuentas nuevas, así
como mostrar todos los nombres de usuario existentes sin sus contraseñas.'''
def ingresar_sistema (usuario,contraseña,lista_usuarios,lista_contraseñas,lista_bloqueos):
    if(len(lista_usuarios)<10):
        if (len(lista_usuarios)==0):
            lista_usuarios.append(usuario)
            lista_contraseñas.append(contraseña)
            lista_bloqueos.append("no")
        else:
            contador=0
            while(contador<len(lista_usuarios)):
                if(usuario==lista_usuarios[contador]):
                    contador=len(lista_usuarios)
                else:
                    contador+=1
                    if(contador==len(lista_usuarios)):
                        lista_usuarios.append(usuario)
                        lista_contraseñas.append(contraseña)
                        lista_bloqueos.append("no")
    return lista_usuarios
lista_usuarios=[]
lista_contraseñas=[]
lista_bloqueos=[]
contador=0
error=0
usuario="s"
while(usuario!=" "):
    usuario=str(input("Dime un nombre de usuario"))
    contraseña=str(input("Dime una contraseña"))
    for i in lista_usuarios:
        if(i==usuario):
            while(contador<len(lista_contraseñas)):
                if(contraseña==lista_contraseñas[contador]):
                    contador=len(lista_contraseñas)
                else:
                    contador+=1
                    if(contador==len(lista_contraseñas)):
                        contraseña=str(input("Dime de nuevo una contraseña"))
                        error+=1
                        if(error==3):
                            lista_bloqueos[contador]=lista_bloqueos[contador].replace("no","si")
                            contador=len(lista_contraseñas)
                        contador=0
    login_usuario=ingresar_sistema (usuario,contraseña,lista_usuarios,lista_contraseñas,lista_bloqueos)
    print(login_usuario)       
    print(lista_contraseñas)
    print(lista_bloqueos)    
                        

    