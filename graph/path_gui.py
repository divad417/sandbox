#!/usr/local/bin/python3

import numpy as np
import tkinter as tk

import path

class SearchWidget:
    def __init__(self, width=400, height=300, zoom=20):
        self.window_width = width
        self.window_height = height
        self.zoom = zoom

        self.start = None
        self.goal = None

        self.array_width = 0
        self.array_height = 0
        self.array = np.array(None, ndmin=2)
        self._expand_array()

        root = tk.Tk()
        root.title('Search Widget')
        root.minsize(100, 50)

        self.canvas = tk.Canvas(root, width=self.window_width, height=self.window_height)
        self.canvas.pack(fill='both', expand=True)

        self.canvas.bind('<Button-1>', self._on_left_click)
        self.canvas.bind('<B1-Motion>', self._on_drag)
        self.canvas.bind('<Button-2>', self._on_right_click)
        self.canvas.bind('<Configure>', self._on_resize)

        self.last_click_col = None
        self.last_click_row = None
        self.left_click_fill_value = 0
        self.right_click_mode = 0

        root.mainloop()

    def _on_left_click(self, event):
        cell = self._column_row(event)
        if cell:        
            self.left_click_fill_value = int(not self.array[cell])
            self._fill_square(event, self.left_click_fill_value)
 
    def _on_drag(self, event):
        self._fill_square(event, self.left_click_fill_value)

    def _on_right_click(self, event):
        if self.right_click_mode == 0:
            if self.start:
                self.array[self.start] = 0
            self.start = self._column_row(event)
            self.array[self.start] = 2
        elif self.right_click_mode == 1:
            if self.goal:
                self.array[self.goal] = 0
            self.goal = self._column_row(event)
            self.array[self.goal] = 3
        self.right_click_mode = int(not self.right_click_mode)
        if self.start and self.goal:
            self._on_solve()
        self._redraw()

    def _fill_square(self, event, fill_value):
        cell = self._column_row(event)
        if cell:
            self.array[cell] = fill_value
            self._redraw()

    def _column_row(self, event):
        column = int(event.x/self.zoom)
        row = int(event.y/self.zoom)
        if (0 <= column < int(self.window_width/self.zoom)
                and 0 <= row < int(self.window_height/self.zoom)):
            return (column, row)
        else:
            return False


    def _on_resize(self, event):
        self.window_width = event.width
        self.window_height = event.height
        self._expand_array()
        self._redraw()

    def _on_scroll(self, event):
        # print('Scroll by {}'.format(event.delta))  # broken in tkinter
        pass

    def _expand_array(self):
        width = int(self.window_width/self.zoom)
        height = int(self.window_height/self.zoom)
        if width > self.array.shape[0] or height > self.array.shape[1]:
            self.array_width = max(width, self.array_width)
            self.array_height = max(height, self.array_height)
            new_array = np.zeros((self.array_width, self.array_height))
            new_array[0:self.array.shape[0], 0:self.array.shape[1]] = self.array
            self.array = new_array

    def _redraw(self):
        self.canvas.delete('all')
        # Fill squares
        for column in range(self.array_width):
            for row in range(self.array_height):
                if self.array[column, row] == 1:
                    self._color_rectangle(column, row, 'black')
                elif self.array[column, row] == 2:
                    self._color_rectangle(column, row, 'green')
                elif self.array[column, row] == 3:
                    self._color_rectangle(column, row, 'red')
        # Draw lines
        for y in range(0, self.window_width, self.zoom):
            self.canvas.create_line(y, 0, y, self.window_height)
        for x in range(0, self.window_height, self.zoom):
            self.canvas.create_line(0, x, self.window_width, x)

    def _color_rectangle(self, column, row, color):
        self.canvas.create_rectangle(
            column * self.zoom, row * self.zoom,
            (column + 1) * self.zoom, (row + 1) * self.zoom,
            fill=color, outline='')

    def _on_solve(self):
        graph = path.Graph2D()
        graph.from_array(self.array)
        graph.set_bounds(start=self.start, goal=self.goal)
        graph.solve()

if __name__ == '__main__':
    w = SearchWidget()