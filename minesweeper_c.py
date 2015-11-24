__author__ = 'Avi Schwartz, Schwartz210@gmail.com'
import random
from Tkinter import *

# Global variables
master = Tk()
master.title("Avi's implementation of Minesweeper")

class MainWindow():
    def __init__(self, main):
        self.grid_size = 600
        self.cell_size = 40
        self.half_cell = self.cell_size / 2
        self.tiles = self.grid_size / self.cell_size
        self.buffer_height = self.cell_size
        self.WIDTH = self.grid_size
        self.HEIGHT = self.grid_size + self.buffer_height
        self.button_dim = [self.cell_size * 3, self.cell_size / 2]
        self.canvas = Canvas(master, width=self.WIDTH, height=self.HEIGHT)
        self.count = 0
        self.canvas.bind("<Button-1>", callback_left)
        self.canvas.bind("<Button-3>", callback_right)

    def counter(self):
        '''
        This function is called within the event timer. It updates the time counter, and draws it on the canvas.
        '''
        if game.game_status == "game over":
            pass
        else:
            self.count += 1

        self.canvas.create_rectangle(250, 0, 350, 40, fill="grey")
        self.canvas.create_text(300, 20, text=str(self.count))

    def event_timer(self):
        '''
        This block of code executes once per second.
        '''
        self.counter()
        self.canvas.after(1000, self.event_timer)

    def create_grid(self):
        '''
        Generates grid at the beginning of the game
        '''
        self.canvas.create_rectangle(0, 0, self.button_dim[0], self.button_dim[1], fill="green")
        self.canvas.create_text(self.button_dim[0] / 2, self.button_dim[1] / 2, text="New game")
        for i in range(self.tiles):
            for j in range(self.tiles):
                self.canvas.create_rectangle(i * self.cell_size, j * self.cell_size + self.buffer_height,
                                             i * self.cell_size + self.cell_size,
                                             j * self.cell_size + self.cell_size + self.buffer_height, fill="Grey")

    def end_graphic(self, mine):
        '''
        This code is executed when player selects mine. The locations of the mines are displayed to the player-
        with "X"'s in red boxes.
        '''
        self.canvas.create_rectangle(mine[0] * self.cell_size, mine[1] * self.cell_size,
                               mine[0] * self.cell_size + self.cell_size,
                               mine[1] * self.cell_size + self.cell_size, fill="red")
        self.canvas.create_text(mine[0] * self.cell_size + self.half_cell,
                                  mine[1] * self.cell_size + self.half_cell, text="X", fill="black")

    def number_graphic(self, mine_count, cell):
        self.canvas.create_text(cell[0] * self.cell_size + self.half_cell,
                              cell[1] * self.cell_size + self.half_cell, text=mine_count, fill="black")

    def zero_graphic(self, cell):
        window.canvas.create_text(cell[0] * window.cell_size + window.half_cell,     #x axis
                                  cell[1] * window.cell_size + window.half_cell,     #y axis
                                  text=0)


class GameState():
    def __init__(self):
        self.mine_quantity = 35
        self.game_status = "start"
        self.mines = []
        self.flags = []
        self.selected_tiles = []

    def create_mines(self):
        '''
        Randomly generates mines at the beginning of the game.
        '''
        while len(self.mines) < self.mine_quantity:
            new_mine = [random.randrange(0, window.tiles), random.randrange(1, window.tiles)]
            if new_mine not in self.mines:
                self.mines.append(new_mine)

    def detect_mine(self, cell):
        '''
        Determines if player selected a mine, if so game over, if not show number of adjacent mines
        '''
        if self.game_status == "game over": return None
        if cell[1] * window.cell_size < window.buffer_height: return None
        self.selected_tiles.append(cell)
        if cell in self.mines:
            self.game_status = "game over"
            self.show_mines()
        else:
            return find_adjacent_mines(cell)

    def show_mines(self):
        '''
        This function is called at game over. It visually shows the player where the mines are located on the canvas
        '''
        for mine in self.mines:
            window.end_graphic(mine)

    def new_game(self):
        '''
        This function reinitializes game state
        '''
        window.count = 0  # in-game counter
        self.game_status = "Start"
        self.flags = []
        self.selected_tiles = []
        window.create_grid()
        self.create_mines()



