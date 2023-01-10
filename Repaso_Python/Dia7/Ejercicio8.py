'''8. Diseñe un método llamado solveSecondOrderEquation que reciba tres enteros
números positivos correspondientes a los coeficientes de una ecuación de segundo orden
(hacha
2+bx+c=0) y calcula sus posibles soluciones. Si los parámetros no son válidos, el
El método debe devolver Ninguno.'''
def solvesecondorderequation (numero1,numero2,numero3):
    resultado_indice_positivo=(-numero2+((numero2**2)-4*numero1*numero3)**0.5)/2*numero1
    resultado_indice_negativo=(-numero2-((numero2**2)-4*numero1*numero3)**0.5)/2*numero1
    return resultado_indice_positivo,resultado_indice_negativo
numero1=2
numero2=5
numero3=9
ecuacion_2_grado=solvesecondorderequation(numero1,numero2,numero3)
print(ecuacion_2_grado)