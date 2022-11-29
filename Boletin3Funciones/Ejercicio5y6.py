'''5. Diseñe una función llamada palíndromo que tenga una cadena de caracteres como parámetro y devuelva
verdadero si es un palíndromo o falso en otro caso. Una palabra es un palíndromo, si se lee el
lo mismo de izquierda a derecha que de derecha a izquierda, ignorando los blancos. Por ejemplo: "anilina" o "el
abad le dio arroz al zorro" Para simplificar el problema, se puede suponer que los caracteres simples
se utilizan, es decir, sin tildes ni diresis.'''
def palindromo (a):
    contador=0
    contador1=-1
    while(contador!=len(a)):
        if(a[contador]=="" and a[contador1]==""):
            contador+=1
            contador1-=1
        elif(a[contador]==" "):
            contador+=1
        elif(a[contador1]==" "):
            contador1-=1
        else:
            if(a[contador]==a[contador1]):
                contador+=1
                contador1-=1
                if(contador==len(a)):
                    resultado=True
            else:
                resultado=False
                contador=len(a)
    return resultado
a="an sdedsna"
reverse=palindromo(a)
print(reverse)
'''6. Realizar una función que busque una palabra escondida dentro de un texto. Por ejemplo, si
la cadena es “shybaoxlna” y la palabra que queremos buscar es “hola”, entonces si se
encontrará y deberá devolver True, en caso contrario deberá devolver False.'''
def whereare (a,b):         
    contador=0
    contadorb=0
    while(contador!=len(a)):
        if(a[contador]==b[contadorb]):
            contador+=1
            contadorb+=1
            if(contadorb==len(b)):
                resultado=True
                contador=len(a)
        else:
            contador+=1
            contadorb=0
            if(contador==len(a)):
                resultado=False
    return resultado
a="codehelloteachertop"
b="helloteacher"
palabra=whereare(a,b)
print(palabra)


            
          
            