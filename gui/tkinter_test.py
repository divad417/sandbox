#!/usr/local/bin/python3

import tkinter as tk

image = '/Users/David/Documents/jumping_rook.png'

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()
canvas.create_image((0,0),image=image)
root.mainloop()