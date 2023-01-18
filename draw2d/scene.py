# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    draw_sky(canvas,scene_width,scene_height)
    draw_ground(canvas, scene_width, scene_height)

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
    draw_oval(canvas, 750, 490, 350, 150, fill="yellow2")
    # draw_oval(canvas, 490, 490, 100, 100, fill="yellow2")
    draw_oval(canvas, 100, 100, 300, 200, fill="pink")

def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 2.5, width=0, fill="dodgerblue1")


# Call the main function so that
# this program will start executing.
main()