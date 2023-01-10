'''5. Diseñe una función llamada palíndromo que tenga una cadena de caracteres como parámetro y devuelva
verdadero si es un palíndromo o falso en otro caso. Una palabra es un palíndromo, si se lee el
lo mismo de izquierda a derecha que de derecha a izquierda, ignorando los blancos. Por ejemplo: "anilina" o "el
abad le dio arroz al zorro" Para simplificar el problema, se puede suponer que los caracteres simples
se utilizan, es decir, sin tildes ni diresis.'''
def palindromo (cadena):
    contador=-1
    contador1=0
    palindromo=False
    while(contador>-len(cadena)):
        if(cadena[contador]==cadena[contador1]):
            contador-=1
            contador1+=1
            if(contador==-len(cadena)):
                palindromo=True
        else:
            contador=-len(cadena)
    return palindromo
cadena="aserejeresa"
es_palindromo=palindromo(cadena)
print(es_palindromo)
    