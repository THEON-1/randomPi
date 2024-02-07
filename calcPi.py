from tkinter import Canvas, Frame, BOTH
from matplotlib import colors
from numpy import pi, gcd
from random import random
from math import sqrt, floor
#from util.numberTheory import isCoprime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class calcPi(Frame):

    def __init__(self, x, y) -> None:
        super().__init__()
        self.dimensions = (x, y)
        self.initialize_draw()
    
    def initialize_vals(self, digits, n):
        self.limit = 2**digits
        self.coprime = 0
        self._coprime = 0
        self.pi_approx = [0]*n

    def initialize_draw(self):
        self.master.title('RandomPi')
        self.pack(fill=BOTH, expand=1)
        self.figure = plt.figure()
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack(fill=BOTH, expand=1)
        self.pack(fill=BOTH, expand=1)
    
    def draw(self):
        n = self.coprime + self._coprime
        offset = 14000/n
        y = self.pi_approx[-1]
        plt.axes(ylim=[pi-offset, pi+offset])
        plt.plot(self.pi_approx)
        plt.axhline(y=y)
        plt.axhline(y=pi, color='red')
        ticks, _ = plt.yticks()
        labels = ['{:1.3f}'.format(t) for t in ticks] \
            + ["{:1.3f}           ".format(y), \
                'π                      ']
        plt.yticks(list(ticks) + [y, pi], labels)
        plt.xlabel(f'approx. π: {y}, error: {abs(pi-y)}')

    def run(self, n):
        self.initialize_vals(24, n)
        for i in range(n):
            self._run_step(i)

    def _run_step(self, i):
        self.step()
        self.calcPi(i)

    def step(self):
        r1 = floor(random() * self.limit)
        r2 = floor(random() * self.limit)
        if gcd(r1, r2) == 1:
            self.coprime += 1
        else:
            self._coprime += 1

    def calcPi(self, i):
        cp = self.coprime
        _cp = self._coprime
        if not cp == 0:
            self.pi_approx[i] = sqrt(6/(cp/(cp+_cp)))
