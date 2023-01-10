'''4. Crea un programa que lea por teclado números de forma sucesiva y los guarde en
una lista; el proceso de lectura y guardado finalizará cuando metamos un número
negativo. En ese momento se mostrará el elemento mayor y los números pares.'''
def mostrar_mayor (lista):
    numero_mayor=0
    for i in lista:
        if(i>=numero_mayor):
            numero_mayor=i
    return numero_mayor   
def mostrar_pares (lista):
    for i in lista:
        if(i%2==1):
            lista.remove(i)
    return lista
lista=[]
numero=0
while(numero>=0):
    numero=int(input("Dime numeros y negativo para parar"))
    if(numero>=0):
        lista.append(numero)
lista_mayor=mostrar_mayor(lista)
print(lista_mayor)
lista_par=mostrar_pares(lista)
print(lista_par)
    