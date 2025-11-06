# Ns 1st 🔨 Maze Generator
# import turtle and random 
import turtle 
import random 

maze_width = 10  
maze_height = 10 
cell_size = 30
screen_width = maze_width * cell_size
screen_height = maze_height * cell_size
wall = 1
empty = 0
star_pos = (0, 0)
end_pos = (maze_height - 1, maze_height - 1)

# set up the maze screen 
def setup_screen():
    screen = turtle.Screen()
    screen.setup(screen_width + 50, screen_height + 50 )
    screen.setup(0, 0, screen_width, screen_height)
    screen.bgcolor("white")

