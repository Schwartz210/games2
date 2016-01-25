__author__ = 'Avi'
from tkinter import *

class MainWindow(object):
    def __init__(self):
        self.master = Tk()
        self.width = 600
        self.height = 600
        self.cells_per_row = 20
        self.cell_size = self.width / self.cells_per_row
        self.half_cell_size = self.cell_size / 2
        self.canvas = Canvas(self.master, width=self.width,height=self.height)

    def end(self):
        self.canvas.pack()
        self.master.mainloop()

    def build_rect(self,coordinates, color):
        '''
        Build a rectangle the size of a cell. Coordinates correspond to top-left corner of cell.
        '''
        x_axis1, y_axis1 = coordinates
        x_axis2 = x_axis1 + self.cell_size
        y_axis2 = y_axis1 + self.cell_size
        self.canvas.create_rectangle(x_axis1,y_axis1, x_axis2, y_axis2, fill=color)

    def print_text(self, coordinates, text):
        x_axis = coordinates[0] + self.half_cell_size
        y_axis = coordinates[1] + self.half_cell_size
        self.canvas.create_text(x_axis, y_axis, text=text, fill='black')

    def display_cell(self, smart_cell):
        self.build_rect(smart_cell.coordinates, smart_cell.color)
        self.print_text(smart_cell.coordinates, smart_cell.text)

    def create_coordinates(self):
        output_list = []
        for i in range(self.cells_per_row):
            for j in range(self.cells_per_row):
                x_axis = i * self.cell_size
                y_axis = j * self.cell_size
                coordinates = [x_axis, y_axis]
                output_list.append(coordinates)
        return output_list

    def convert_coordinates_to_grid(self, coordinates):
        output_list = [0,0]
        output_list[0] = int(coordinates[0] / window.cell_size)
        output_list[1] = int(coordinates[1] / window.cell_size)
        return output_list


window = MainWindow()