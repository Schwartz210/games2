__author__ = 'Avi Schwartz, Schwartz210@gmail.com'
import random
from Tkinter import *

<<<<<<< HEAD

=======
>>>>>>> origin/master
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

<<<<<<< HEAD

# Global variables
=======
#Global variables
>>>>>>> origin/master
master = Tk()
window = MainWindow(master)

master.title("Avi's implementation of Minesweeper")
<<<<<<< HEAD
mine_quantity = 35
=======
mine_quantity = 50
>>>>>>> origin/master
game_status = "start"
mines = []
flags = []
count = 0
selected_tiles = []

<<<<<<< HEAD

=======
>>>>>>> origin/master
def create_grid():
    '''
    Generates grid at the beginning of the game
    '''
<<<<<<< HEAD
    window.canvas.create_rectangle(0, 0, window.button_dim[0], window.button_dim[1], fill="green")
    window.canvas.create_text(window.button_dim[0] / 2, window.button_dim[1] / 2, text="New game")
    for i in range(window.tiles):
        for j in range(window.tiles):
            window.canvas.create_rectangle(i * window.cell_size, j * window.cell_size + window.buffer_height,
                                           i * window.cell_size + window.cell_size,
                                           j * window.cell_size + window.cell_size + window.buffer_height, fill="Grey")

=======
    window.canvas.create_rectangle(0,0,window.button_dim[0],window.button_dim[1] , fill="green")
    window.canvas.create_text(window.button_dim[0] / 2, window.button_dim[1] / 2, text="New game")
    for i in range(window.tiles):
        for j in range(window.tiles):
            window.canvas.create_rectangle(i * window.cell_size, j * window.cell_size + window.buffer_height, i * window.cell_size + window.cell_size, j * window.cell_size + window.cell_size + window.buffer_height, fill="Grey")
>>>>>>> origin/master

def create_mines():
    '''
    Randomly generates mines at the beginning of the game.
    '''
    global mines
    mines = []
    while len(mines) < mine_quantity:
<<<<<<< HEAD
        new_mine = [random.randrange(0, window.tiles), random.randrange(1, window.tiles)]
        if new_mine not in mines:
            mines.append(new_mine)


=======
        new_mine = [random.randrange(0,window.tiles), random.randrange(1,window.tiles)]
        if new_mine not in mines:
            mines.append(new_mine)

>>>>>>> origin/master
def detect_mine(cell):
    '''
    Determines if player selected a mine, if so game over, if not show number of adjacent mines
    '''
    global game_status, first_turn, selected_tiles
    if game_status == "game over": return None
    if cell[1] * window.cell_size < window.buffer_height: return None
    selected_tiles.append(cell)
    if cell in mines:
        game_status = "game over"
<<<<<<< HEAD
        window.canvas.create_rectangle(cell[0] * window.cell_size, cell[1] * window.cell_size,
                                       cell[0] * window.cell_size + window.cell_size,
                                       cell[1] * window.cell_size + window.cell_size, fill="red")
=======
        window.canvas.create_rectangle(cell[0] * window.cell_size, cell[1] * window.cell_size, cell[0] * window.cell_size + window.cell_size, cell[1] * window.cell_size + window.cell_size, fill="red")
>>>>>>> origin/master
        show_mines()
    else:
        return find_adjacent_mines(cell)

<<<<<<< HEAD

=======
>>>>>>> origin/master
def find_adjacent_cell(cell):
    '''
    Takes mouseclick cell as input, find the quantity of mines adjacent to that cell (0 - 8). The a1 variable series
    represents all adjacent cells.
    '''
<<<<<<< HEAD
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


def find_adjacent_mines(cell):
    adjacent_cells = find_adjacent_cell(cell)
    mine_count = 0  # accumulator variable
