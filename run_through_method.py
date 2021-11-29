# Задача 16

import numpy as np

# Проверка достаточных условий 
def test_dd(X):
    D = np.diag(np.abs(X)) # Поиск диагональных коэффициентов
    print(D)
    S = np.sum(np.abs(X), axis=1) - D # Find row sum without diagonal
    if np.all(D > S):
        print ('Диагонально доминирующая матрица')
        return True
    else:
        print ('НЕ диагонально доминирующая матрица')
        return False



# Решение СЛАУ методом прогонки
def RTM(a,b):
    if(not test_dd(a)):
        print('Ошибка исходных данных')
        return -1
    
    n=len(a)
    x=[0 for k in range(0,n)] #обнуление вектора решений
    print('Размерность матрицы:',n,'x',n)

    #прямой ход
    v=[0 for k in range(0,n)]
    u=[0 for k in range(0,n)]

    # для перевой строки 
    v[0]=a[0][1] / (-a[0][0])
    u[0]=(-b[0])/(-a[0][0])

    for i in range(1,n-1):
        v[i]=a[i][i+1]/(-a[i][i]-a[i][i-1]*v[i-1])
        u[i]= (a[i][i-1]*u[i-1]-b[i])/(-a[i][i]-a[i][i-1]*v[i-1])

    v[n-1]=0
    u[n-1]=(a[n-1][n-2]*u[n-2]-b[n-1])/(-a[n-1][n-1]-a[n-1][n-2]*v[n-2])

    print(f'Прогоночные коэффициенты: alfa={v} , beta={u}')

    #обратный ход

    x[n-1]=u[n-1]
    for i in range(n-1,0,-1):
        x[i-1]=v[i-1]*x[i]+u[i-1]
    return x


A=np.array([[-11, -7, 0, 0, 0], [7, 10, -1, 0, 0], [0,-10,20,6,0], [0,0,10,18,-7],[0,0,0,6, -13]])
B = np.array([-1,4,5,6,-9])

test_dd(A)



#вызов функции и вывод на экран
print(A)
print(B)
print(RTM(A,B))

print(f'Проверка решения с помощью встроенной функции: {np.linalg.inv(A).dot(B)}')