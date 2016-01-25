__author__ = 'Avi'
from gui import window
from random import randint, choice

class GameState(object):
    def __init__(self):
        self.timer_count = 0
        self.coordinates_list = window.create_coordinates()
        self.smart_cells = self.create_cells()
        self.smart_cell_dict = self.build_smart_cell_dict()
        self.create_cells()
        self.show_all_cells()
        self.name = 'Test'

    def create_cells(self):
        output_list = []
        for coordinates in self.coordinates_list:
            smart_cell = SmartCell(coordinates)
            output_list.append(smart_cell)
        return output_list

    def build_smart_cell_dict(self):
        output_dict = {}
        for smart_cell in self.smart_cells:
            grid = window.convert_coordinates_to_grid(smart_cell.coordinates)
            name = self.make_name(grid)
            output_dict[name] = smart_cell
        return output_dict

    def show_all_cells(self):
        for smart_cell in self.smart_cells:
            window.display_cell(smart_cell)

    def make_name(self, coordinates):
        output_value = str(coordinates[0]) + '-' + str(coordinates[1])
        return output_value


class SmartCell(object):
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.color = 'grey'
        self.text = ''
        self.status = False

    def select(self):
        self.status = True
        self.color = 'blue'
        window.display_cell(self)

    def unselect(self):
        self.status = False
        self.color = 'grey'
        window.display_cell(self)


class Word(object):
    def __init__(self, word):
        self.word = word
        self.alignment = 'neutral'
        self.coordinates_list = []

    def random_coordinates(self):
        '''
        Generates random pair of coordinates
        '''
        output_list = []
        for i in range(2):
            random_coordinate = randint(20)
            output_list.append(random_coordinate)
        return output_list

    def convert_direction_to_vector(self, direction):
        if direction == 'left': vector = [-1,0]
        elif direction == 'right': vector = [1,0]
        elif direction == 'up': vector = [0,-1]
        elif direction == 'down': vector = [0,1]
        elif direction == 'left_up': vector = [-1,-1]
        elif direction == 'left_down': vector = [-1,1]
        elif direction == 'right_up': vector = [1,-1]
        elif direction == 'right_down': vector = [1,1]
        else: raise AttributeError
        return vector

    def next_coordinates(self, coordinates, direction):
        output_list = [0,0]
        vector = self.convert_direction_to_vector(direction[1])
        for i in range(2):
            output_list[i] = coordinates[i] + vector[i]
        return output_list

    def find_borders(self, coordinates):
        border = window.cells_per_row - 1
        output_list = [0,0,0,0]   #  [left/right/up/down]
        output_list[0] = ['left', coordinates[0]]
        output_list[1] = ['right', border - coordinates[0]]
        output_list[2] = ['up', coordinates[1]]
        output_list[3] = ['down', border - coordinates[1]]
        return output_list

    def find_available_directions(self, coordinates):
        '''
        Eliminates potential directions if the word can't fit without hitting a border
        '''
        output_list = []
        size = len(self.word)
        borders = self.find_borders(coordinates)
        for border in borders:
            if size < border[1]:
                output_list.append(border)
        return output_list

    def build_word_placement(self):
        '''
        Container function
        '''
        output_list = []
        count = len(self.word) - 1
        first_placement = self.random_coordinates()
        output_list.append(first_placement)
        available_directions = self.find_available_directions(first_placement)
        direction = choice(available_directions)
        for i in range(count):
            next_placement = self.next_coordinates(output_list[-1], direction)
            output_list.append(next_placement)
        return output_list