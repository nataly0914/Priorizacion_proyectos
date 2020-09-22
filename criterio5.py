import numpy as np
import csv
import pandas as pd

m = pd.read_excel('ahp(criterio5).xlsx') #matriz de comparaciones

result1 = m**2
#print(result1)

result2 = result1.sum(1) #suma filas
#print(result2)
result3 = result2.sum(0) #suma columnas
#print(result3)

result4c = result2*(1/result3)
print(result4c)

V5 = np.matrix(result4c).reshape(20, 1)

print('Valores propios', V5) #valores propios V

#CÁLCULO CONSISTENCIA LÓGICA

matrixB = m.sum(0) #suma de cada columna
B = np.matrix(matrixB).reshape(1, 20)
print('matriz B', B) #MATRIZ B

n = np.shape(B)[1] #dimensión (n)

maxVP = B*V5 #valor propio máximo
print("El máximo valor propio es:", maxVP)

indexC = (maxVP - n) / (n-1)
print('CI es', indexC)
indexA = (1.98 * (n-2))/n
print('IA es', indexA)

relationC = indexC / indexA
print(relationC)

if relationC <0.1:
   print("Relación de consistencia adecuada")
else:
   print("Es necesario reevaluar los juicios. Se debe consultar nuevamente a los expertos")
