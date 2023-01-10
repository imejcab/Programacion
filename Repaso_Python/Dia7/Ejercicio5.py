'''5. Diseñe un método llamado powerIt que reciba dos enteros y eleve el primero
número al segundo. Puede usar el producto o la recursividad y verificar los valores. Si
no se proporciona ningún exponente, el primer número se eleva a 0.'''
def powerit (numero1=0,numero2=1):
    producto=1
    for i in range (0,numero1):
        producto=producto*numero2
    return producto
numero1=6
numero2=4
producto_numero=powerit(numero1,numero2)
print(producto_numero)

        
    
