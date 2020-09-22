import numpy as np

#MATRIZ COMPARACIÓN ALTERNATIVAS - CRITERIO 1 (ECONÓMICO)

a1 = (1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00, 11.00, 12.00, 13.00, 14.00)
a2 = (a1[0]/a1[1], 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00, 11.00, 12.00, 13.00)
a3 = (a1[0]/a1[2], a2[1]/a2[2], 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00, 11.00, 12.00)
a4 = (a1[0]/a1[3], a2[1]/a2[3], a3[2]/a3[3], 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00, 11.00)
a5 = (a1[0]/a1[4], a2[1]/a2[4], a3[2]/a3[4], a4[3]/a4[4], 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00)
a6 = (a1[0]/a1[5], a2[1]/a2[5], a3[2]/a3[5], a4[3]/a4[5], a5[4]/a5[5], 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00)
a7 = (a1[0]/a1[6], a2[1]/a2[6], a3[2]/a3[6], a4[3]/a4[6], a5[4]/a5[6], a6[5]/a6[6], 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00)
a8 = (a1[0]/a1[7], a2[1]/a2[7], a3[2]/a3[7], a4[3]/a4[7], a5[4]/a5[7], a6[5]/a6[7], a7[6]/a7[7], 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00)
a9 = (a1[0]/a1[8], a2[1]/a2[8], a3[2]/a3[8], a4[3]/a4[8], a5[4]/a5[8], a6[5]/a6[8], a7[6]/a7[8], a8[7]/a8[8], 1.00, 2.00, 3.00, 4.00, 5.00, 6.00)
a10 = (a1[0]/a1[9], a2[1]/a2[9], a3[2]/a3[9], a4[3]/a4[9], a5[4]/a5[9], a6[5]/a6[9], a7[6]/a7[9], a8[7]/a8[9], a9[8]/a9[9], 1.00, 2.00, 3.00, 4.00, 5.00)
a11 = (a1[0]/a1[10], a2[1]/a2[10], a3[2]/a3[10], a4[3]/a4[10], a5[4]/a5[10], a6[5]/a6[10], a7[6]/a7[10], a8[7]/a8[10], a9[8]/a9[10], a10[9]/a10[10], 1.00, 2.00, 3.00, 4.00)
a12 = (a1[0]/a1[11], a2[1]/a2[11], a3[2]/a3[11], a4[3]/a4[11], a5[4]/a5[11], a6[5]/a6[11], a7[6]/a7[11], a8[7]/a8[11], a9[8]/a9[11], a10[9]/a10[11], a11[10]/a11[11], 1.00, 2.00, 3.00)
a13 = (a1[0]/a1[12], a2[1]/a2[12], a3[2]/a3[12], a4[3]/a4[12], a5[4]/a5[12], a6[5]/a6[12], a7[6]/a7[12], a8[7]/a8[12], a9[8]/a9[12], a10[9]/a10[12], a11[10]/a11[12], a12[11]/a12[13], 1.00, 2.00)
a14 = (a1[0]/a1[13], a2[1]/a2[13], a3[2]/a3[13], a4[3]/a4[13], a5[4]/a5[13], a6[5]/a6[13], a7[6]/a7[13], a8[7]/a8[13], a9[8]/a9[13], a10[9]/a10[13], a11[10]/a11[13], a12[11]/a12[13], a13[12]/a13[14], 1.00)

matrixC1 = np.matrix[a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14]
print(matrixC1)