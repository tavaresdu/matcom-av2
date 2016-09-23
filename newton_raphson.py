# -*- coding: utf-8 -*-

def main(f, x):
    fd = derivada(f)

    is_not_precise = True
    while is_not_precise:
        y = get_y(f, x)
        yd = get_y(fd, x)
        tn = tangente(x, y, yd)
        xr = x_reta(tn, 0.0)

        if xr == x:
            is_not_precise = False
        else:
            x = xr
            print xr

def derivada(f):
    g = len(f) - 1 # Grau da equação
    fd = list() # f'(x)

    for t in f: # Para cada termo da função
        fd.append(float(t*g)) # a*X^n -> n*a*X^(n-1)
        g = g - 1

    del fd[-1] # Derivada da constante ficou 0
    return fd

def get_y(f, x):
    g = len(f) - 1
    y = float()

    for t in f: # Para cada termo da função
        y += t*(x**g)
        g = g - 1

    return y

def tangente(x, y, yd):
    tn = list()

    tn.append(yd)
    tn.append((yd * x * -1) + y)

    return tn

def x_reta(f, y):
    xr = y + (f[1] * -1) / f[0]
    return xr

if __name__ == '__main__':
    fl = open('input-nr.txt', 'r')
    f = [float(t) for t in fl.readline().split(' ')]
    x = float(fl.readline())
    fl.close()

    main(f, x)
