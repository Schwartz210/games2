__author__ = 'Avi Schwartz, Schwartz210@gmail.com'
import random
from Tkinter import *

class MainWindow():
    def __init__(self):
        self.grid_size = 600
        self.cell_size = 40
        self.half_cell = self.cell_size / 2
        self.tiles = self.grid_size / self.cell_size
        self.buffer_height = self.cell_size
        self.WIDTH = self.grid_size
        self.HEIGHT = self.grid_size + self.buffer_height
        self.button_dim = [self.cell_size * 3, self.cell_size / 2]
        self.master = Tk()
        self.master.title("Avi's implementation of Minesweeper")
        self.canvas = Canvas(self.master, width=self.WIDTH, height=self.HEIGHT)
        self.count = 0
        self.canvas.bind("<Button-1>", callback_left)
        self.canvas.bind("<Button-3>", callback_tester)

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

    def create_buttons(self):
        '''
        Generates grid at the beginning of the game
        '''
        self.canvas.create_rectangle(0, 0, self.button_dim[0], self.button_dim[1], fill="green")
        self.canvas.create_text(self.button_dim[0] / 2, self.button_dim[1] / 2, text="New game")

    def end_graphic(self, mine):
        '''
        This code is executed when player selects mine. The locations of the mines are displayed to the player-
        with "X"'s in red boxes.
        '''
        placement = mine.placement
        self.canvas.create_rectangle(placement[0] * self.cell_size,
                                     placement[1] * self.cell_size,
                                     placement[0] * self.cell_size + self.cell_size,
                                     placement[1] * self.cell_size + self.cell_size,
                                     fill="red")

        self.canvas.create_text(placement[0] * self.cell_size + self.half_cell,
                                placement[1] * self.cell_size + self.half_cell,
                                text="X", fill="black")

    def number_graphic(self, cell):
        placement = cell.placement
        mine_count = cell.mine_count
        self.canvas.create_text(placement[0] * self.cell_size + self.half_cell,
                                placement[1] * self.cell_size + self.half_cell,
                                text=mine_count, fill="black")

    def flag_graphic(self, cell):
        placement = cell.placement
        self.canvas.create_text(placement[0] * self.cell_size + self.half_cell,
                                placement[1] * self.cell_size + self.half_cell,
                                text="FLAG", fill="black")

    def grey_graphic(self, cell):
        placement = cell.placement
        self.canvas.create_rectangle(placement[0] * self.cell_size,
                                     placement[1] * self.cell_size,
                                     placement[0] * self.cell_size + self.cell_size,
                                     placement[1] * self.cell_size + self.cell_size,
                                     fill="grey")

class GameState():
    def __init__(self):
        self.mine_quantity = 35
        self.game_status = "start"
        self.mines = []
        self.flags = []
        self.selected_tiles = []
        self.cells = []
        self.cell_dict = {}

    def create_mines(self):
        '''
        Randomly generates mines at the beginning of the game.
        '''
        for cell in self.cells:
            cell.mine_probability()

    def trip_mine(self):
        '''
        Executes if player selects mine
        '''
        self.game_status = "game over"
        self.show_mines()

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
        self.cells = []
        self.cell_dict = {}
        self.create_cells()
        self.start_cells()
        self.create_cell_dict()
        self.create_mines()
        self.find_all_mines()
        self.next_cells()
        window.create_buttons()
        self.find_all_mines()

    def create_cells(self):
        for i in range(window.tiles):
            for j in range(window.tiles):
                placement = [i ,j + 1]
                a_cell = Cell(placement, True)
                self.cells.append(a_cell)

    def create_cell_dict(self):
        for cell in self.cells:
            self.cell_dict[cell.name] = cell

    def start_cells(self):
        for cell in self.cells:
            cell.start()

    def next_cells(self):
        for cell in self.cells:
            cell.next_phase()

    def find_all_mines(self):
        for cell in self.cells:
            if cell.is_mine:
                self.mines.append(cell)


class Cell():
    def __init__(self, placement, status):
        self.placement = placement
        self.status = status
        self.name = ""
        self.mine_count = 0
        self.adjacent_cells = []
        self.is_mine = False
        self.letters = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J",10:"K",11:"L",12:"M",13:"N",14:"O",15:"P"}

    def find_adjacent_cell(self):
        '''
        Takes mouseclick cell as input, find the quantity of mines adjacent to that cell (0 - 8). The a1 variable series
        represents all adjacent cells.
        '''
        self.adjacent_cells = []
        a1 = [self.placement[0] - 1, self.placement[1] - 1]  # upper left adjacent cell
        a2 = [self.placement[0], self.placement[1] - 1]  # upper adjacent cell
        a3 = [self.placement[0] + 1, self.placement[1] - 1]  # upper right adjacent cell
        a4 = [self.placement[0] - 1, self.placement[1]]  # left adjacent cell
        a5 = [self.placement[0] + 1, self.placement[1]]  # right adjacent cell
        a6 = [self.placement[0] - 1, self.placement[1] + 1]  # lower left adjacent cell
        a7 = [self.placement[0], self.placement[1] + 1]  # lower adjacent cell
        a8 = [self.placement[0] + 1, self.placement[1] + 1]  # lower right adjacent cell
        a_series = [a1, a2, a3, a4, a5, a6, a7, a8]
        for item in a_series:
            if 15 > item[0] >= 0 and 15 > item[1] >= 1:
                name = find_name(item)
                self.adjacent_cells.append(game.cell_dict[name])
        return self.adjacent_cells

    def mine_probability(self):
        a = random.randrange(5)
        if a == 0:
            self.is_mine = True

    def find_adjacent_mines(self):
        for adjacent_cell in self.adjacent_cells:
            if adjacent_cell in game.mines:
                self.mine_count += 1

    def create_name(self):
        a = self.letters[self.placement[0]]
        b = self.placement[1]
        self.name = a + str(b)
        return self.name

    def start(self):
        self.create_name()
        window.grey_graphic(self)

    def next_phase(self):
        self.find_adjacent_cell()
        self.find_adjacent_mines()

    def select_cell(self):
        window.number_graphic(self)
        if self.is_mine:
            game.trip_mine()


a_cell = Cell([1,1],True)

def find_name(placement):
    a = a_cell.letters[placement[0]]
    b = placement[1]
    name = a + str(b)
    return name

def detect_button(coordinates):
    '''
    Determines if player hit "New Game" button, if so start new game
    '''
    if coordinates[0] < window.button_dim[0] and coordinates[1] < window.button_dim[1]:
        game.new_game()

def detect_border(coordinates):
    if coordinates[1] < window.buffer_height:
        return True

def find_placement(coordinates):
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
    detect_button(coord)

    if detect_border(coord) == True:
        return None
    placement = find_placement(coord)
    name = find_name(placement)
    cell = game.cell_dict[name]
    cell.select_cell()

def callback_right(event):
    '''
    Handler for right mouseclick. This block of code executes everytime left-mouseclick event occurs.
    '''
    coord = [event.x, event.y]
    cell = find_cell(coord)
    if cell not in game.flags:
        window.flag_graphic(cell)
        game.flags.append(cell)
    else:
        window.grey_graphic()
        flags.remove(cell)

def callback_tester(event):
    coord = [event.x, event.y]
    detect_button(coord)
    placement = find_placement(coord)
    name = find_name(placement)
    cell = game.cell_dict[name]
    print cell.name


# Objects
window = MainWindow()
game = GameState()

# function calls
game.new_game()
window.event_timer()
window.canvas.pack()
window.master.mainloop()
