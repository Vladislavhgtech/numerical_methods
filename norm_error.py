# Задача №13
import numpy as np
import math

"В условии задачи дана вычисленная векторная норма ||x||inf=max(xi), "
"поэтому посчитаем подчинённую матричную норму ||x||inf"


def matrix_norm(matrix, m,n):
    '''Фукция вычисления норм'''
    max_row_abs=[]
    for i in range(m):
        row_abs = [abs(matrix[i][j]) for j in range(n)]
        max_row_abs.append(max(row_abs))
    return max(max_row_abs)

def relative_error(matrix, f, norm_df):
    '''Функция вычисления погрешности'''
    m,n = matrix.shape
    m1,n1=f.shape
    
    #Вычиляем обратную матрицу с помощью numpy
    inverse_matrix_A=np.linalg.inv(matrix)
    m2,n2=inverse_matrix_A.shape

    # Вычисляем нормы
    norm_A=matrix_norm(matrix,m,n)
    norm_f=matrix_norm(f,m1,n1)
    norm_inv_mat_A=matrix_norm(inverse_matrix_A, m2,n2)

    # Вычисляем Мю
    m=norm_A*norm_inv_mat_A
    
    print(f'Оценка относительной погрешности:   {m*norm_df/norm_f}')

    
    
def run():
    A= np.array(([-7, -3, -8],[6, -6, -8],[-5, 1, -3]))
    f=np.array(([-7.1, 7.2, 6.7],))
    norm_df=0.6
    relative_error(A, f, norm_df)
        
    
run()














