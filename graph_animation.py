#!/usr/local/bin/python3

import tkinter as tk
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = tk.Tk()
root.wm_title("Embedding in Tk")

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def animate(i):
        line.set_ydata(np.sin(x+i/10.0))  # update the data
        return line,

    canvas.get_tk_widget().grid(column=0,row=1)

    ax = fig.add_subplot(111)
    line, = ax.plot(x, np.sin(x))
    ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=False)

def _quit():
    root.quit()     # stops mainloop

button = tk.Button(master=root, text="Quit", command=_quit)
button.pack(side=tk.BOTTOM)

tk.mainloop()
