# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def main(xi,yi):
    qtd = len(xi)
    tx = total(xi)
    ty = total(yi)

    xy = list()
    x2 = list()
    for i in xrange(0, qtd):
        xy.append(xi[i] * yi[i])
        x2.append(xi[i] ** 2.0)

    txy = total(xy)
    tx2 = total(x2)

    d = tx / qtd
    e = ty / qtd
    a1 = ((qtd*txy) - (tx*ty)) / ((qtd*tx2) - (tx**2))
    a0 = e - (a1 * d)

    print 'a1 =',a1
    print 'a0 =',a0

    y = list()
    for i in xrange(0, qtd):
        y.append(a1*xi[i]+a0)

    plt.plot(range(1,qtd+1), yi, 'bo')
    plt.plot(range(1,qtd+1), y)

def total(lst):
    total = float()
    for i in lst:
        total += i
    return total

if __name__ == '__main__':
    plt.title('Minimos Quadrados')
    plt.grid(True)
    plt.axis([-2, 8, -2, 8])
    plt.plot([-100,100],[0,0], 'k-') # Linha X
    plt.plot([0,0],[-100,100], 'k-') # Linha Y

    fl = open('input-mq.txt', 'r')
    x = [float(i) for i in fl.readline().split(' ')]
    y = [float(i) for i in fl.readline().split(' ')]
    fl.close()

    if len(x) == len(y):
        main(x,y)
        plt.show()
    else:
        print 'Valores de X e Y precisam ter a mesma quantidade.'