=======
    a1 = [cell[0] - 1, cell[1] - 1] #upper left adjacent cell
    a2 = [cell[0], cell[1] - 1]  #upper adjacent cell
    a3 = [cell[0] + 1, cell[1] -1]  #upper right adjacent cell
    a4 = [cell[0] - 1, cell[1]]  #left adjacent cell
    a5 = [cell[0] + 1, cell[1]]  #right adjacent cell
    a6 = [cell[0] - 1, cell[1] + 1]  #lower left adjacent cell
    a7 = [cell[0], cell[1] + 1]  #lower adjacent cell
    a8 = [cell[0] + 1, cell[1] + 1]  #lower right adjacent cell
    adjacent_cells = [a1,a2,a3,a4,a5,a6,a7,a8]
    return adjacent_cells

def find_adjacent_mines(cell):
    adjacent_cells = find_adjacent_cell(cell)
    mine_count = 0     #accumulator variable
>>>>>>> origin/master
    for adjacent_cell in adjacent_cells:
        if adjacent_cell in mines:
            mine_count += 1
    if mine_count == 0:
<<<<<<< HEAD
        electricity(cell)
    window.canvas.create_text(cell[0] * window.cell_size + window.half_cell,
                              cell[1] * window.cell_size + window.half_cell, text=mine_count, fill="black")


def zero_adjacent_mines(cell):
=======
        zero_adjacent_mines(cell)
    window.canvas.create_text(cell[0] * window.cell_size + window.half_cell, cell[1] * window.cell_size + window.half_cell, text=mine_count, fill="black")

def zero_adjacent_mines(cell):

>>>>>>> origin/master
    adjacent_cells_primary = find_adjacent_cell(cell)
    for adjacent_cell_p in adjacent_cells_primary:
        mine_count = 0
        adjacent_cell_secondary = find_adjacent_cell(adjacent_cell_p)
        for adjacent_cell_s in adjacent_cell_secondary:
            if adjacent_cell_s in mines:
                mine_count += 1
        if adjacent_cell_p not in selected_tiles:
<<<<<<< HEAD
            window.canvas.create_text(adjacent_cell_p[0] * window.cell_size + window.half_cell,
                                      adjacent_cell_p[1] * window.cell_size + window.half_cell, text=mine_count,
                                      fill="black")


def find_adjacent_zeros(cell):
    adjacent_zeros = []
    adjacent_cells_primary = find_adjacent_cell(cell)
    for adjacent_cell_p in adjacent_cells_primary:
        mine_count = 0
        adjacent_cells_secondary = find_adjacent_cell(adjacent_cell_p)
        for adjacent_cell_s in adjacent_cells_secondary:
            if adjacent_cell_s in mines:
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
        window.canvas.create_text(z[0] * window.cell_size + window.half_cell,
                                  z[1] * window.cell_size + window.half_cell,
                                  text=0)
=======
            window.canvas.create_text(adjacent_cell_p[0] * window.cell_size + window.half_cell, adjacent_cell_p[1] * window.cell_size + window.half_cell, text=mine_count, fill="black")
>>>>>>> origin/master


def detect_button(coordinates):
    '''
    Determines if player hit "New Game" button, if so start new game
    '''
    global game_status
    if coordinates[0] < window.button_dim[0] and coordinates[1] < window.button_dim[1]:
        new_game()

<<<<<<< HEAD

=======
>>>>>>> origin/master
def find_cell(coordinates):
    '''
    Converts input from mouse measured in pixels --> cell in canvas grid.
    '''
<<<<<<< HEAD
    cell_conversion = [0, 0]
    cell_conversion[0] = coordinates[0] / window.cell_size
    cell_conversion[1] = coordinates[1] / window.cell_size
    return cell_conversion


=======
    cell_conversion = [0,0]
    cell_conversion[0] = coordinates[0] / window.cell_size
    cell_conversion[1] = coordinates[1]  / window.cell_size
    return cell_conversion

