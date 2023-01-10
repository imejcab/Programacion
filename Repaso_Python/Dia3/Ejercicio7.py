'''Escribir una función denominada encajan que indique si dos fichas de dominó
encajan o no. Las fichas son recibidas en dos cadenas de texto con el siguiente
formato
[3,4] [2,5]'''
def encajar_piezas (pieza1,pieza2):
    lista_numeros=["0","1","2","3","4","5","6"]
    contador1=0
    contador2=0
    while(contador1<len(pieza1)):
        if(contador1%2==1):
            if(pieza1[contador1]==pieza2[contador2]):
                resultado=True
                contador1=len(pieza1)
            else:
                contador1+=1
                if(contador1==len(pieza1)):
                    contador2+=1
                    contador1=0
                    if(contador2==len(pieza2)):
                        resultado=False
                        contador1=len(pieza1)
        else:
            contador1+=1
            if(contador1==len(pieza1)):
                contador2+=1
                contador1=0
                if(contador2==len(pieza2)):
                    resultado=False
                    contador1=len(pieza1)
    return resultado
pieza1="[3,3]"
pieza2="[3,5]"
fusion_piezas=encajar_piezas(pieza1,pieza2)
if(fusion_piezas==False):
    print(f"Las piezas {pieza1} y {pieza2} no encajan")
else:
    print(f"Las piezas {pieza1} y {pieza2} encajan perfectamente")
    