def find_adjacent_mines(cell):
    adjacent_cells = find_adjacent_cell(cell)
    mine_count = 0  # accumulator variable
    for adjacent_cell in adjacent_cells:
        if adjacent_cell in game.mines:
            mine_count += 1
    if mine_count == 0:
        electricity(cell)
    window.number_graphic(mine_count, cell)

def zero_adjacent_mines(cell):
    adjacent_cells_primary = find_adjacent_cell(cell)
    for adjacent_cell_p in adjacent_cells_primary:
        mine_count = 0
        adjacent_cell_secondary = find_adjacent_cell(adjacent_cell_p)
        for adjacent_cell_s in adjacent_cell_secondary:
            if adjacent_cell_s in game.mines:
                mine_count += 1
        if adjacent_cell_p not in game.selected_tiles:
            window.number_graphic()

def find_adjacent_zeros(cell):
    adjacent_zeros = []
    adjacent_cells_primary = find_adjacent_cell(cell)
    for adjacent_cell_p in adjacent_cells_primary:
        mine_count = 0
        adjacent_cells_secondary = find_adjacent_cell(adjacent_cell_p)
        for adjacent_cell_s in adjacent_cells_secondary:
            if adjacent_cell_s in game.mines:
                mine_count += 1
        if mine_count == 0:
            adjacent_zeros.append(adjacent_cell_p)
    return adjacent_zeros

def electricity(cell):
    electric = []
    adjacent_zeros = find_adjacent_zeros(cell)
    for zero in adjacent_zeros:
        zero_2 = find_adjacent_zeros(zero)
        for z in zero_2:
            if z not in electric:
                electric.append(z)

    for z in electric:
        window.zero_graphic(z)

def find_adjacent_cell(cell):
    '''
        Takes mouseclick cell as input, find the quantity of mines adjacent to that cell (0 - 8). The a1 variable series
        represents all adjacent cells.
        '''
    adjacent_cells = []
    a1 = [cell[0] - 1, cell[1] - 1]  # upper left adjacent cell
    a2 = [cell[0], cell[1] - 1]  # upper adjacent cell
    a3 = [cell[0] + 1, cell[1] - 1]  # upper right adjacent cell
    a4 = [cell[0] - 1, cell[1]]  # left adjacent cell
    a5 = [cell[0] + 1, cell[1]]  # right adjacent cell
    a6 = [cell[0] - 1, cell[1] + 1]  # lower left adjacent cell
    a7 = [cell[0], cell[1] + 1]  # lower adjacent cell
    a8 = [cell[0] + 1, cell[1] + 1]  # lower right adjacent cell
    a_series = [a1, a2, a3, a4, a5, a6, a7, a8]
    for item in a_series:
        if not item[1] < 1:
            adjacent_cells.append(item)
    return adjacent_cells

def detect_button(coordinates):
    '''
    Determines if player hit "New Game" button, if so start new game
    '''
    global game_status
    if coordinates[0] < window.button_dim[0] and coordinates[1] < window.button_dim[1]:
        game.new_game()

def find_cell(coordinates):
    '''
    Converts input from mouse measured in pixels --> cell in canvas grid.
    '''
    cell_conversion = [0, 0]
    cell_conversion[0] = coordinates[0] / window.cell_size
    cell_conversion[1] = coordinates[1] / window.cell_size
    return cell_conversion

def callback_left(event):
    '''
    Handler for left mouseclick. This block of code executes everytime left-mouseclick event occurs.
    '''
    coord = [event.x, event.y]
    cell = find_cell(coord)
    detect_button(coord)
    game.detect_mine(cell)

def callback_right(event):
    '''
    Handler for right mouseclick. This block of code executes everytime left-mouseclick event occurs.
    '''
    global flags
    coord = [event.x, event.y]
    cell = find_cell(coord)
    if cell not in flags:
        window.canvas.create_text(cell[0] * window.cell_size + window.half_cell,
                                  cell[1] * window.cell_size + window.half_cell, text="FLAG", fill="black")
        flags.append(cell)
    else:
        window.canvas.create_rectangle(cell[0] * window.cell_size, cell[1] * window.cell_size,
                                       cell[0] * window.cell_size + window.cell_size,
                                       cell[1] * window.cell_size + window.cell_size, fill="grey")
        flags.remove(cell)


# Objects
window = MainWindow(master)
game = GameState()



game.new_game()
window.event_timer()


window.canvas.pack()
master.mainloop()
