# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def main():
    t = np.arange(0., 5., 0.2)
    plt.plot(t,t**2)
    plt.grid(True)

if __name__ == '__main__':
    plt.title('Minimos Quadrados')
    plt.axis([-2, 16, -2, 16])
    plt.plot([-100,100],[0,0], 'k-') # Linha X
    plt.plot([0,0],[-100,100], 'k-') # Linha Y
    main()
    plt.show()
