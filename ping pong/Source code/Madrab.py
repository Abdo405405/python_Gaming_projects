from Shape import Shape

# Madrab (Paddle) class inherits from Shape
class Madrab(Shape):

    # Method to move the paddle (Madrab) upwards
    def shape_move_up(self):
        # Get the current y-coordinate of the paddle
        y = self.shape.ycor()

        # Increase the y-coordinate by 20 units if it's within the upper boundary (y < 240)
        # Otherwise, keep it at the upper boundary
        y += 0.5 if y < 240 else 0

        # Set the new y-coordinate for the paddle
        self.shape.sety(y)

    # Method to move the paddle (Madrab) downwards
    def shape_move_down(self):
        # Get the current y-coordinate of the paddle
        y = self.shape.ycor()

        # Decrease the y-coordinate by 20 units if it's within the lower boundary (y > -240)
        # Otherwise, keep it at the lower boundary
        y -= 0.5 if -240 < y else 0

        # Set the new y-coordinate for the paddle
        self.shape.sety(y)
