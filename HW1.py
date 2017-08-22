# This Python file uses the following encoding: utf-8
import os, sys
import numpy as np
def gaussJordan(myMatrix):
    mInv = np.linalg.inv(myMatrix) # Se regresa la matriz inversa obtenida
    return mInv


def lookMax(A, n):
    for i in range(0, n):
        # Se busca el maximo elemento dentro de la matriz, así como la fila pertenicente a este elemento
        maxElement = abs(A[i][i])
        maxRow = i
        for k in range(i+1, n):
            if abs(A[k][i]) > maxElement:
                maxElement = abs(A[k][i])
                maxRow = k

        swapMax(A, maxRow, i)

def swapMax(A,maxRow, i):
    # Se hace un swap de la fila máxima por la fila actual(dejando la matriz en la forma Escalonada)
    for k in range(i, n + 1):
        tmp = A[maxRow][k]
        A[maxRow][k] = A[i][k]
        A[i][k] = tmp

def reduceMatrix(A, i):
    # Todas las filas debajo o encima del pivote, deben quedar igualadas a 0, dejando la matriz de forma reducida escalonada
    for k in range(i + 1, n):
        c = -A[k][i] / A[i][i]
        for j in range(i, n + 1):
            if i == j:
                A[k][j] = 0
            else:
                A[k][j] += c * A[i][j]

def gauss(A):
    n = len(A)

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]/A[i][i]
        for k in range(i-1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x

def main():
    f = open("matrix.txt", "r")  # Se abre un archivo txt con el nombre matrix
    n = int(f.readline()) # Se cre
    str = ""
    for line in f:
        str+=(line) #Se declara un string para ir almacenando cada linea del archivo leido
        str.replace(",","") #Se sutituye las comasp


    myMatrix = np.matrix(str) # Se crea un np matrix de la librería de Numpy para obtener el determinante de la matriz
    print(myMatrix)
    det = np.linalg.det(myMatrix)
    if(det<.1 and det>-.1):
        print("Es una matriz singular")
    else:
        print("Matriz invertible")
        m = np.ndarray.tolist(myMatrix)
        print(gaussJordan(myMatrix))


if __name__ == '__main__':
    main()
'''
Archivo con la matriz esperada
4
20, 17, 11, 12;
3, 0, 9, 16;
1, 4 ,19, 65;
112, 2, 4, 9
'''

