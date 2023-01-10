'''13. Escribe una función que, dada una lista de nombres y una letra, devuelva una lista
con todos los nombres que empiezan por dicha letra. Debe validar los datos.'''
def identificar_inicial (nombres,letra):
    lista=[]
    for i in nombres:
        if(i[0]==letra):
            lista.append(i)
    return lista
nombres=["andrea","adrian","sofia","claudia","luis","angel"]
letra="a"
lista_letra=identificar_inicial(nombres,letra)
print(lista_letra)