'''9. Crear una función que, tomando una cadena de texto como entrada, construya y devuelva
otra cadena formada de la siguiente manera: el método debe colocar todas las consonantes
al principio y todas las vocales al final de la misma, eliminando los blancos.
Por ejemplo, pasándole la cadena "curso de programacion", una posible solución sería
"crsdprgrmcnuoeoaaio'''
def modificar_texto (texto):
    vocal=["a","e","i","o","u"]
    lista=[]
    for i in texto:
        if(i!="a" and i!="e" and i!="i" and i!="o" and i!="u"):
            lista.append(i)
    for i in texto:
        for x in vocal:
            if(i==x):
                lista.append(i)
    return lista
texto="La vida da mas vueltas de la que te imaginas".lower()
texto_ordenado=modificar_texto(texto)
print(texto_ordenado)
for i in texto_ordenado:
    print(i)