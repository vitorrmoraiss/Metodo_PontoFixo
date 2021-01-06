# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 19:27:56 2019

"""

#################### MÉTODO PONTO FIXO ####################

import numpy as np
import matplotlib.pyplot as pyplot

#função pro usuario digitar a função
def eval_f(fx,x):
    return eval(fx)

#função pra plotar grafico 
def plot(fx, gx,glx, a, b):
    xx=np.linspace (a,b)
    pyplot.plot(xx, eval_f(fx,xx), label='f(x)')
    pyplot.plot(xx, eval_f(gx,xx), label='g(x)')
    pyplot.plot(xx, eval_f(glx,xx), label='glx(x)')
    pyplot.grid()
    pyplot.show()
    
    

def ponto_fixo (gx, a, b, tol, n):
    x=(a+b)/2
    for i in range(n):
        xant = x
        x = eval_f(gx, x)
        erro = abs((x-xant)/max(1,x))
        print(i, xant, x, erro)
        if fx == 0 or erro < tol:
            break 
        
fx = input('f(x):')
gx = input('g(x):')
glx = input('glx(x):')

plot(fx, gx, glx, -10,5) #Intervalos 
ponto_fixo(gx, -10, 5, 10*-5, 20) #Precisao e interacoes 

    