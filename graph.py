import os

import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def main():

    plot()


def plot():

    halflives = np.arange(0, 5.1, 0.1)
    remaining = 0.5**halflives

    plt.grid(visible=True, which='major', axis='both')

    plt.plot(halflives, remaining, color='#404040', linewidth=0.5)

    plt.xlabel('H a l f - L i v e s')
    plt.ylabel('R e m a i n i n g')

    plt.yticks([1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0], [1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0])

    plt.scatter([0,1,2,3,4,5], [1, 0.5, 0.25, 0.125, 0.0625, 0.03125], color='#404040', marker='o')

    plt.show()


main()
