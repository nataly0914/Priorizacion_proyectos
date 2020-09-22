import numpy as np
import pandas as pd


#MATRIZ COMPARACIÓN CRITERIOS
c1 = (1, 1.00, 2.00, 3.00, 4.00, 6.00, 7.00)
c2 = (c1[0]/c1[1], 1, 1.00, 2.00, 3.00, 4.00, 6.00)
c3 = (c1[0]/c1[2], c2[1]/c2[2], 1, 1.00, 2.00, 3.00, 4.00)
c4 = (c1[0]/c1[3], c2[1]/c2[3], c3[2]/c3[3], 1, 1.00, 2.00, 3.00)
c5 = (c1[0]/c1[4], c2[1]/c2[4], c3[2]/c3[4], c4[3]/c4[4], 1, 1.00, 2.00)
c6 = (c1[0]/c1[5], c2[1]/c2[5], c3[2]/c3[5], c4[3]/c4[5], c5[4]/c5[5], 1, 1.00)
c7 = (c1[0]/c1[6], c2[1]/c2[6], c3[2]/c3[6], c4[3]/c4[6], c5[4]/c5[6], c6[5]/c6[6], 1)

matrix = np.matrix([c1, c2, c3, c4, c5, c6, c7])
#print(matrix)


result1 = matrix**2 #matriz cuadrada
result2 = result1.sum(1) #dimensión filas
result3 = result2.sum(0) #dimensión columnas

result4 = result2*(1/result3) # VALORES PROPIOS
print('Los valores propios son:', result4)

matrixB = matrix.sum(0)
#print(matrixB)
n = np.linalg.matrix_rank(matrix)
#print(n)

maxVP = matrixB*result4 # valor propio máximo
print(maxVP)

indexC = (maxVP - n) / (n-1)
print('El índice CI es:', float(indexC))

def indexA(n1):
    indexAA ={2:0, 3:0.58, 4:0.9, 5:1.12, 6:1.24, 7:1.32, 8:1.41, 9:1.45, 10:1.49}
    return indexAA[n1]

#print(type(indexC))
print('El índice RI es:', indexA(7))
relationC = indexC / indexA(7)
print(relationC)

if relationC <0.1:
    print("Relación de consistencia adecuada")
else:
    print("Es necesario reevaluar los juicios. Se debe consultar nuevamente a los expertos")

#####EXPORTAR EN EXCEL#######
matrixC = pd.DataFrame(matrix)
matrixC.to_excel('matrizC.xlsx')

#####EXPORTAR EN EXCEL#######
matrixValores = pd.DataFrame(result4)
matrixValores.to_excel('matrizValores.xlsx')