>>>>>>> origin/master
def callback_left(event):
    '''
    Handler for left mouseclick. This block of code executes everytime left-mouseclick event occurs.
    '''
    coord = [event.x, event.y]
    cell = find_cell(coord)
    detect_button(coord)
    detect_mine(cell)

<<<<<<< HEAD

=======
>>>>>>> origin/master
def callback_right(event):
    '''
    Handler for right mouseclick. This block of code executes everytime left-mouseclick event occurs.
    '''
    global flags
    coord = [event.x, event.y]
    cell = find_cell(coord)
    if cell not in flags:
<<<<<<< HEAD
        window.canvas.create_text(cell[0] * window.cell_size + window.half_cell,
                                  cell[1] * window.cell_size + window.half_cell, text="FLAG", fill="black")
        flags.append(cell)
    else:
        window.canvas.create_rectangle(cell[0] * window.cell_size, cell[1] * window.cell_size,
                                       cell[0] * window.cell_size + window.cell_size,
                                       cell[1] * window.cell_size + window.cell_size, fill="grey")
        flags.remove(cell)


=======
        window.canvas.create_text(cell[0] * window.cell_size + window.half_cell, cell[1] * window.cell_size + window.half_cell, text="FLAG", fill="black")
        flags.append(cell)
    else:
        window.canvas.create_rectangle(cell[0] * window.cell_size,cell[1] * window.cell_size,cell[0] * window.cell_size + window.cell_size, cell[1] * window.cell_size + window.cell_size, fill="grey")
        flags.remove(cell)

>>>>>>> origin/master
def show_mines():
    '''
    This function is called at game over. It visually shows the player where the mines are located on the canvas
    '''
    for mine in mines:
<<<<<<< HEAD
        window.canvas.create_rectangle(mine[0] * window.cell_size, mine[1] * window.cell_size,
                                       mine[0] * window.cell_size + window.cell_size,
                                       mine[1] * window.cell_size + window.cell_size, fill="red")
        window.canvas.create_text(mine[0] * window.cell_size + window.half_cell,
                                  mine[1] * window.cell_size + window.half_cell, text="X", fill="black")


=======
        window.canvas.create_rectangle(mine[0] * window.cell_size, mine[1] * window.cell_size, mine[0] * window.cell_size + window.cell_size, mine[1] * window.cell_size + window.cell_size, fill="red")
        window.canvas.create_text(mine[0] * window.cell_size + window.half_cell, mine[1] * window.cell_size + window.half_cell, text="X", fill="black")
>>>>>>> origin/master
def counter():
    '''
    This function is called within the event timer. It updates the time counter, and draws it on the canvas.
    '''
    global count
<<<<<<< HEAD
    if game_status == "game over":
        pass
    else:
        count += 1

    window.canvas.create_rectangle(250, 0, 350, 40, fill="grey")
    window.canvas.create_text(300, 20, text=str(count))

=======
    if game_status == "game over": pass
    else: count += 1

    window.canvas.create_rectangle(250,0, 350, 40, fill="grey")
    window.canvas.create_text(300,20,text=str(count))
>>>>>>> origin/master

def event_timer():
    '''
    This block of code executes once per second.
    '''
    counter()
    window.canvas.after(1000, event_timer)

<<<<<<< HEAD

=======
>>>>>>> origin/master
def new_game():
    '''
    This function reinitializes game state
    '''
    global count, game_status, flags, selected_tiles
    count = 0
    game_status = "Start"
    flags = []
    selected_tiles = []
    create_grid()
    create_mines()


new_game()
event_timer()
<<<<<<< HEAD
window.canvas.bind("<Button-1>", callback_left)
window.canvas.bind("<Button-3>", callback_right)

window.canvas.pack()
=======
window.canvas.pack()
window.canvas.bind("<Button-1>",callback_left)
window.canvas.bind("<Button-3>",callback_right)
>>>>>>> origin/master
master.mainloop()
