__author__ = 'Avi'
from gui import window
from GameEngine import GameState



game = GameState()

def convert_click_to_cell(event):
    coordinates = [event.x, event.y]
    grid = window.convert_coordinates_to_grid(coordinates)
    name = game.make_name(grid)
    cell = game.smart_cell_dict[name]
    return cell

def callback_right(event):
    cell = convert_click_to_cell(event)
    cell.unselect()

def callback_left(event):
    cell = convert_click_to_cell(event)
    cell.select()


window.canvas.bind('<Button-1>',callback_left)
window.canvas.bind('<Button-3>',callback_right)
window.end()