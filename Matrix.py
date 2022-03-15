# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 17:02:23 2022
You are given two matrices A & B of same size, 
return another matrix which is the sum of A and B.
@author: MMEENAK4
"""

def sumMatrices(A, B):
    n = len(A)
    m = len(A[0])
    result = []
    diff = []
    for row in range(n):
        result_row = []
        diff_row = []
        for col in range(m):
            result_row.append(A[row][col] + B[row][col])
            diff_row.append(A[row][col] - B[row][col])
        result.append(result_row)
        diff.append(diff_row)
    return diff

A = [[0, 1, 2],[3, 4, 5],[7, 8, 9]]
B = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]
A = [[1, 1]]               
B = [[2, 3]]
print(sumMatrices(A,B))

"""
Created on Thu Jan 20 17:02:23 2022
You are given a 2D integer matrix A, 
return a 1D integer vector containing column-wise sums of original matrix.
@author: MMEENAK4
"""

def colsumMatrix(A):
    n = len(A)
    m = len(A[0])
    col_sum = []
    for col in range(m):
        sum = 0
        for row in range(n):
            sum += A[row][col]
        col_sum.append(sum)
    return col_sum

A = [[1,2,3,4],[5,6,7,8],[9,2,3,4]]
print(colsumMatrix(A))
"""
Created on Thu Jan 20 17:02:23 2022
You are given a 2D integer matrix A, 
return a 1D integer vector containing column-wise sums of original matrix.
@author: MMEENAK4
"""

def rowsumMatrix(A):
    n = len(A)
    m = len(A[0])
    row_sum = []
    for row in range(n):
        sum = 0
        for col in range(m):
            sum += A[row][col]
        row_sum.append(sum)
    return row_sum

A = [[1,2,3,4],[5,6,7,8],[9,2,3,4]]
print(rowsumMatrix(A))
"""
Created on Thu Jan 20 17:02:23 2022
You are given two integer matrices A(having M X N size) and B(having N X P).
multiply matrix A with B and return the resultant matrix. (i.e. return the matrix AB).
@author: MMEENAK4
"""

def matrixMult(A, B):
        M = len(A)
        N = len(A[0])
        P = len(B[0])
    
        C = []
        
        for i in range(0, M):
            C.append([0] * P)
    
        for i in range(0, M):
            for j in range(0, P):
                for k in range(0, N):
                    C[i][j] += A[i][k] * B[k][j]
    
        return C
    
   

A = [[1, 2, 3], [4, 5, 6]]            
B = [[10, 11], [20, 21], [30, 31]] 
print(matrixMult(A,B))

"""
given a matrix A, you have to return another matrix which is the transpose of A.

"""

def tranposeMatrix(A):
    ans = []
    for i in range(0,len(A[0])):
        temp = []
        for j in range(0,len(A)):
            temp.append(A[j][i])
        ans.append(temp)
    return ans

A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
tranposeMatrix(A)
"""
Created on Thu Jan 20 17:02:23 2022
Give a N * N square matrix A, return an array of its anti-diagonals. 
@author: MMEENAK4
"""

def print_antidiagonal(A):
    n = len(A)
    N = 2 * n - 1
 
    result = []
     
    for i in range(N) :
        result.append([])
     
    # Push each element in the result vector
    for i in range(n) :
        for j in range(n) :
            result[i + j].append(A[i][j])
    for i in range((2*n)-1):
            while len(result[i]) < n:
                result[i].append(0)
    return result
    
    
    
A =[[1,2,3],[4,5,6],[7,8,9]]
print(print_antidiagonal(A))

"""
Created on Thu Jan 20 17:02:23 2022
given a matrix A and and an integer B, 
perform scalar multiplication of matrix A with an integer B.
@author: MMEENAK4
"""

def scalarMult(A, B):
    n = len(A)
    m = len(A[0])
    result = []
    for i in range(n):
        result_row = []
        for j in range(m):
            result_row.append(A[i][j]*B)   
        result.append(result_row)
    return result
    
    
    
A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
B = 2 
print(scalarMult(A,B))

"""
given two two matrices A & B of equal sizes 
check whether two matrices are equal or not.
"""


def matEqual(A, B):
    n = len(A)
    m = len(A[0])
    for i in range(n): 
        for j in range(m):
            if(A[i][j] != B[i][j]):
                return 0
    return 1

A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
B = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
B = [[1, 2, 3],[7, 8, 9],[4, 5, 6]]
print(matEqual(A,B))

"""
given a N X N integer matrix. find the sum of all the main diagonal elements of A.
Main diagonal of a matrix A is a collection of elements A[i, j] such that i = j.
"""


def maiDiagSum(A):
    n = len(A)
    m = len(A[0])
    sum = 0
    for i in range(n): 
        for j in range(m):
            if i == j:
                sum += A[i][j]
    return sum

A = [[1, -2, -3],[-4, 5, -6],[-7, -8, 9]]
print(maiDiagSum(A))

"""
find the sum of all the minor diagonal elements of A.
"""

def printDiagonalSums(A):
    n = len(A)
    principal = 0
    secondary = 0
    for i in range(0, n):
        principal += A[i][i]
        secondary += A[i][n - i - 1]
    return secondary

A = [[1, -2, -3],[-4, 5, -6],[-7, -8, 9]]
printDiagonalSums(A)

"""
given a 2D integer matrix A, make all the elements in a row or column zero if the A[i][j] = 0.
Specifically, make entire ith row and jth column zero.
"""
def convert(A):
 
    # base case
    if not A or not len(A):
        return
 
    (M, N) = (len(A), len(A[0]))
 
    rowFlag = colFlag = False
 
    # scan the first row for any 0's
    for j in range(N):
        if A[0][j] == 0:
            rowFlag = True
            break
 
    # scan the first column for any 0's
    for i in range(M):
        if A[i][0] == 0:
            colFlag = True
            break
 
    # process the rest of the Arix and use the first row and the
    # first column to mark if any cell in the corresponding
    # row or column has a value 0 or not
    for i in range(1, M):
        for j in range(1, N):
            if A[i][j] == 0:
                A[0][j] = A[i][0] = 0
 
    # if `(0, j)` or `(i, 0)` is 0, assign 0 to cell `(i, j)`
    for i in range(1, M):
        for j in range(1, N):
            if A[0][j] == 0 or A[i][0] == 0:
                A[i][j] = 0
 
    # if `rowFlag` is true, then assign 0 to all cells of the first row
    i = 0
    while rowFlag and i < N:
        A[0][i] = 0
        i = i + 1
 
    # if `colFlag` is true, then assign 0 to all cells of the first column
    i = 0
    while colFlag and i < M:
        A[i][0] = 0
        i = i + 1
        
    return A

A = [[1,2,3,4],[5,6,7,0],[9,2,0,4]]
print(convert(A))