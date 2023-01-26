# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    draw_sky(canvas,scene_width,scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_fish(canvas, 150, 150)
    draw_fish2(canvas, 60, 80)
    draw_fish1(canvas, 200, 110)
    draw_fish2(canvas, 500, 90)
    draw_fish(canvas, 600, 110)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.



    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 2.5,
        scene_width, scene_height, width=0, fill="chocolate1")
    draw_oval(canvas, 750, 490, 350, 150, width=0, fill="yellow2")
    # draw_oval(canvas, 490, 490, 100, 100, fill="yellow2")
    draw_oval(canvas, 50, 50, 350, 300, width=0, fill='gray10')
    draw_oval(canvas, -50, 50, 300, 300, width=0, fill='gray10')
    draw_oval(canvas, 100, 50, 500, 300, width=0, fill='gray10')
    draw_oval(canvas, 50, 400, 300, 450, width=0, fill='ivory1')
    draw_oval(canvas, 0, 400, 200, 450, width=0, fill='ivory1')
    draw_oval(canvas, 300, 300, 600, 350, width=0, fill='ivory1')
    draw_oval(canvas, 450, 400, 800, 450, width=0, fill='ivory1')

    

def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0,scene_width, scene_height / 2.5, width=0, fill="dodgerblue1")
    half_height = round(scene_height / 3)
    min_diam = 15
    max_diam = 30
    for i in range(100):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(0, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter, width=0,
                fill="skyblue")
def draw_fish(canvas, peak_x, peak_y):
    skirt_left  = peak_x - 40
    skirt_right = peak_x - 10
    skirt_bottom = peak_y - 40
    trunk_left  = peak_x - 10
    trunk_right = peak_x + 90
    trunk_bottom = peak_y + 0
    skirt_bottoms = peak_y - 50
    draw_oval(canvas, trunk_left, trunk_bottom, trunk_right, skirt_bottoms, width=0, fill='saddlebrown')
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y,skirt_right, skirt_bottom, outline='saddlebrown', fill="saddlebrown")
def draw_fish1(canvas, peak_x, peak_y):
    skirt_left  = peak_x - 40
    skirt_right = peak_x - 10
    skirt_bottom = peak_y - 40
    trunk_left  = peak_x - 10
    trunk_right = peak_x + 90
    trunk_bottom = peak_y + 0
    skirt_bottoms = peak_y - 50
    draw_oval(canvas, trunk_left, trunk_bottom, trunk_right, skirt_bottoms, width=0, fill='hotpink')
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y,skirt_right, skirt_bottom, outline='hotpink', fill="hotpink")
def draw_fish2(canvas, peak_x, peak_y):
    skirt_left  = peak_x - 40
    skirt_right = peak_x - 10
    skirt_bottom = peak_y - 40
    trunk_left  = peak_x - 10
    trunk_right = peak_x + 90
    trunk_bottom = peak_y + 0
    skirt_bottoms = peak_y - 50
    draw_oval(canvas, trunk_left, trunk_bottom, trunk_right, skirt_bottoms, width=0, fill='yellow1')
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y,skirt_right, skirt_bottom, outline='yellow1', fill="yellow1")
# Call the main function so that
# this program will start executing.
main()