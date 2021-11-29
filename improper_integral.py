# Задача № 11
'''Для вычисления несобственного интеграла модернизуруем метод Симпсона'''

import math
import numpy as np
import matplotlib.pyplot as plt

def function_graph(function):
    '''Функция, которая рисует графики'''
    fig = plt.subplots()
    x = np.linspace(1, 2)
    plt.plot(x, function(x))
    plt.show()


def simpson(f, x1, x2, n, e):
    '''Функция вычисления интеграла,
    где x1,x2 - границы интегрирования, 
    f - целевая функция, n - разбиение,
    e - шаг, на который отходим от границ интеграирования '''
    a=x1+e
    b=x2
    h=(b-a)/n
    k=0.0
    x=a + h
    for i in range(1,(n//2) + 1):
        k += 4*f(x)
        x += 2*h
    x = a + 2*h
    for i in range(1,n//2):
        k += 2*f(x)
        x += 2*h
    return (h/3)*(f(a)+f(b)+k)


def function(x): 
    return math.log(x)/(1+x**2)


print(simpson(function, 0.0, 1.0, 10000000, 0.000000001))

#print(function(10))
#function_graph(function)


