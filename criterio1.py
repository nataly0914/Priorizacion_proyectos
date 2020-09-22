import numpy as np
import csv
import pandas as pd

m = pd.read_excel('ahp(criterio1).xlsx') #matriz de comparaciones
#m = pd.read_excel('ahp(criterio2).xlsx') #matriz de comparaciones
#m = pd.read_excel('ahp(criterio3).xlsx') #matriz de comparaciones
#m = pd.read_excel('ahp(criterio4).xlsx') #matriz de comparaciones
#m = pd.read_excel('ahp(criterio5).xlsx') #matriz de comparaciones
#m = pd.read_excel('ahp(criterio6).xlsx') #matriz de comparaciones
#m = pd.read_excel('ahp(criterio7).xlsx') #matriz de comparaciones

result1 = m**2
#print(result1)

result2 = result1.sum(1) #suma filas
#print(result2)
result3 = result2.sum(0) #suma columnas
#print(result3)

result4c = result2*(1/result3)
print(result4c)
V1 = np.matrix(result4c).reshape(20, 1)
#V2 = np.matrix(result4c).reshape(20, 1)
#V3 = np.matrix(result4c).reshape(20, 1)
#V4 = np.matrix(result4c).reshape(20, 1)
#V5 = np.matrix(result4c).reshape(20, 1)
#V6 = np.matrix(result4c).reshape(20, 1)
#V7 = np.matrix(result4c).reshape(20, 1)

print('Valores propios', V1) #valores propios V

#CÁLCULO CONSISTENCIA LÓGICA

matrixB = m.sum(0) #suma de cada columna
B = np.matrix(matrixB).reshape(1, 20)
print('matriz B', B) #MATRIZ B

n = np.shape(B)[1] #dimensión (n)

maxVP = B*V1 #valor propio máximo
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

from matrices import (result4)
from criterio2 import V2
from criterio3 import V3
from criterio4 import V4
from criterio5 import V5
from criterio6 import V6
from criterio7 import V7

print(result4)

matrixV = np.concatenate([V1, V2, V3, V4, V5, V6, V7]).reshape(20, 7)
print(matrixV)

#####EXPORTAR EN EXCEL#######
matrixVectores = pd.DataFrame(matrixV)
matrixVectores.to_excel('matrizV.xlsx')

matrixD = np.dot(matrixV, result4)
print('La matriz de decisión es:', matrixD)
print(max(matrixD))

#####EXPORTAR EN EXCEL#######
matrixDecision = pd.DataFrame(matrixD)
matrixDecision.to_excel('matrizD.xlsx')
