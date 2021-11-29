# Для более глубокого понимания понятия "Норма",
# вычисли все нормы, которые приведены в учебнике

# Задача 12

import numpy as np
import math



def matrix_norm(matrix, m,n):
    max_row_abs=[]
    sum_row_abs=0
    sum_sqr_row_abs=[]
    for i in range (m):
        for j in range(n):
            sum_row_abs+=abs(matrix[i][j])
    print(f'Норма 1 = {sum_row_abs}')

    for i in range (m):
        for j in range(n):
            sum_row_abs+=(matrix[i][j])**2
    print(f'Норма 2 = {(np.sum(sum_row_abs)**0.5)}')

    
    for i in range(m):
        row_abs = [abs(matrix[i][j]) for j in range(n)]
        max_row_abs.append(sum(row_abs))
    print(f'A = {max(max_row_abs)}')
        
    a = []
    for j in range(n):
        col_abs = [abs(matrix[i][j]) for i in range(m)]
        a.append(sum(col_abs))
    print(f'A = {max(a)}')


A = np.array(([-1, 3, 2],[3, -3, 4],[1, 9, 7]))
 

m,n = A.shape

matrix_norm(A,m,n)