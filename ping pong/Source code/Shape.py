import turtle

# Base class for creating and managing a shape using turtle graphics
class Shape:
    def __init__(self):
        # Create a new turtle object to represent the shape
        self.shape = turtle.Turtle()

    # Method to define the properties of the shape (speed, shape, color, position, and size)
    def properties_of_shape(
        self, speed, shape, color, goto: tuple, stretch_wid=None, stretch_len=None
    ):
        # Set the movement speed of the shape (0 is instant, higher numbers slow down the movement)
        self.shape.speed(speed)

        # Set the shape of the turtle (e.g., "square", "circle")
        self.shape.shape(shape)

        # Set the color of the shape
        self.shape.color(color)

        # Lift the pen up to prevent drawing lines when the shape moves
        self.shape.penup()

        # Move the shape to the specified coordinates (x, y)
        self.shape.goto(x=goto[0], y=goto[1])

        # If stretch width and length are provided, resize the shape accordingly
        if stretch_len is not None and stretch_wid is not None:
            self.shape.shapesize(stretch_wid=stretch_wid, stretch_len=stretch_len)
