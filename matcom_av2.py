# -*- coding: utf-8 -*-

def main():
    f = [1,-2,3] # f(x)
    ix = 3 # Ponto X inicial

    x = ix
    fd = derivada(f)
    y = get_y(f, x)
    yd = get_y(fd, x)
    tn = tangente(x, y, yd)

    print f
    print fd
    print y
    print yd
    print tn

def derivada(f):
    g = len(f) - 1 # Grau da equação
    fd = list() # f'(x)

    for t in f: # Para cada termo da função
        fd.append(t*g) # a*X^n -> n*a*X^(n-1)
        g = g - 1

    del fd[-1] # Derivada da constante ficou 0
    return fd

def get_y(f, x):
    g = len(f) - 1
    y = int()

    for t in f: # Para cada termo da função
        y += t*(x**g)
        g = g - 1

    return y

def tangente(x, y, yd):
    tn = list()

    tn.append(yd)
    tn.append((yd * x * -1) + y)

    return tn

def get_x(f, y):
    pass

if __name__ == '__main__':
    main()
