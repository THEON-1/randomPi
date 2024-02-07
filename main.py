from tkinter import Tk
from calcPi import calcPi

def main(n=10000000):
    x = 1000
    y = 600
    root = Tk()

    root.geometry(str(x)+'x'+str(y)+'+300+300')

    cP = calcPi(100, 100)
    cP.run(n)
    cP.draw()

    cP.mainloop()

if __name__ == "__main__":
    main()